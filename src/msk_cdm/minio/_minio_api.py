from io import BytesIO
import logging
import os
from pathlib import Path
import sys
from typing import Optional, Union
import urllib3

from dotenv import dotenv_values
from minio import Minio
from minio.commonconfig import CopySource
import pandas as pd


logger = logging.getLogger()


class MinioAPI(object):
    """Object to simplify reading/writing to/from Minio."""

    def __init__(
        self,
        *,
        ACCESS_KEY: Optional[str] = None,
        SECRET_KEY: Optional[str] = None,
        ca_certs: Optional[str] = None,
        url_port: Optional[str] = "pllimsksparky3:9000", 
        fname_minio_env: Optional[Union[Path, str]] = None,
        bucket: Optional[str] = None,
    ):
        """Initialization

                Args:
                    - ACCESS_KEY: Minio access key. Optional if `fname_minio_env` is passed, in which case it may be present in the env file picked up by .env
                    - SECRET_KEY: Minio secret key. Optional if `fname_minio_env` is passed, in which case it may be present in the env file picked up by .env
                    - ca_certs: optional filename pointer to ca_cert bundle for `urllib3`. Only specify if not passing `fname_minio_env`.
                    - fname_minio_env: A filename with KEY=value lines with values for keys `CA_CERTS`, `URL_PORT`, `BUCKET`.
        <<<<<<< HEAD

        =======
                    - bucket: optional default minio bucket to use for operations. Can also be specified as environment variable $BUCKET.
        >>>>>>> 3ec82dfbcd3c73bea271fd6a2daedb4520763b9a
        """
        self._ACCESS_KEY = ACCESS_KEY
        self._SECRET_KEY = SECRET_KEY
        self._ca_certs = ca_certs
        self._url_port = url_port

        self._bucket = bucket
        self._client = None

        if fname_minio_env is not None:
            self._process_env(fname_minio_env)
        self._connect()

    def load_obj(
        self, path_object: str, bucket_name: Optional[str] = None
    ) -> urllib3.response.HTTPResponse:
        """Read an object from minio

        Raises `urllib3.exceptions.HTTPError` if request is unsuccessful.

        Args:
            path_object: Object file to read from minio.
            bucket_name: Optional bucket name, otherwise defaults to BUCKET passed
            via minio env fniame to constructor

        Returns:
            urllib3.response.HTTPResponse

        """
        if self._bucket is not None:
            bucket_name = self._bucket
        obj = self._client.get_object(bucket_name, path_object)
        # From here, the object can be read in pandas
        # df = pd.read_csv(obj, sep=sep, low_memory=False)

        return obj

    def save_obj(
        self,
        df,
        path_object: str,
        sep: Optional[str] = ",",
        bucket_name: Optional[str] = None,
    ):
        """Save an object to minio

        Args:
            df: Pandas dataframe to be saved to Minio
            path_object: Object filename for `df`
            sep: Separator when saving the Pandas dataframe
            bucket_name: Optional bucket name, otherwise defaults to BUCKET passed
            via minio env fniame to constructor

        """

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
        
    def load_df(self, 
                fname, 
                sep: Optional[str] = "\t",
                dtype: Optional[str] = object
               ):
      obj = self.load_obj(fname) 
      df= pd.read_csv(obj, dtype=dtype, sep=sep)
      return df

    def save_df(self, 
                df, 
                fname, 
                sep: Optional[str] = "\t"
               ):
      obj = obj_minio.save_obj(df, fname, sep=sep)
      print(f'Saved data to: {fname}')
    
    def print_list_objects(
        self,
        bucket_name: Optional[str] = None,
        prefix: Optional[str] = None,
        recursive: Optional[bool] = True,
    ):
        """Create a Python list of objects in a specified minio bucket

        Args:
            - bucket_name: Optional bucket name, otherwise defaults to  BUCKET passed via minio env fname to constructor
            - prefix: Optional string used to find an object starting with <prefix>

        Returns:
            obj_list: List of strings containing path locations in minio bucket.

        """
        if self._bucket is not None:
            bucket_name = self._bucket

        objs = self._client.list_objects(
            bucket_name=bucket_name, recursive=recursive, prefix=prefix
        )
        obj_list = []
        for obj in objs:
            obj_list.append(obj.object_name)

        return obj_list

    def remove_obj(self, path_object: str, bucket_name: Optional[str] = None):
        """Remove an object from minio

        Args:
            path_object: Object file to be removed from minio
            bucket_name: Optional bucket name, otherwise defaults to  BUCKET passed via minio env fname to constructor

        """
        # Remove list of objects.
        self._client.remove_object(bucket_name=bucket_name, object_name=path_object)
        print("Object removed. Bucket: %s, Object: %s" % (bucket_name, path_object))

        return None

    def copy_obj(
        self,
        source_path_object: str,
        dest_path_object: str,
        source_bucket: Optional[str] = None,
        dest_bucket: Optional[str] = None,
    ):
        """Copy an object in minio.

        Objects can be copied across different BUCKETS.
        Warning: objects with greater than 1GB may fail using this.
        Instead, use `load_obj` and `save_obj` in combination.

        Args:
            source_path_object: Object file to be copied
            dest_path_object: Object filename that `source_path_object` will be copied to
            bucket_name: Optional bucket name, otherwise defaults to  BUCKET passed
            via minio env fniame to constructor

        Returns:
            output: Object name and version ID of object
        """
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

    def _process_env(self, fname_minio_env):
        dict_config = dotenv_values(fname_minio_env)

        env_access_key = os.getenv("ACCESS_KEY")
        if env_access_key:
            dict_config["ACCESS_KEY"] = env_access_key

        env_secret_key = os.getenv("SECRET_KEY")
        if env_secret_key:
            dict_config["SECRET_KEY"] = env_secret_key

        if not self._ACCESS_KEY:
            self._ACCESS_KEY = dict_config.get("ACCESS_KEY", None)
        if not self._SECRET_KEY:
            self._SECRET_KEY = dict_config.get("SECRET_KEY", None)
        if not self._ca_certs:
            self._ca_certs = dict_config.get("CA_CERTS", None)
        if not self._url_port:
            self._url_port = dict_config.get("URL_PORT", None)
        if not self._bucket:
            self._bucket = dict_config.get("BUCKET", None)

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
