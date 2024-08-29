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


cwd = pathlib.Path(__file__).parent.resolve()


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
            token=None,
            hostname=None,
            http_path=None,
            fname_databricks_env=None
    ):
        """
        Initializes the DatabricksAPI class and establishes a connection to the
        Databricks cluster.

        Parameters:
        -----------
        token : str, optional
            The access token for authentication with Databricks (default is None).
        hostname : str, optional
            The hostname of the Databricks server (default is None).
        http_path : str, optional
            The HTTP path for the Databricks SQL endpoint (default is None).
        fname_databricks_env : str, optional
            The file name of the environment file containing connection parameters
            (default is None).
        """
        self._TOKEN = token
        self._HOSTNAME = hostname
        self._HTTP_PATH = http_path
        self._sql_client = None
        self._URL = None
        self._workspace_client = None

        if fname_databricks_env is not None:
            print('Parsing env file')
            self._process_env(fname_databricks_env=fname_databricks_env)

        self._connect(
            token=self._TOKEN,
            hostname=self._HOSTNAME,
            http_path=self._HTTP_PATH
        )

    def _connect(
        self,
        token,
        hostname,
        http_path
    ):
        """
        Establishes a connection to the Databricks cluster using the provided
        access token, hostname, and HTTP path.

        Parameters:
        -----------
        token : str
            The access token for authentication with Databricks.
        hostname : str
            The hostname of the Databricks server.
        http_path : str
            The HTTP path for the Databricks SQL endpoint.

        Returns:
        --------
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
            token=token
        )

        print('Connected.')

        self._sql_client = connection
        self._workspace_client = workspace_client


        return None

    def _process_env(
            self,
            fname_databricks_env
    ):
        """
        Processes the environment file to extract connection parameters such as
        the access token, hostname, HTTP path, and URL.

        Parameters:
        -----------
        fname_databricks_env : str
            The file name of the environment file containing connection parameters.

        Returns:
        --------
        None
        """

        dict_config = dotenv_values(fname_databricks_env)

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
            fname_sql
    ):
        """
        Executes a Spark SQL query from a file and returns the result as a pandas
        DataFrame.

        Parameters:
        -----------
        fname_sql : str
            The file name of the SQL file containing the query.

        Returns:
        --------
        df : pandas.DataFrame
            A DataFrame containing the results of the query.
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
    ):
        """
        Executes a Spark SQL query from a string and returns the result as a pandas
        DataFrame.

        Parameters:
        -----------
        sql : str
           The Spark SQL query string to be executed.

        Returns:
        --------
        df : pandas.DataFrame
           A DataFrame containing the results of the query.
        """

        cursor = self._sql_client.cursor()
        for i,query in enumerate(sql.split(';')):
            cursor.execute(query)

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
        # Read csv/tsv file from volume and convert into Pandas dataframe
        response = self._workspace_client.files.download(volume_path)
        data_str = BytesIO(response.contents.read())
        df = pd.read_csv(data_str, sep=sep)

        return df

    def write_db_obj(
            self,
            df: pd.DataFrame,
            volume_path: str,
            sep: Optional[str] = '\t',
            overwrite: Optional[bool] = True,
            dict_database_table_info: Optional[dict] = None
    ):
        """
        If `dict_database_table_info` is used, it must contain these keys
        - catalog: Databricks catalog used
        - schema: Schema within the catalog
        - table: Table in the schema that will contain the dataframe information
        - volume_path: Path location on the volume of the object. A csv file for use of this
        - sep_of_volume_obj: File separator used for the object. Typically, comma or tab separated

        """

        csv_bytes = df.to_csv(index=False, sep=sep).encode("utf-8")
        csv_buffer = BytesIO(csv_bytes)

        print('Writing to %s' % volume_path)
        self._workspace_client.files.upload(
            volume_path,
            csv_buffer,
            overwrite=overwrite
        )
        print('Write to volume complete')

        if dict_database_table_info is not None:

            if sep != dict_database_table_info.get('sep'):
                dict_database_table_info['sep'] = sep
                print("Conflict with separator in dict; setting to value object was saved as.")

            self.create_table_from_volume(
                connection=self._workspace_client,
                dict_database_table_info=dict_database_table_info
            )

        return None

    def _sql_write_creator(
            self,
            catalog,
            schema,
            table,
            volume_path,
            sep='\t'
    ):
        sql_write = f"""
        DROP TABLE IF EXISTS {catalog}.{schema}.{table};
        CREATE TABLE IF NOT EXISTS {catalog}.{schema}.{table};
       
        COPY INTO {catalog}.{schema}.{table} FROM (
        SELECT *, _metadata FROM '{volume_path}'
        ) 
        FILEFORMAT = CSV 
        FORMAT_OPTIONS ('delimiter' = '{sep}', 'header' = 'true') 
        COPY_OPTIONS ('mergeSchema' = 'true');
        
        """

        return sql_write

    def create_table_from_volume(
            self,
            dict_database_table_info
    ):
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
        --------
        None
        """
        cursor = self._sql_client.cursor()
        cursor.close()
        self._sql_client.close()
        print('Databricks connection closed')

        return None


