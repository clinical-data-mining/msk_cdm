#!/usr/bin/env python

"""Example script demonstrating JSON read/write functionality for Databricks volumes.

This script shows how to use the new write_json_obj() and read_json_obj() methods
to work with JSON data in Databricks volumes.

Requires a Databricks environment file with connection credentials.
"""

import argparse
from msk_cdm.databricks import DatabricksAPI


def example_write_json(env_file, volume_path):
    """Demonstrate writing JSON data to Databricks volume"""

    # Initialize Databricks API
    db_api = DatabricksAPI(fname_databricks_env=env_file)

    # Example 1: Write a single dict as JSON
    print("\n=== Example 1: Write single dict as JSON ===")
    data_dict = {
        "patient_id": "P-0000001",
        "age": 45,
        "diagnosis": "Stage II",
        "treatment_date": "2024-01-15"
    }

    json_path = f"{volume_path}/patient_data.json"
    db_api.write_json_obj(
        data=data_dict,
        volume_path=json_path,
        save_format="json"
    )
    print(f"Successfully wrote single dict to {json_path}")


    # Example 2: Write list of dicts and convert to CSV
    print("\n=== Example 2: Write list of dicts as CSV ===")
    data_list = [
        {"patient_id": "P-0000001", "visit_date": "2024-01-15", "blood_pressure": "120/80"},
        {"patient_id": "P-0000001", "visit_date": "2024-02-15", "blood_pressure": "118/78"},
        {"patient_id": "P-0000002", "visit_date": "2024-01-20", "blood_pressure": "130/85"},
    ]

    csv_path = f"{volume_path}/visits.csv"
    db_api.write_json_obj(
        data=data_list,
        volume_path=csv_path,
        save_format="csv",
        csv_sep="\t"
    )
    print(f"Successfully converted JSON to CSV at {csv_path}")


    # Example 3: Write both JSON and CSV formats
    print("\n=== Example 3: Write both JSON and CSV formats ===")
    data_cohort = [
        {"cohort_id": "LUNG_001", "patient_count": 245, "median_age": 62},
        {"cohort_id": "BREAST_001", "patient_count": 318, "median_age": 54},
        {"cohort_id": "CRC_001", "patient_count": 156, "median_age": 58},
    ]

    both_path = f"{volume_path}/cohort_summary"
    db_api.write_json_obj(
        data=data_cohort,
        volume_path=both_path,
        save_format="both"
    )
    print(f"Successfully wrote both formats: {both_path}.json and {both_path}.csv")


    # Example 4: Write JSON and create Databricks table
    print("\n=== Example 4: Write CSV and create Databricks table ===")
    data_metrics = [
        {"metric_name": "overall_survival", "cohort": "LUNG_001", "value": 18.5, "unit": "months"},
        {"metric_name": "progression_free_survival", "cohort": "LUNG_001", "value": 12.3, "unit": "months"},
        {"metric_name": "response_rate", "cohort": "LUNG_001", "value": 45.2, "unit": "percent"},
    ]

    table_path = f"{volume_path}/clinical_metrics.csv"
    table_info = {
        "catalog": "main",
        "schema": "clinical",
        "table": "metrics_example",
        "volume_path": table_path,
        "sep": "\t"
    }

    db_api.write_json_obj(
        data=data_metrics,
        volume_path=table_path,
        save_format="csv",
        dict_database_table_info=table_info
    )
    print(f"Successfully created table: main.clinical.metrics_example")


    # Example 5: Write JSON string
    print("\n=== Example 5: Write from JSON string ===")
    json_string = '{"study_id": "MSK-001", "status": "active", "enrollment": 150}'

    string_path = f"{volume_path}/study_info.json"
    db_api.write_json_obj(
        data=json_string,
        volume_path=string_path,
        save_format="json"
    )
    print(f"Successfully wrote JSON string to {string_path}")

    db_api.close_connection()


def example_read_json(env_file, volume_path):
    """Demonstrate reading JSON data from Databricks volume"""

    # Initialize Databricks API
    db_api = DatabricksAPI(fname_databricks_env=env_file)

    # Example 1: Read JSON as dict
    print("\n=== Example 1: Read JSON as dict ===")
    json_path = f"{volume_path}/patient_data.json"
    data = db_api.read_json_obj(
        volume_path=json_path,
        return_format="dict"
    )
    print(f"Read data: {data}")
    print(f"Type: {type(data)}")


    # Example 2: Read JSON as DataFrame
    print("\n=== Example 2: Read JSON as DataFrame ===")
    json_path = f"{volume_path}/cohort_summary.json"
    df = db_api.read_json_obj(
        volume_path=json_path,
        return_format="dataframe"
    )
    print(f"DataFrame shape: {df.shape}")
    print(df)


    # Example 3: Read JSON as raw string
    print("\n=== Example 3: Read JSON as raw string ===")
    json_path = f"{volume_path}/study_info.json"
    json_str = db_api.read_json_obj(
        volume_path=json_path,
        return_format="raw"
    )
    print(f"Raw JSON: {json_str}")
    print(f"Type: {type(json_str)}")

    db_api.close_connection()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Demo script for JSON read/write operations with Databricks volumes"
    )
    parser.add_argument(
        "--env_file",
        action="store",
        dest="env_file",
        required=True,
        help="Path to Databricks environment file with connection credentials"
    )
    parser.add_argument(
        "--volume_path",
        action="store",
        dest="volume_path",
        required=True,
        help="Base path on Databricks volume (e.g., /Volumes/main/default/my_volume/examples)"
    )
    parser.add_argument(
        "--mode",
        action="store",
        dest="mode",
        choices=["write", "read", "both"],
        default="both",
        help="Operation mode: write, read, or both"
    )

    args = parser.parse_args()

    if args.mode in ["write", "both"]:
        example_write_json(env_file=args.env_file, volume_path=args.volume_path)

    if args.mode in ["read", "both"]:
        example_read_json(env_file=args.env_file, volume_path=args.volume_path)

    print("\n=== All examples completed successfully! ===")
