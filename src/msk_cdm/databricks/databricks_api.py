import os, logging
import pathlib
from dotenv import dotenv_values
from io import BytesIO, StringIO
from typing import Any
import json

from databricks import sql
from databricks.sdk import WorkspaceClient
from databricks.connect import DatabricksSession
from mkdocs.config.config_options import Optional
from sqlalchemy import create_engine, URL
import pandas as pd
import certifi

from databricks.sdk.core import Config, oauth_service_principal

cwd = pathlib.Path(__file__).parent.resolve()


logging.getLogger("databricks.sql").setLevel(logging.DEBUG)
# logging.getLogger(sql_path).setLevel(logging.DEBUG)
logging.basicConfig(filename=os.path.join(cwd, "results.log"), level=logging.DEBUG)

os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()


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
        cluster_id: Optional[str] = None,
        fname_databricks_env: Optional[str] = None,
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
        self._CLUSTER_ID = cluster_id
        self._sql_client = None
        self._URL = None
        self._workspace_client = None

        if fname_databricks_env is not None:
            print("Parsing env file")
            self._process_env(fname_databricks_env=fname_databricks_env)

        if self._client_secret is not None:
            self._connect_with_oauth(
                client_id=self._client_id,
                client_secret=self._client_secret,
                hostname=self._HOSTNAME,
                http_path=self._HTTP_PATH,
            )

        if self._TOKEN is not None:
            self._connect_with_token(
                token=self._TOKEN, hostname=self._HOSTNAME, http_path=self._HTTP_PATH
            )

        return None

    def _connect_with_oauth(
        self, client_id: str, client_secret: str, hostname: str, http_path: str
    ) -> None:
        """Connect with Service Principle credentials.
        Establishes a connection to the Databricks cluster using OAuth authentication.

        Args:
            client_id: The client ID of the service principal for OAuth authentication.
            client_secret: The client secret of the service principal for OAuth authentication.
            hostname: The hostname of the Databricks server.
            http_path: The HTTP path for the Databricks SQL endpoint.

        Returns:
            None
        """
        print("Making databricks connection")

        def credential_provider():
            config = Config(
                host=hostname, client_id=client_id, client_secret=client_secret
            )
            return oauth_service_principal(config)

        connection = sql.connect(
            server_hostname=hostname,
            http_path=http_path,
            credentials_provider=credential_provider,
        )

        workspace_client = WorkspaceClient(
            host=hostname, client_id=client_id, client_secret=client_secret
        )

        print("Connected.")

        self._sql_client = connection
        self._workspace_client = workspace_client

        return None

    def _connect_with_token(self, token: str, hostname: str, http_path: str) -> None:
        """Connection with personal token
        Establishes a connection to the Databricks cluster using the provided
        access token, hostname, and HTTP path.

        Args:
            token: The access token for authentication with Databricks.
            hostname: The hostname of the Databricks server.
            http_path: The HTTP path for the Databricks SQL endpoint.

        Returns:
            None
        """
        print("Making databricks connection")
        connection = sql.connect(
            server_hostname=hostname, http_path=http_path, access_token=token
        )

        workspace_client = WorkspaceClient(host=hostname, token=token)

        print("Connected.")

        self._sql_client = connection
        self._workspace_client = workspace_client

        return None

    def _process_env(self, fname_databricks_env: str) -> None:
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
            self._client_id = dict_config.get(
                "CLIENT_ID", None
            )  # Retrieve client_id from the environment
        if not self._client_secret:
            self._client_secret = dict_config.get(
                "CLIENT_SECRET", None
            )  # Retrieve client_secret from the environment
        if not self._TOKEN:
            self._TOKEN = dict_config.get("TOKEN", None)
        if not self._HOSTNAME:
            self._HOSTNAME = dict_config.get("HOSTNAME", None)
        if not self._URL:
            self._URL = dict_config.get("URL", None)
        if not self._HTTP_PATH:
            self._HTTP_PATH = dict_config.get("HTTP_PATH", None)
        if not self._CLUSTER_ID:
            self._CLUSTER_ID = dict_config.get("DATABRICKS_CLUSTER_ID", None)

        return None

    def query_from_file(self, *, fname_sql: str) -> pd.DataFrame:
        """Query Databricks from a SQL file
        Executes a Spark SQL query from a file and returns the result as a pandas
        DataFrame.

        Args:
            fname_sql: The file name of the SQL file containing the query.

        Returns:
            df: A DataFrame containing the results of the query.
        """
        # open SQL file
        fd = open(fname_sql, "r")
        sqlFile = fd.read()
        fd.close()

        print("Preview of SQL in %s:" % fname_sql)
        print(sqlFile[:50])

        df = self.query_from_sql(sql=sqlFile)

        return df

    def query_from_sql(self, *, sql: str) -> pd.DataFrame:
        """Query Databricks from a SQL string
        Executes a Spark SQL query from a string and returns the result as a pandas
        DataFrame.

        Args:
            sql: The Spark SQL query string to be executed.

        Returns:
            df: A DataFrame containing the results of the query.
        """

        cursor = self._sql_client.cursor()
        for i, query in enumerate(sql.split(";")):
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
        df = pd.DataFrame(data, columns=column_names)

        return df

    def read_db_obj(self, volume_path: str, sep: Optional[str] = "\t") -> pd.DataFrame:
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

    def read_json_obj(
        self, volume_path: str, return_format: Optional[str] = "dict"
    ) -> dict | list | pd.DataFrame:
        """Read JSON object from Databricks volume

        Reads a JSON file from the Databricks volume and returns it in the
        specified format.

        Args:
            volume_path: The path to the JSON file on the Databricks volume.
            return_format: The format to return the data in:
                          - "dict": Return as dict or list (default)
                          - "dataframe": Convert to pandas DataFrame
                          - "raw": Return as JSON string

        Returns:
            The JSON data in the specified format:
            - dict/list: Python objects parsed from JSON
            - DataFrame: pandas DataFrame (if data is tabular)
            - str: Raw JSON string

        Examples:
            # Read as dict
            data = obj.read_json_obj("/Volumes/catalog/schema/volume/data.json")

            # Read as DataFrame
            df = obj.read_json_obj("/Volumes/catalog/schema/volume/data.json",
                                  return_format="dataframe")

            # Read as raw JSON string
            json_str = obj.read_json_obj("/Volumes/catalog/schema/volume/data.json",
                                        return_format="raw")
        """
        # Download JSON file from volume
        response = self._workspace_client.files.download(volume_path)
        json_bytes = response.contents.read()

        # Return raw JSON string if requested
        if return_format == "raw":
            return json_bytes.decode('utf-8')

        # Parse JSON
        try:
            data = json.loads(json_bytes)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON file at {volume_path}: {e}")

        # Return as dict/list if requested
        if return_format == "dict":
            return data

        # Convert to DataFrame if requested
        elif return_format == "dataframe":
            try:
                if isinstance(data, dict):
                    # Single dict: treat as single row
                    df = pd.DataFrame([data])
                elif isinstance(data, list):
                    # List of dicts: standard DataFrame creation
                    df = pd.DataFrame(data)
                else:
                    raise ValueError(
                        "JSON data must be dict or list of dicts for DataFrame conversion"
                    )
                return df
            except Exception as e:
                raise ValueError(f"Could not convert JSON to DataFrame: {e}")

        else:
            raise ValueError(
                f"return_format must be 'dict', 'dataframe', or 'raw', not '{return_format}'"
            )

    def create_directory_on_volume(self, path: str) -> None:
        """
        Creates a directory on the Databricks volume at the specified path.

        Args:
            path: The path where the directory should be created.

        Returns:
            None
        """
        # Create a directory for file to be uploaded
        print("Creating directory on volume: %s" % path)
        self._workspace_client.files.create_directory(path)

        print("Created")

    def write_db_obj(
        self,
        df: pd.DataFrame,
        volume_path: str,
        sep: Optional[str] = "\t",
        overwrite: Optional[bool] = True,
        dict_database_table_info: Optional[dict] = None,
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

        print("Writing to %s" % volume_path)
        self._workspace_client.files.upload(
            volume_path, csv_buffer, overwrite=overwrite
        )
        print("Write to volume complete")

        if dict_database_table_info is not None:
            if sep != dict_database_table_info.get("sep"):
                dict_database_table_info["sep"] = sep
                print(
                    "Conflict with separator in dict; setting to value object was saved as."
                )

            self.create_table_from_volume(
                dict_database_table_info=dict_database_table_info
            )

        return None

    def write_json_obj(
        self,
        data: dict | list | str,
        volume_path: str,
        save_format: Optional[str] = "json",
        csv_sep: Optional[str] = "\t",
        overwrite: Optional[bool] = True,
        dict_database_table_info: Optional[dict] = None,
    ):
        """Write JSON data to Databricks volume with optional format conversion

        Accepts JSON data in multiple formats and saves it to Databricks volume.
        Can save as JSON file, convert to CSV, or save both formats.

        Args:
            data: JSON data as dict, list of dicts, or JSON string
                  - dict: Single JSON object {"key": "value"}
                  - list: List of JSON objects [{"col1": "val1"}, {"col2": "val2"}]
                  - str: JSON string to be parsed
            volume_path: The path where the file should be saved on the Databricks volume.
                        For save_format="both", this will be used as the base path
            save_format: Output format options:
                        - "json": Save as JSON file (default)
                        - "csv": Convert to CSV and save
                        - "both": Save both JSON and CSV versions
            csv_sep: The separator used when saving as CSV (default: "\t")
            overwrite: Whether to overwrite existing files (default: True)
            dict_database_table_info: A dictionary containing information about the
                                      database table. If provided, a table will be created.
                                      Must contain these keys:
                                        - catalog: Databricks catalog used
                                        - schema: Schema within the catalog
                                        - table: Table name in the schema
                                        - volume_path: Path location on the volume
                                        - sep: File separator used for the object

        Returns:
            None

        Examples:
            # Save dict as JSON
            data = {"name": "John", "age": 30}
            obj.write_json_obj(data, "/Volumes/catalog/schema/volume/data.json")

            # Save list of dicts as CSV
            data = [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]
            obj.write_json_obj(data, "/Volumes/catalog/schema/volume/data.csv",
                              save_format="csv")

            # Save both formats and create table
            obj.write_json_obj(data, "/Volumes/catalog/schema/volume/data",
                              save_format="both",
                              dict_database_table_info={...})
        """
        # Parse input data into a consistent format
        if isinstance(data, str):
            try:
                parsed_data = json.loads(data)
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON string: {e}")
        elif isinstance(data, (dict, list)):
            parsed_data = data
        else:
            raise TypeError(
                f"data must be dict, list, or JSON string, not {type(data).__name__}"
            )

        # Initialize variables to avoid unbound warnings
        df = None
        json_path = None
        csv_path = None

        # Convert to DataFrame for CSV operations
        if save_format in ["csv", "both"] or dict_database_table_info is not None:
            try:
                if isinstance(parsed_data, dict):
                    # Single dict: treat as single row
                    df = pd.DataFrame([parsed_data])
                elif isinstance(parsed_data, list):
                    # List of dicts: standard DataFrame creation
                    df = pd.DataFrame(parsed_data)
                else:
                    raise ValueError("Data must be dict or list of dicts for CSV conversion")
            except Exception as e:
                raise ValueError(f"Could not convert JSON to DataFrame: {e}")

        # Determine file paths based on save_format
        if save_format == "json":
            json_path = volume_path if volume_path.endswith('.json') else f"{volume_path}.json"
        elif save_format == "csv":
            csv_path = volume_path if volume_path.endswith('.csv') else f"{volume_path}.csv"
        elif save_format == "both":
            base_path = volume_path.rsplit('.', 1)[0]  # Remove extension if present
            json_path = f"{base_path}.json"
            csv_path = f"{base_path}.csv"
        else:
            raise ValueError(f"save_format must be 'json', 'csv', or 'both', not '{save_format}'")

        # Save as JSON
        if save_format in ["json", "both"]:
            if json_path is None:
                raise ValueError("Internal error: json_path not initialized")

            print(f"Saving JSON to {json_path}")

            # Create directory on volume
            dir_volume_path = os.path.dirname(json_path)
            self.create_directory_on_volume(path=dir_volume_path)

            # Convert to JSON bytes
            json_bytes = json.dumps(parsed_data, indent=2).encode('utf-8')
            json_buffer = BytesIO(json_bytes)

            # Upload to volume
            print(f"Writing JSON to {json_path}")
            self._workspace_client.files.upload(
                json_path, json_buffer, overwrite=overwrite
            )
            print("JSON write to volume complete")

        # Save as CSV
        if save_format in ["csv", "both"]:
            if csv_path is None or df is None:
                raise ValueError("Internal error: csv_path or df not initialized")

            print(f"Saving CSV to {csv_path}")

            # Create directory on volume
            dir_volume_path = os.path.dirname(csv_path)
            self.create_directory_on_volume(path=dir_volume_path)

            # Convert DataFrame to CSV bytes
            csv_bytes = df.to_csv(index=False, sep=csv_sep).encode('utf-8')
            csv_buffer = BytesIO(csv_bytes)

            # Upload to volume
            print(f"Writing CSV to {csv_path}")
            self._workspace_client.files.upload(
                csv_path, csv_buffer, overwrite=overwrite
            )
            print("CSV write to volume complete")

        # Create table if requested (uses CSV format)
        if dict_database_table_info is not None:
            if save_format == "json":
                raise ValueError(
                    "Cannot create table from JSON format alone. "
                    "Use save_format='csv' or 'both' when creating tables."
                )

            if csv_path is None:
                raise ValueError("Internal error: csv_path not initialized for table creation")

            # Update volume_path in dict to point to CSV file
            if "volume_path" not in dict_database_table_info:
                dict_database_table_info["volume_path"] = csv_path

            # Ensure separator matches
            if csv_sep != dict_database_table_info.get("sep"):
                dict_database_table_info["sep"] = csv_sep
                print("Updating separator in dict to match CSV format")

            self.create_table_from_volume(
                dict_database_table_info=dict_database_table_info
            )

        return None

    def _sql_write_creator(
        self,
        catalog: str,
        schema: str,
        table: str,
        volume_path: str,
        sep: Optional[str] = "\t",
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

    def create_table_from_volume(self, dict_database_table_info: dict) -> None:
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
        catalog = dict_database_table_info.get("catalog")
        schema = dict_database_table_info.get("schema")
        table = dict_database_table_info.get("table")
        volume_path = dict_database_table_info.get("volume_path")
        sep_of_volume_obj = dict_database_table_info.get("sep")
        print("Creating SQL table from volume:")
        print("Catalog: %s" % catalog)
        print("Schema: %s" % schema)
        print("Table: %s" % table)
        print("Volume path: %s" % volume_path)
        print("Separator: %s" % sep_of_volume_obj)

        sql_write = self._sql_write_creator(
            catalog=catalog,
            schema=schema,
            table=table,
            volume_path=volume_path,
            sep=sep_of_volume_obj,
        )

        cursor = self._sql_client.cursor()
        for i, query in enumerate(sql_write.split(";")[:-1]):
            print(query)
            cursor.execute(query)

        print("Table created")

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
        print("Databricks connection closed")

        return None

    def init_spark_session(self) -> Any:
        """
        Initializes a Databricks Spark session using environment configuration.

        This function sets necessary environment variables for Databricks Connect and
        creates a Spark session using DatabricksSession.builder.getOrCreate().

        Args:
            env (dict): Environment variables dictionary containing URL, TOKEN, and DATABRICKS_CLUSTER_ID.

        Returns:
            SparkSession: A Spark session connected to the specified Databricks cluster.
        """
        import os

        os.environ["DATABRICKS_HOST"] = self._URL
        os.environ["DATABRICKS_TOKEN"] = self._TOKEN
        os.environ["DATABRICKS_CLUSTER_ID"] = self._CLUSTER_ID
        return DatabricksSession.builder.getOrCreate()

    def load_csv_from_volume(self, spark: Any, fname_idb: str) -> Any:
        """
        Loads a CSV file from a Databricks volume into a Spark DataFrame.

        Args:
            spark (SparkSession): An active Spark session.
            fname_idb (str): Path to the CSV file in the volume.

        Returns:
            DataFrame: A Spark DataFrame containing the CSV contents.
        """
        return spark.read.format("csv").load(
            fname_idb, sep="\t", header=True, escape='"', multiLine=True
        )

    def load_table(self, spark: Any, table_name: str) -> Any:
        """
        Loads a Delta table into a Spark DataFrame.

        Args:
            spark (SparkSession): An active Spark session.
            table_name (str): Fully qualified name of the Delta table.

        Returns:
            DataFrame: A Spark DataFrame with the table contents.
        """
        return spark.read.format("delta").table(table_name)
