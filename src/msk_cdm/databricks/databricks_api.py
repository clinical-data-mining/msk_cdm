import os, logging
import pathlib
from dotenv import dotenv_values
from io import BytesIO, StringIO

from databricks import sql
from databricks.sdk import WorkspaceClient
from mkdocs.config.config_options import Optional
from sqlalchemy import (
    create_engine,
    URL
)
import pandas as pd
import certifi

from databricks.sdk.core import Config, oauth_service_principal 

cwd = pathlib.Path(__file__).parent.resolve()
TIMEOUT_TIME = 1800             # 30 min timeout in seconds
CHUNK_SIZE = 50 * 1024 * 1024   # 50MB upload chunks


logging.getLogger("databricks.sql").setLevel(logging.DEBUG)
# logging.getLogger(sql_path).setLevel(logging.DEBUG)
logging.basicConfig(
    filename = os.path.join(cwd, "results.log"),
    level    = logging.DEBUG
)

os.environ['SSL_CERT_FILE'] = certifi.where()
os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()


class DatabricksAPI(object):
    """A class to interact with Databricks through its SQL API. This class allows
    connecting to a Databricks cluster, executing queries, and retrieving
    the results as pandas DataFrames."""
    def __init__(
            self,
            client_id: Optional[str] = None,  # Client ID for Service Principal
            client_secret: Optional[str] = None,  # Client Secret for Service Principal
            token: Optional[str] = None,
            hostname: Optional[str] = None,
            http_path: Optional[str] = None,
            fname_databricks_env: Optional[str] = None
    ) -> None:
        """Initializes the DatabricksAPI class with minimal changes for OAuth.
        
        
        Args:
            client_id: Client ID for Service Principal.
            client_secret: Client Secret for Service Principal.
            token: The access token for authentication with Databricks (default is None).
            hostname: The hostname of the Databricks server (default is None).
            http_path: The HTTP path for the Databricks SQL endpoint (default is None).
            fname_databricks_env: The file name of the environment file containing connection parameters (default is None).
        """
        self._client_id = client_id
        self._client_secret = client_secret
        self._TOKEN = token
        self._HOSTNAME = hostname
        self._HTTP_PATH = http_path
        self._sql_client = None
        self._URL = None
        self._workspace_client = None

        if fname_databricks_env is not None:
            print('Parsing env file')
            self._process_env(fname_databricks_env=fname_databricks_env)

        if self._client_secret is not None:
            self._connect_with_oauth(
                client_id=self._client_id,
                client_secret=self._client_secret,
                hostname=self._HOSTNAME,
                http_path=self._HTTP_PATH
            )

        if self._TOKEN is not None:
            self._connect_with_token(
                token=self._TOKEN,
                hostname=self._HOSTNAME,
                http_path=self._HTTP_PATH
            )

        return None
    
    
    def _connect_with_oauth(
        self,
        client_id: str,
        client_secret: str,
        hostname: str,
        http_path: str
    ) -> None:
        """ Connect with Service Principle credentials.
        Establishes a connection to the Databricks cluster using OAuth authentication.

        Args:
            client_id: The client ID of the service principal for OAuth authentication.
            client_secret: The client secret of the service principal for OAuth authentication.
            hostname: The hostname of the Databricks server.
            http_path: The HTTP path for the Databricks SQL endpoint.

        Returns:
            None
        """
        print('Making databricks connection')

        def credential_provider():
            config = Config(
                host          = hostname,
                client_id     = client_id,
                client_secret = client_secret)
            return oauth_service_principal(config)

        connection = sql.connect(
            server_hostname=hostname,
            http_path=http_path,
            credentials_provider=credential_provider
        )

        workspace_client = WorkspaceClient(
            host=hostname,
            client_id=client_id,
            client_secret=client_secret,
            retry_timeout_seconds=TIMEOUT_TIME
        )

        print('Connected.')

        self._sql_client = connection
        self._workspace_client = workspace_client

        return None

    def _connect_with_token(
            self,
            token: str,
            hostname: str,
            http_path: str
    ) -> None:
        """ Connection with personal token
        Establishes a connection to the Databricks cluster using the provided
        access token, hostname, and HTTP path.

        Args:
            token: The access token for authentication with Databricks.
            hostname: The hostname of the Databricks server.
            http_path: The HTTP path for the Databricks SQL endpoint.

        Returns:
            None
        """
        print('Making databricks connection')
        connection = sql.connect(
            server_hostname=hostname,
            http_path=http_path,
            access_token=token
        )

        workspace_client = WorkspaceClient(
            host=hostname,
            token=token,
            retry_timeout_seconds=TIMEOUT_TIME
        )

        print('Connected.')

        self._sql_client = connection
        self._workspace_client = workspace_client

        return None

    def _process_env(
            self,
            fname_databricks_env: str
    ) -> None:
        """
        Processes the environment file to extract connection parameters such as
        the access token, hostname, HTTP path, and URL.

        Args:
            fname_databricks_env: The file name of the environment file containing connection parameters.

        Returns:
            None
        """

        dict_config = dotenv_values(fname_databricks_env)

        if not self._client_id:
            self._client_id = dict_config.get("CLIENT_ID", None)  # Retrieve client_id from the environment
        if not self._client_secret:
            self._client_secret = dict_config.get("CLIENT_SECRET", None)  # Retrieve client_secret from the environment
        if not self._TOKEN:
            self._TOKEN = dict_config.get("TOKEN", None)
        if not self._HOSTNAME:
            self._HOSTNAME = dict_config.get("HOSTNAME", None)
        if not self._URL:
            self._URL = dict_config.get("URL", None)
        if not self._HTTP_PATH:
            self._HTTP_PATH = dict_config.get("HTTP_PATH", None)

        return None

    def query_from_file(
            self,
            *,
            fname_sql: str
    ) -> pd.DataFrame:
        """Query Databricks from a SQL file
        Executes a Spark SQL query from a file and returns the result as a pandas
        DataFrame.

        Args:
            fname_sql: The file name of the SQL file containing the query.

        Returns:
            df: A DataFrame containing the results of the query.
        """
        # open SQL file
        fd = open(fname_sql, 'r')
        sqlFile = fd.read()
        fd.close()

        print('Preview of SQL in %s:' % fname_sql)
        print(sqlFile[:50])

        df = self.query_from_sql(sql=sqlFile)

        return df

    def query_from_sql(
            self,
            *,
            sql: str
    ) -> pd.DataFrame:
        """Query Databricks from a SQL string
        Executes a Spark SQL query from a string and returns the result as a pandas
        DataFrame.

        Args:
            sql: The Spark SQL query string to be executed.

        Returns:
            df: A DataFrame containing the results of the query.
        """

        cursor = self._sql_client.cursor()
        for i,query in enumerate(sql.split(';')):
            cursor.execute(query)

        ### Another way to do the query above is through SQLalchemy
        # engine = create_engine(
        #     url = f"databricks://token:{token}@{hostname}?" +
        #           f"http_path={http_path}&catalog={catalog}&schema={schema}"
        # )
        #
        # with engine.connect() as conn:
        #     # This will read the contents of `main.test.some_table`
        #     df_sql = pd.read_sql(f"SELECT *, _metadata FROM {catalog}.{schema}.{table}", conn)


        # Gather column names from query
        column_names = [desc[0] for desc in cursor.description]
        data = cursor.fetchall()

        # Convert to pandas dataframe
        df = pd.DataFrame(
            data,
            columns=column_names
        )

        return df

    def read_db_obj(
            self,
            volume_path: str,
            sep: Optional[str] ='\t'
    ) -> pd.DataFrame:
        """Read object from Databricks volume
        Reads a CSV/TSV file from the Databricks volume and converts it into a
        pandas DataFrame.

        Args:
            volume_path: The path to the file on the Databricks volume.
            sep: The separator used in the file.

        Returns:
            df: A DataFrame containing the data from the file.
        """
        # Read csv/tsv file from volume and convert into Pandas dataframe
        response = self._workspace_client.files.download(volume_path)
        data_str = BytesIO(response.contents.read())
        df = pd.read_csv(data_str, sep=sep)

        return df

    def create_directory_on_volume(
            self,
            path: str
    ) -> None:
        """
        Creates a directory on the Databricks volume at the specified path.

        Args:
            path: The path where the directory should be created.

        Returns:
            None
        """
        # Create a directory for file to be uploaded
        print('Creating directory on volume: %s' % path)
        self._workspace_client.files.create_directory(path)

        print('Created')

    def write_db_obj(
            self,
            df: pd.DataFrame,
            volume_path: str,
            sep: Optional[str] = '\t',
            overwrite: Optional[bool] = True,
            dict_database_table_info: Optional[dict] = None
    ):
        """Write data to Databricks volume
        Writes a pandas DataFrame to a CSV file on the Databricks volume. Optionally,
        creates a table in Databricks from the CSV file.

        Args:
            df: The DataFrame to be written to the file.
            volume_path: The path where the file should be saved on the Databricks volume.
            sep: The separator used in the file.
            overwrite: Whether to overwrite the existing file.
            dict_database_table_info: A dictionary containing information about the
                                      database table. If `dict_database_table_info` is used, it must contain these keys

                                        - catalog: Databricks catalog used
                                        - schema: Schema within the catalog
                                        - table: Table in the schema that will contain the dataframe information
                                        - volume_path: Path location on the volume of the object. A csv file for use of this
                                        - sep: File separator used for the object. Typically, comma or tab separated

        Returns:
            None


        """
        # Create directory on volume for data to be uploaded. If directory, exists, nothing will happen to existing data
        dir_volume_path = os.path.dirname(volume_path)
        self.create_directory_on_volume(path=dir_volume_path)

        csv_bytes = df.to_csv(index=False, sep=sep).encode("utf-8")
        csv_buffer = BytesIO(csv_bytes)

        print('Writing to %s' % volume_path)
        self._workspace_client.files.upload(
            volume_path,
            csv_buffer,
            overwrite=overwrite,
            chunk_size=CHUNK_SIZE
        )
        print('Write to volume complete')

        if dict_database_table_info is not None:
            if sep != dict_database_table_info.get('sep'):
                dict_database_table_info['sep'] = sep
                print("Conflict with separator in dict; setting to value object was saved as.")

            self.create_table_from_volume(dict_database_table_info=dict_database_table_info)

        return None

    def _sql_write_creator(
            self,
            catalog: str,
            schema: str,
            table: str,
            volume_path: str,
            sep: Optional[str] = '\t'
    ) -> str:
        """
        Generates a SQL query string to create a table in Databricks from a file
        located on the Databricks volume.

        Args:
            catalog: The catalog in which the table will be created.
            schema: The schema within the catalog.
            table: The name of the table to be created.
            volume_path: The path to the file on the Databricks volume.
            sep: The separator used in the file.

        Returns:
            sql_write: A SQL query string to create the table.
        """
        sql_write = f"""
        DROP TABLE IF EXISTS {catalog}.{schema}.{table};
        CREATE TABLE IF NOT EXISTS {catalog}.{schema}.{table};
       
        COPY INTO {catalog}.{schema}.{table} FROM '{volume_path}'
        FILEFORMAT = CSV 
        FORMAT_OPTIONS ('delimiter' = '{sep}', 'header' = 'true') 
        COPY_OPTIONS ('mergeSchema' = 'true');
        
        """

        return sql_write

    def create_table_from_volume(
            self,
            dict_database_table_info: dict
    ) -> None:
        """
        Creates a SQL table in Databricks from a file located on the Databricks volume.

        Args:
            dict_database_table_info: A dictionary containing information about the
                                      database table. If `dict_database_table_info` is used, it must contain these keys

                                        - catalog: Databricks catalog used
                                        - schema: Schema within the catalog
                                        - table: Table in the schema that will contain the dataframe information
                                        - volume_path: Path location on the volume of the object. A csv file for use of this
                                        - sep: File separator used for the object. Typically, comma or tab separated

        Returns:
            None
        """
        catalog = dict_database_table_info.get('catalog')
        schema = dict_database_table_info.get('schema')
        table = dict_database_table_info.get('table')
        volume_path = dict_database_table_info.get('volume_path')
        sep_of_volume_obj = dict_database_table_info.get('sep')
        print('Creating SQL table from volume:')
        print('Catalog: %s' % catalog)
        print('Schema: %s' % schema)
        print('Table: %s' % table)
        print('Volume path: %s' % volume_path)
        print('Separator: %s' % sep_of_volume_obj)

        sql_write = self._sql_write_creator(
            catalog=catalog,
            schema=schema,
            table=table,
            volume_path=volume_path,
            sep=sep_of_volume_obj
        )

        cursor = self._sql_client.cursor()
        for i,query in enumerate(sql_write.split(';')[:-1]):
            print(query)
            cursor.execute(query)

        print('Table created')

        return None


    def close_connection(self):
        """
        Closes the connection to the Databricks cluster.

        Returns:
            None
        """
        cursor = self._sql_client.cursor()
        cursor.close()
        self._sql_client.close()
        print('Databricks connection closed')

        return None
