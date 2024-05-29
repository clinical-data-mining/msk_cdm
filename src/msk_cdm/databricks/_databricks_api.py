import logging
from pathlib import Path
from typing import Optional, Union

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
                    - TOKEN: Minio access key. Optional if `fname_databricks_env` is passed, in which case it may be present in the env file picked up by .env
                    - HOSTNAME: Minio secret key. Optional if `fname_databricks_env` is passed, in which case it may be present in the env file picked up by .env
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
        client = sql.connect(
            server_hostname=self._HOSTNAME,
            http_path=self._HTTP_PATH,
            access_token=self._TOKEN
        )

        self._client = client

    def create_workspace_client(
            self,
    ):
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
        # open SQL file
        fd = open(fname_sql, 'r')
        sqlFile = fd.read()
        fd.close()

        cursor = self._client.cursor()
        for i,query in enumerate(sqlFile.split(';')):
            print(query[:50])
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


