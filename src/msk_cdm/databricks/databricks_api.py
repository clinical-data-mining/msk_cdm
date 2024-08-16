import os, logging
from databricks import sql
import pandas as pd
import certifi
import pathlib
from dotenv import dotenv_values

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
    """
    A class to interact with Databricks through its SQL API. This class allows
    connecting to a Databricks cluster, executing queries, and retrieving
    the results as pandas DataFrames.
    """
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
        self._client = None
        self._URL = None

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
        print('Connected.')

        self._client = connection

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

        cursor = self._client.cursor()
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

    def close_connection(self):
        """
        Closes the connection to the Databricks cluster.

        Returns:
        --------
        None
        """
        cursor = self._client.cursor()
        cursor.close()
        self._client.close()
        print('Databricks connection closed')

        return None


