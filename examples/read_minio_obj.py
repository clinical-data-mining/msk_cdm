#!/usr/bin/env python

""" Example script that reads an object from minio via the minio API.

Requires you to have a .env file in your home directory with SECRET_KEY and ACCESS_KEY
for minio.
"""

import argparse
from io import BytesIO

import pandas as pd
import urllib3

from msk_cdm.minio import MinioAPI


def read_minio_obj(minio_env_fname, input_obj):
    minio_api = MinioAPI(fname_minio_env=minio_env_fname)

    try:
        # urllib3.response.HTTPResponse
        response = minio_api.load_obj(input_obj)
    except urllib3.exceptions.HTTPError as e:
        raise RuntimeError(f"Request failed:, {e.reason}")

    if not response.status == 200:
        raise RuntimeError(f"Got response code {response.status}")

    # type "bytes"
    txt = response.read()
    print(f"Read {len(txt)}-byte object from Minio.")

    # Parse as a TSV. Obviously depending on the object you load, it might not be a TSV.
    df = pd.read_csv(BytesIO(txt), sep="\t")
    print(df)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Demo script to read a file from Minio via the CDM API"
    )
    parser.add_argument(
        "--minio_env_fname",
        action="store",
        dest="minio_env_fname",
        default="/mind_data/cdm_repos/cdm-utilities/minio_env.txt",
        help="file with env vars pointing to minio certs",
    )
    parser.add_argument(
        "--input_obj",
        action="store",
        dest="input_obj",
        default=(
            "labels/progression/genie_lung_crc_breast_prostate_pancreas_progression_"
            "labels_20230609.tsv"
        ),
        help="Input file to read from Minio",
    )

    args = parser.parse_args()

    read_minio_obj(minio_env_fname=args.minio_env_fname, input_obj=args.input_obj)
