from io import BytesIO
import os
import sys
import urllib3

from dotenv import load_dotenv, find_dotenv, dotenv_values
from minio import Minio
from minio.commonconfig import CopySource


def _read_minio_api_config(fname_env):
    """Requires a .env file be populated with"""
    config = dotenv_values(fname_env)
    dict_config = dict(config)

    load_dotenv(dict_config["MINIO_ENV"])

    ACCESS_KEY = os.getenv("ACCESS_KEY")
    SECRET_KEY = os.getenv("SECRET_KEY")

    if not ACCESS_KEY or not SECRET_KEY:
        raise RuntimeError(
            "Can't find ACCESS_KEY or SECRET_KEY environment variables. Perhaps you're "
            "missing a .env file with them?"
        )

    # Add Minio access and secret key to the configure json
    dict_config["ACCESS_KEY"] = ACCESS_KEY
    dict_config["SECRET_KEY"] = SECRET_KEY

    return dict_config


class MinioAPI(object):
    """ "
    Interface to read/write to Minio
    """

    def __init__(
        self,
        *,
        ACCESS_KEY=None,
        SECRET_KEY=None,
        ca_certs=None,
        url_port="tllihpcmind6:9000",
        fname_minio_env=None
    ):
        self._ACCESS_KEY = ACCESS_KEY
        self._SECRET_KEY = SECRET_KEY
        self._ca_certs = ca_certs
        self._url_port = url_port
        self._fname_minio_env = fname_minio_env

        self._bucket = None
        self._client = None

        if self._fname_minio_env is not None:
            self._process_env()

        self._connect()

    def _process_env(self):
        # Setup Minio configuration
        minio_config = _read_minio_api_config(fname_env=self._fname_minio_env)
        self._ACCESS_KEY = minio_config["ACCESS_KEY"]
        self._SECRET_KEY = minio_config["SECRET_KEY"]
        self._ca_certs = minio_config["CA_CERTS"]
        self._url_port = minio_config["URL_PORT"]
        self._bucket = minio_config["BUCKET"]

        return None

    def _connect(self):
        # required for self-signed certs
        httpClient = urllib3.PoolManager(
            cert_reqs="CERT_REQUIRED", ca_certs=self._ca_certs
        )

        # Create secure client with access key and secret key
        client = Minio(
            endpoint=self._url_port,
            access_key=self._ACCESS_KEY,
            secret_key=self._SECRET_KEY,
            secure=True,
            http_client=httpClient,
        )

        self._client = client

    def print_list_objects(self, bucket_name=None, prefix=None, recursive=True):
        if self._bucket is not None:
            bucket_name = self._bucket

        objs = self._client.list_objects(
            bucket_name=bucket_name, recursive=recursive, prefix=prefix
        )
        obj_list = []
        for obj in objs:
            obj_list.append(obj.object_name)

        return obj_list

    def load_obj(self, path_object, bucket_name=None):
        """Read an object from minio.
        Raises urllib3.exceptions.HTTPError if request is unsuccessful.

        Returns:
            - urllib3.response.HTTPResponse
        """
        if self._bucket is not None:
            bucket_name = self._bucket
        obj = self._client.get_object(bucket_name, path_object)
        # From here, the object can be read in pandas
        # df = pd.read_csv(obj, sep=sep, low_memory=False)

        return obj

    def save_obj(self, df, path_object, sep=",", bucket_name=None):
        if self._bucket is not None:
            bucket_name = self._bucket

        csv_bytes = df.to_csv(index=False, sep=sep).encode("utf-8")
        csv_buffer = BytesIO(csv_bytes)

        self._client.put_object(
            bucket_name=bucket_name,
            object_name=path_object,
            data=csv_buffer,
            length=len(csv_bytes),
            content_type="application/csv",
        )

        return None

    def remove_obj(self, path_object, bucket_name=None):
        # Remove list of objects.
        self._client.remove_object(bucket_name=bucket_name, object_name=path_object)
        print("Object removed. Bucket: %s, Object: %s" % (bucket_name, path_object))

        return None

    def copy_obj(
        self, source_path_object, dest_path_object, source_bucket=None, dest_bucket=None
    ):
        if self._bucket is not None:
            source_bucket = self._bucket
            dest_bucket = self._bucket

        result = self._client.copy_object(
            dest_bucket,
            dest_path_object,
            CopySource(source_bucket, source_path_object),
        )

        output = [result.object_name, result.version_id]

        return output
