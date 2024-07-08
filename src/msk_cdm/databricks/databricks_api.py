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


    def query_from_file(self, sql_path):
        connection = self._client

        print('Loading query')
        # query = "SELECT * FROM mode_clinical_test.dcmspt.patient_demographics_v LIMIT 2"
        fd = open(sql_path, 'r')
        sqlFile = fd.read()
        fd.close()

        print('Querying data')
        cursor = connection.cursor()
        for i,query in enumerate(sqlFile.split(';')):
            print(query[:50])
            cursor.execute(query)

        column_names = [desc[0] for desc in cursor.description]


        data = cursor.fetchall()
        for row in data:
            logging.debug(row)

        cursor.close()
        connection.close()

        df = pd.DataFrame(data, columns=column_names)

        return df