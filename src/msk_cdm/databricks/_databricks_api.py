import os, logging
from databricks import sql
import pandas as pd
import certifi
import pathlib
from pathlib import Path
from dotenv import dotenv_values

from typing import Optional, Union
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
    """Object to simplify reading/writing to/from Minio."""

    def __init__(
        self,
        *,
        TOKEN: Optional[str] = None,
        URL: Optional[str] = None,
        HTTP_PATH: Optional[str] = None,
        HOSTNAME: Optional[str] = None,
        fname_databricks_env: Optional[Union[Path, str]] = None
    ):
        """Initialization to connect with Databricks

                Args:
                    - TOKEN: Databricks user token. Optional if `fname_databricks_env` is passed, in which case it may be present in the env file picked up by .env
                    - HOSTNAME: Databricks hostname. Optional if `fname_databricks_env` is passed, in which case it may be present in the env file picked up by .env
                    - URL: optional filename pointer to ca_cert bundle for `urllib3`. Only specify if not passing `fname_databricks_env`.
                    - HTTP_PATH:
                    - fname_databricks_env: A filename with KEY=value lines with values for keys `CA_CERTS`, `URL_PORT`, `BUCKET`.

        """
        # self._TOKEN = TOKEN
        # self._HOSTNAME = HOSTNAME
        # self._URL = URL
        # self._HTTP_PATH = HTTP_PATH
        self._client = None
        print(HOSTNAME)
        client = sql.connect(
            server_hostname=HOSTNAME,
            http_path=HTTP_PATH,
            token=TOKEN
        )
        print("Connected successfully.")
        self._client = client

        # if fname_databricks_env is not None:
        #     self._process_env(fname_databricks_env)
        # self._connect_sql()

        return None

    # def _process_env(
    #         self,
    #         fname_databricks_env
    # ):
    #
    #     dict_config = dotenv_values(fname_databricks_env)
    #
    #     if not self._TOKEN:
    #         self._TOKEN = dict_config.get("TOKEN", None)
    #     if not self._HOSTNAME:
    #         self._HOSTNAME = dict_config.get("HOSTNAME", None)
    #     if not self._URL:
    #         self._URL = dict_config.get("URL", None)
    #     if not self._HTTP_PATH:
    #         self._HTTP_PATH = dict_config.get("HTTP_PATH", None)

    def connect_sql(
            self,
            hostname,
            http_path,
            token
    ):
        # hostname = self._HOSTNAME
        # url = self._URL
        # http_path = self._HTTP_PATH
        # token = self._TOKEN
        print(hostname)
        client = sql.connect(
            server_hostname=hostname,
            http_path=http_path,
            token=token
        )
        print("Connected successfully.")
        self._client = client

    def query_from_file(
            self,
            *,
            fname_sql
    ):
        """Query Databricks from a file containing Spark SQL

        Args:
            fname_sql: The file name of the SQL

        Returns:
            df: Pandas dataframe containing the results of the query

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
        """Query Databricks from a SQL string

        Args:
            sql: A Spark SQL statement

        Returns:
            df: Pandas dataframe containing the results of the query

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


