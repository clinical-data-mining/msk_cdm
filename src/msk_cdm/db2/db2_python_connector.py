"""
db2_python_connector.py

This object leverages the ibm_db_dbi module to connect to the MSK Darwin database and perform SQL queries,
as well as save the results to Minio object storage.
"""
import pandas as pd
import ibm_db_dbi as db
from msk_cdm.minio import MinioAPI

class db2connection(object):
    """
    A class used to establish a connection to the MSK Darwin database using IBM DB2
    and perform various query operations.

    Attributes
    ----------
    _conn : object
        Database connection object.
    _database : str
        Name of the database.
    _host : str
        Database host URL.
    _port : str
        Port for database connection.
    _protocol : str
        Protocol used for the database connection.
    _uid : str
        User ID for database authentication.

    Methods
    -------
    __init__(database: str, host: str, port: str, protocol: str, uid: str, pwd: str) -> None
        Initializes the database connection.

    _connection_string(database: str, host: str, port: str, protocol: str, uid: str, pwd: str) -> str
        Constructs the connection string for IBM DB2.

    _connect(pwd: str) -> None
        Establishes the connection to the database using the connection string.

    query_ddp(fname_sql: str) -> pd.DataFrame
        Executes a query from a SQL file and returns the result as a DataFrame.

    query_ddp_sql(sql: str) -> pd.DataFrame
        Executes a raw SQL query and returns the result as a DataFrame.

    query_ddp_and_save(fname_sql: str, fname_minio_config: str, fname_output: str, fname_backup: str = None) -> pd.DataFrame
        Executes a query from a SQL file, saves the result to Minio, and optionally creates a backup.

    _backup_copy(obj_minio: MinioAPI, minio_bucket: str, fname_output: str, fname_backup: str) -> str
        Copies an existing file in Minio to a backup location.
    """

    def __init__(
            self,
            database: str,
            host: str,
            port: str,
            protocol: str,
            uid: str,
            pwd: str
    ) -> None:
        """
        Initializes the db2connection object by setting up the connection parameters
        and establishing a connection to the MSK Darwin database.

        Parameters
        ----------
        database : str
            Name of the database.
        host : str
            Database host URL.
        port : str
            Port for database connection.
        protocol : str
            Protocol used for the connection (e.g., TCPIP).
        uid : str
            User ID for authentication.
        pwd : str
            Password for authentication.
        """
        self._conn = None
        self._database = database
        self._host = host
        self._port = port
        self._protocol = protocol
        self._uid = uid

        # Create connection
        self._connect(pwd=pwd)

    def _connection_string(
            self,
            database: str,
            host: str,
            port: str,
            protocol: str,
            uid: str,
            pwd: str
    ) -> str:
        """
        Constructs a connection string from the given parameters for IBM DB2.

        Parameters
        ----------
        database : str
            Name of the database.
        host : str
            Database host URL.
        port : str
            Port for the connection.
        protocol : str
            Protocol for the connection (e.g., TCPIP).
        uid : str
            User ID for authentication.
        pwd : str
            Password for authentication.

        Returns
        -------
        str
            The connection string required for IBM DB2.
        """
        conn_str = f'DATABASE={database};HOSTNAME={host};PORT={port};PROTOCOL={protocol};UID={uid};PWD={pwd};'
        return conn_str

    def _connect(
            self,
            pwd: str
    ) -> None:
        """
        Establishes a connection to the database using the connection string.

        Parameters
        ----------
        pwd : str
            Password for authentication.
        """
        conn_str = self._connection_string(
            database=self._database,
            host=self._host,
            port=self._port,
            protocol=self._protocol,
            uid=self._uid, pwd=pwd
        )

        # Establish connection
        conn = db.connect(conn_str, '', '')
        self._conn = conn

    def query_ddp(
            self,
            fname_sql: str
    ) -> pd.DataFrame:
        """
        Executes a SQL query from a file and returns the result as a DataFrame.

        Parameters
        ----------
        fname_sql : str
            Path to the SQL file containing the query.

        Returns
        -------
        pd.DataFrame
            DataFrame containing the query results.
        """
        with open(fname_sql, 'r') as fd:
            sqlFile = fd.read()

        # Query data
        df = self.query_ddp_sql(sql=sqlFile)
        return df

    def query_ddp_sql(
            self,
            sql: str
    ) -> pd.DataFrame:
        """
        Executes a raw SQL query and returns the result as a DataFrame.

        Parameters
        ----------
        sql : str
            The SQL query string.

        Returns
        -------
        pd.DataFrame
            DataFrame containing the query results.
        """
        df = pd.read_sql(sql, self._conn)
        return df

    def query_ddp_and_save(
            self,
            fname_sql: str,
            fname_minio_config: str,
            fname_output: str,
            fname_backup: str = None
    ) -> pd.DataFrame:
        """
        Executes a SQL query from a file, saves the result to Minio, and optionally creates a backup.

        Parameters
        ----------
        fname_sql : str
            Path to the SQL file containing the query.
        fname_minio_config : str
            Path to the Minio configuration file.
        fname_output : str
            Path to save the output file in Minio.
        fname_backup : str, optional
            Path to save the backup of the output file (default is None).

        Returns
        -------
        pd.DataFrame
            DataFrame containing the query results.
        """
        # Init Minio
        obj_minio = MinioAPI(fname_minio_env=fname_minio_config)

        # Query data
        df = self.query_ddp(fname_sql)

        # # Copy old file to backup
        if fname_backup is not None:
            self._backup_copy(
                obj_minio=obj_minio,
                minio_bucket=obj_minio.bucket_name,
                fname_output=fname_output,
                fname_backup=fname_backup
            )

        # Save dataframe
        if fname_output is not None:
            obj_minio.save_obj(
                df=df,
                path_object=fname_output,
                sep='\t'
            )

        return df

    def _backup_copy(
            self,
            obj_minio: MinioAPI,
            minio_bucket: str,
            fname_output: str,
            fname_backup: str
    ) -> str:
        """
        Copies an existing file from Minio to a backup location.

        Parameters
        ----------
        obj_minio : MinioAPI
            Minio API object for interacting with the Minio server.
        minio_bucket : str
            Name of the Minio bucket.
        fname_output : str
            Path to the output file to be backed up.
        fname_backup : str
            Path to the backup file in Minio.

        Returns
        -------
        str
            The result of the copy operation.
        """
        # Check if file exists in Minio
        list_ = obj_minio.print_list_objects(bucket_name=minio_bucket, recursive=True, prefix=fname_output)

        if any(ext in fname_output for ext in list_):
            # Copy object to backup location
            result = obj_minio.copy_obj(
                source_bucket=minio_bucket,
                source_path_object=fname_output,
                dest_bucket=minio_bucket,
                dest_path_object=fname_backup
            )

        return result
