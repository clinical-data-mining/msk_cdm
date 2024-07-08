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
    def __init__(
            self,
            token,
            hostname,
            http_path
    ):

        self._client = None
        self._connect(
            token=token,
            hostname=hostname,
            http_path=http_path
        )

    def _connect(self, token, hostname, http_path):
        print('Making databricks connection')
        connection = sql.connect(
            server_hostname=hostname,
            http_path=http_path,
            access_token=token
        )
        print('Connected.')

        self._client = connection

        return None


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