# Databricks JSON Support Feature

## Overview

This feature adds native JSON support to the `DatabricksAPI` class, enabling seamless reading and writing of JSON data to Databricks volumes. The implementation includes two new methods that complement the existing `read_db_obj()` and `write_db_obj()` functions.

## New Methods

### 1. `write_json_obj()`

Writes JSON data to Databricks volumes with flexible format options.

**Signature:**
```python
def write_json_obj(
    self,
    data: dict | list | str,
    volume_path: str,
    save_format: Optional[str] = "json",
    csv_sep: Optional[str] = "\t",
    overwrite: Optional[bool] = True,
    dict_database_table_info: Optional[dict] = None,
)
```

**Parameters:**
- `data`: JSON data as dict, list of dicts, or JSON string
- `volume_path`: Path where file should be saved on Databricks volume
- `save_format`: Output format - `"json"`, `"csv"`, or `"both"` (default: `"json"`)
- `csv_sep`: Separator for CSV format (default: `"\t"`)
- `overwrite`: Whether to overwrite existing files (default: `True`)
- `dict_database_table_info`: Optional dictionary for creating a Databricks table

**Key Features:**
- Accepts multiple input formats (dict, list, JSON string)
- Saves as JSON, CSV, or both formats simultaneously
- Automatic table creation from CSV data
- Smart file extension handling

**Examples:**

```python
from msk_cdm.databricks import DatabricksAPI

# Initialize API
db_api = DatabricksAPI(fname_databricks_env='path/to/env.txt')

# Example 1: Save dict as JSON
data = {"patient_id": "P-001", "age": 45, "diagnosis": "Stage II"}
db_api.write_json_obj(
    data=data,
    volume_path="/Volumes/main/schema/volume/patient.json"
)

# Example 2: Convert JSON to CSV
data = [
    {"id": "P-001", "age": 45},
    {"id": "P-002", "age": 52}
]
db_api.write_json_obj(
    data=data,
    volume_path="/Volumes/main/schema/volume/patients.csv",
    save_format="csv"
)

# Example 3: Save both formats
db_api.write_json_obj(
    data=data,
    volume_path="/Volumes/main/schema/volume/patients",
    save_format="both"
)
# Creates: patients.json and patients.csv

# Example 4: Create Databricks table
table_info = {
    "catalog": "main",
    "schema": "clinical",
    "table": "patients",
    "volume_path": "/Volumes/main/schema/volume/patients.csv",
    "sep": "\t"
}
db_api.write_json_obj(
    data=data,
    volume_path="/Volumes/main/schema/volume/patients.csv",
    save_format="csv",
    dict_database_table_info=table_info
)
```

### 2. `read_json_obj()`

Reads JSON data from Databricks volumes with flexible output formats.

**Signature:**
```python
def read_json_obj(
    self,
    volume_path: str,
    return_format: Optional[str] = "dict"
) -> dict | list | pd.DataFrame
```

**Parameters:**
- `volume_path`: Path to the JSON file on Databricks volume
- `return_format`: Return format - `"dict"`, `"dataframe"`, or `"raw"` (default: `"dict"`)

**Returns:**
- `"dict"`: Python dict or list objects
- `"dataframe"`: pandas DataFrame (for tabular JSON)
- `"raw"`: Raw JSON string

**Examples:**

```python
# Example 1: Read as dict
data = db_api.read_json_obj(
    volume_path="/Volumes/main/schema/volume/config.json"
)
# Returns: {"key": "value", ...}

# Example 2: Read as DataFrame
df = db_api.read_json_obj(
    volume_path="/Volumes/main/schema/volume/patients.json",
    return_format="dataframe"
)
# Returns: pandas DataFrame

# Example 3: Read as raw string
json_str = db_api.read_json_obj(
    volume_path="/Volumes/main/schema/volume/data.json",
    return_format="raw"
)
# Returns: '{"key": "value", ...}'
```

## Use Cases

### 1. API Response Storage
Store API responses as JSON for later processing:
```python
import requests

# Fetch data from API
response = requests.get("https://api.example.com/data")
data = response.json()

# Store in Databricks
db_api.write_json_obj(
    data=data,
    volume_path="/Volumes/main/raw/api_responses/response_20240115.json"
)
```

