import logging
from pathlib import Path
from typing import Optional, Union

import signal
from contextlib import contextmanager

from dotenv import dotenv_values
import pandas as pd
from databricks import sql
from databricks.sdk import WorkspaceClient


logger = logging.getLogger()


class DatabricksAPI(object):
    """Object to simplify reading/writing to/from Minio."""

    def __init__(
        self,
        *,
        TOKEN: Optional[str] = None,
        URL: Optional[str] = None,
        HTTP_PATH: Optional[str] = None,
        HOSTNAME: Optional[str] = "msk-mode-test.cloud.databricks.com",
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
        self._TOKEN = TOKEN
        self._HOSTNAME = HOSTNAME
        self._URL = URL
        self._HTTP_PATH = HTTP_PATH

        if fname_databricks_env is not None:
            self._process_env(fname_databricks_env)
        self._connect_sql()

    def _process_env(
            self,
            fname_databricks_env
    ):

        dict_config = dotenv_values(fname_databricks_env)

        if not self._TOKEN:
            self._TOKEN = dict_config.get("TOKEN", None)
        if not self._HOSTNAME:
            self._HOSTNAME = dict_config.get("HOSTNAME", None)
        if not self._URL:
            self._URL = dict_config.get("URL", None)
        if not self._HTTP_PATH:
            self._HTTP_PATH = dict_config.get("HTTP_PATH", None)

    def _connect_sql(self):
        try:
            with timeout(10):  # Timeout in 10 seconds
                client = sql.connect(
                    server_hostname=self._HOSTNAME,
                    http_path=self._HTTP_PATH,
                    access_token=self._TOKEN
                )
                print("Connected successfully.")
                self._client = client
        # except:
        #     TimeoutException:
        #         print('Failed to connect: Connection timed out')
        except Exception as e:
            print('Client connection failed:', str(e))

    def _connect_sql(self):
        try:
            client = sql.connect(
                server_hostname=self._HOSTNAME,
                http_path=self._HTTP_PATH,
                access_token=self._TOKEN
            )
            print("Connected successfully.")
        except Exception as e:

            print('Client connection failed:', str(e))
            logger.error('Connection failed with exception: %s', str(e))
            raise e
            # Re-raise the exception for further handling if necessary self._client = client
    def _connect_sql(self):
        try:
            client = sql.connect(
                server_hostname=self._HOSTNAME,
                http_path=self._HTTP_PATH,
                access_token=self._TOKEN
            )
            print("Connected successfully.")
        except Exception as e:
            print('Client connection failed:', str(e))
            logger.error('Connection failed with exception: %s', str(e))
            raise e  # Re-raise the exception for further handling if necessary

        self._client = client

    def create_workspace_client(self):
        """Create a workspace client to explore the databricks dbfs and clusters

        Returns:
            w: A Databricks workspace client object

        """
        w = WorkspaceClient(
            host=self._URL,
            token=self._TOKEN
        )
        # Example use cases:
        ## Print all available clusters
        # for c in w.clusters.list():
        #     print(c.cluster_name)
        ## Print accessible paths in dbfs:/
        # d = w.dbutils.fs.ls('/')
        # for f in d:
        #     print(f.path)

        return w

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




    # Define a timeout exception
class TimeoutException(Exception):
    pass

        # Timeout handler
def raise_timeout(signum, frame):
    raise TimeoutException

# Context manager to handle the timeout
@contextmanager
def timeout(time):
    # Register a signal handler
    signal.signal(signal.SIGALRM, raise_timeout)
    signal.alarm(time)  # Set the alarm
    try:
        yield
    except TimeoutException:
        print('Connection attempt timed out!')
    finally:
        signal.alarm(0)  # Disable the alarm

# def _connect_sql(self):
#     try:
#         with timeout(10):  # Timeout in 10 seconds
#             client = sql.connect(
#                 server_hostname=self._HOSTNAME,
#                 http_path=self._HTTP_PATH,
#                 access,
#                 token=self._TOKEN
#             )
#             print("Connected successfully.")
#         self._client = client
#     except TimeoutException:
#         print('Failed to connect: Connection timed out')
#     except Exception as e:
#         print('Client connection failed:', str(e))