### 2. Configuration Management
Store and retrieve configuration files:
```python
# Save config
config = {
    "model_params": {"learning_rate": 0.01, "epochs": 100},
    "data_params": {"batch_size": 32, "validation_split": 0.2}
}
db_api.write_json_obj(
    data=config,
    volume_path="/Volumes/main/configs/model_config.json"
)

# Load config
config = db_api.read_json_obj(
    volume_path="/Volumes/main/configs/model_config.json"
)
```

### 3. Data Format Conversion
Convert JSON from external sources to tables:
```python
# JSON from external source
clinical_data = [
    {"patient_id": "P-001", "metric": "OS", "value": 18.5},
    {"patient_id": "P-002", "metric": "PFS", "value": 12.3}
]

# Save as both formats and create table
table_info = {
    "catalog": "main",
    "schema": "clinical",
    "table": "metrics",
    "volume_path": "/Volumes/main/clinical/metrics.csv",
    "sep": "\t"
}

db_api.write_json_obj(
    data=clinical_data,
    volume_path="/Volumes/main/clinical/metrics",
    save_format="both",
    dict_database_table_info=table_info
)
```

### 4. Metadata Storage
Store dataset metadata alongside data files:
```python
metadata = {
    "dataset_name": "clinical_cohort_2024",
    "created_date": "2024-01-15",
    "record_count": 1245,
    "columns": ["patient_id", "age", "diagnosis"],
    "source": "Epic EHR"
}

db_api.write_json_obj(
    data=metadata,
    volume_path="/Volumes/main/metadata/cohort_metadata.json"
)
```

## Design Decisions

### Why a Separate Function?
- **Clean separation**: JSON and CSV have different use cases
- **Type safety**: Clear contract for JSON operations
- **Backward compatibility**: No risk of breaking existing code
- **Optimization**: Can add JSON-specific features (schema validation, etc.)

### Format Options
The `save_format` parameter supports three modes:
1. **"json"**: Native JSON storage - best for nested/complex data
2. **"csv"**: Convert to tabular format - best for table creation
3. **"both"**: Save both formats - best for flexibility

### Type Handling
- Single dict → Single-row DataFrame
- List of dicts → Multi-row DataFrame
- JSON string → Parsed and processed

## Error Handling

The functions include comprehensive error handling:

```python
# Invalid JSON string
try:
    db_api.write_json_obj(
        data="{invalid json}",
        volume_path="/path/to/file.json"
    )
except ValueError as e:
    print(f"Invalid JSON: {e}")

# Incompatible operations
try:
    db_api.write_json_obj(
        data=data,
        save_format="json",  # JSON only
        dict_database_table_info=table_info  # Requires CSV!
    )
except ValueError as e:
    print(f"Error: {e}")
    # Error: Cannot create table from JSON format alone
```

## Performance Considerations

- JSON files are stored with `indent=2` for readability
- CSV conversion uses pandas for efficiency
- Directory creation is automatic and idempotent
- Files are buffered in memory before upload

## Future Enhancements

Potential future additions:
- JSON schema validation
- Streaming support for large files
- Compression options (gzip)
- Direct JSON table creation (Databricks native JSON tables)
- Batch operations for multiple files

## Testing

Run the example script to test the functionality:

```bash
python examples/databricks_json_example.py \
    --env_file /path/to/databricks_env.txt \
    --volume_path /Volumes/main/default/my_volume/test \
    --mode both
```

## Related Functions

- `write_db_obj()`: Write pandas DataFrame to CSV
- `read_db_obj()`: Read CSV to pandas DataFrame
- `create_table_from_volume()`: Create Databricks table from file

## Migration Guide

### From write_db_obj to write_json_obj

**Before:**
```python
# Manual conversion required
df = pd.DataFrame(json_data)
db_api.write_db_obj(df, volume_path)
```

**After:**
```python
# Direct JSON support
db_api.write_json_obj(json_data, volume_path, save_format="csv")
```

## Branch Information

This feature is implemented in branch: `feature/databricks-json-support`

To use this feature:
```bash
git checkout feature/databricks-json-support
```
