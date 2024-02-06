# Redcap to cBioPortal ETL
---
---

Step-by-step break down of setting up a Redcap study for data to be exposed on cBioPortal, pulling data from Redcap, and creating configuration files for transforming data into a cBioPortal data format

There are three (3) configuration files that can be used for exporting data from Redcap and transforming the data into the cBioPortal format:
- API mapping file (Required)
- Key variable map file (Required)
- Data transformation file (Optional)

 
## Setting up Redcap for the ETL
---
### Required from Redcap before starting
- A Redcap API token for the study
- At least one (1) Redcap report
- These variables in the study codebook:
    - DOB column
    - record id column
    - de-identified ID column
    - IMPACT sample id column
    
### Requirements for a Redcap report
Data on cBioPortal **cannot contain PHI** such as dates, accession numbers, or identifiable patient IDs. 

Therefore, the following is needed for each Redcap reports:
- The date of birth column, or another reference date. This is **only** used when the report contains a date attribute that needs to be de-identified.
- The de-identified patient ID column. This will map to the IDs used when initially creating a cBioPortal study.
- The IMPACT sample id column. Only required for sample-level data.

### Ideal setup of Redcap reports
Data that will be imported into cBioPortal will need to fit these three categories:
- Patient-level summaries (data_clinical_patient.txt)
- Sample-level summaries (data_clinical_sample.txt)
- Timeline files (data_timeline_specimen.txt)

Therefore, Redcap reports will ideally be constructed in a similar way:
- Non-repeating instruments, patients (Every row contains data for each **patient**)
- Repeating instruments, samples (Every row contains data for an **sample id**)
- Repeating instruments, events (Every row contains data for a date/time stamp)

If Redcap report data does not fit this ideal setup, that's okay! Steps below can be taken to format the data. Once your Redcap study is setup, the following configuration files need to be created. 

## Configuration files for exporting data from Redcap
---
### API mapping file
#### Purpose
This file is used as high-level instructions for code to perform these functions:
- Export the Redcap reports of interest onto your server. 
- Decide which reports are needed for transfer and which are to be imported onto cbioPortal
- Indicate how Redcap report data should be transformed to fit the cBioPortal format

#### Columns
- REPORT_NAME
    - Name of report on redcap, but can be named anything.
- API_ID
    - API ID number located in the Redcap report summary/edit page
- FOR_CBIOPORTAL
    - Indication if Redcap report will be loaded onto cbioportal or if left as a csv at destination
- TIMELINE_LEVEL
    - Column indicates that the Redcap report will be converted into a cBioPortal **timeline** file according to the specifications in the data transformation files. Entry for this column should be the filename for the data transformation file.
- PATIENT_LEVEL
    - Column indicates that the Redcap report will be converted into a cBioPortal **patient** summary file. For direct mapping into a summary file, enter (x). Otherwise, entry for this column should be the filename for the data transformation file. 
- SAMPLE_LEVEL
    - Column indicates that the Redcap report will be converted into a cBioPortal **sample** summary file. For direct mapping into a summary file, enter (x). Otherwise, entry for this column should be the filename for the data transformation file. 
- TIMELINE_TYPE
    - Label for the expected cBioPortl timeline file type that the Redcap report will be converted to. Each cBioPortal format file will have to adhere to a specific format. The format types are: treatment, toxicity, and diagnosis (please see the cbioportal docs for more info: [cBioPortal Docs](https://docs.cbioportal.org/5.1-data-loading/data-loading/file-formats#timeline-data))
        
### Redcap key variable map file
#### Purpose
This file is used to identify the patient and sample ID mapping (record_id to a de-identified id), while also using the DOB as a marker for de-identifying dates to age, in days

#### Columns
- variable
    - DOB column (col_dte_birth)
    - record id column (col_darwin_id)
    - de-identified ID column (col_sample_id)
    - IMPACT sample id column (col_record_id)
- redcap_field
    - Entries for each attribute defined in Redcap study
    
### Data transformation files
#### Purpose
This file is used to determine the specifications for how data will be transformed and aggregated to fit the patient-, sample-, or timeline-level data files. 

#### Columns
- COLUMN_NAME_REDCAP
    - Column name used in Redcap
- COLUMN_NAME_CBIOPORTAL
    - Column name that will be used in cbioportal ("heading" name). This name should be all CAPS. For timeline transformations, use START_DATE and END_DATE
- KEEP_FOR_CBIOPORTAL
    - (This column will be deprecated) should be all (x).
- TIMELINE
    - Marker if column shoud be included in a timeline file type. Mark as (x) to include.
- AGGREGATE_PATIENT
    - Marker if column shoud be included in a **patient**-level file type. Mark as (x) to include. If report transformed with this file is a repeated instrument, notes can be used here to aggregate by other functions (max, min, mean, etc).
- AGGREGATE_SAMPLE
    - Marker if column shoud be included in a **sample**-level file type. Mark as (x) to include. If report transformed with this file is a repeated instrument, unaligned with sample-level data, notes can be used here to aggregate by other functions (max, min, mean, etc).
- MELT_ID_VARS
    - When **melting** a Redcap report, (ie. transforming data from patient-level to timeline values) mark the row (x) that indicates the patient ID that will be used.
- MELT_VAL_VARS
    - When **melting** data, indicate the Redcap report columns to be used as date events. Note that COLUMN_NAME_CBIOPORTAL must be labeled as START_DATE or END_DATE when using.
- PIVOT_IDX
    - (This column will be deprecated) When **pivoting** a Redcap report (ie. transforming data from repeated-instrument to patient-level values), mark the row (x) that indicates the patient ID that will be used.
- PIVOT_SUMMARY
    - (This column will be deprecated) When **pivoting** data, mark the rows (x) that will be converted from multiple selection (dropdown, checkbox) into a pivot table of multiple columns of Yes/No
    
## Exporting reports from your Redcap study
---
Once the API mapping configuration file has been created, Redcap reports can be pulled to a destination using:

[`data-curation/redcap_tools/redcap_api_report_pull.py`](https://github.com/msk-mind/data-curation/blob/main/redcap_tools/redcap_api_report_pull.py)

### Requirements
Create a virtual environment containing these packages:
- redcap
- pandas
- numpy
- re
- argparse

Alternatively, after creating a virtual environment, install the required packages using the [requirements.txt](https://github.com/msk-mind/data-curation/blob/main/requirements.txt) file using 

`pip install -r /path/to/requirements.txt`

### Command Line
```
redcap_api_report_pull.py  \
-t REDCAP_API_TOKEN \
-u REDCAP_URL \
-map API_MAPPING_FILE \
-vars KEY_VARIABLE_MAP_FILE \
-dest PATH_TO_REDCAP_REPORT_EXPORTS
```

### Example
```
/path_to/venv/bin/python /path_to/redcap_tools/redcap_api_report_pull.py  \
-t your_redcap_token \
-u https://redcap.mskcc.org/api/ \
-map /path/to/mapping_file.csv \
-vars /path/to/key_variables_file.csv \
-dest /another/path/to/exported/data
```

## Formatting Redcap reports in the cBioPortal format
---
Once data and codebook is exported from Redcap, data must be transformed and formatted into the cBioPortal format before importing. The cBioPortal format consists of three file types:
- Patient-level summary
- Sample-level summary
- Timeline (event) data

Depending on the complexity of the Redcap reports being exported (i.e. reports from one instrument [simple] vs. reports from multiple instruments [complex]), built-in or custom made functions can be used. 

### Built-in functionality

#### Requirements
Create a virtual environment containing these packages:
- pandas
- numpy


Alternatively, after creating a virtual environment, install the required packages using the [requirements.txt](https://github.com/msk-mind/data-curation/blob/main/requirements.txt) file using 

`pip install -r /path/to/requirements.txt`

#### Python Function
```
class RedcapToCbioportalFormat(fname_report_api, 
                               path_config, 
                               fname_report_map, 
                               fname_variables,
                               path_save)

```
[Source Code](https://github.com/msk-mind/data-curation/blob/main/cbioportal-study-merge-tools/create_summary_from_redcap_reports.py)

##### Parameters:
```
path_config: (str) Pathname to timeline and summary data transformation files. (TODO: Deprecate. Move this info directly into the API mapping file [fname_report_api])

fname_report_api: (str) Filename for the API mapping file. This file is used as high-level instructions for export Redcap reports and pointing to transformation files.

fname_report_map: (str) Filename for table mapping the Redcap report name to the export Redcap data filename. This typically generatea a file named `*_redcap_report_mapping.tsv`

fname_variables: (str) Filename to the Redcap key variable map file. This is created when setting up the Redcap report export.

path_save: (str) Pathname to save formatted data and cBioPortal header files to be merged.
```

##### Attributes:
```
create_summary_default(patient_or_sample): 
Creates cBioPortal data and header summary files defined in the the data transformation configuration files. Options for patient_or_sample include `patient` or `sample`. 

create_timeline_files()
Create cBioPortal timeline files that can be directly imported into "datahub" 

```

##### Returns:
```
summary_manifest_patient.csv
summary_manifest_sample.csv

These manifest files contain a table mapping all patient or sample summary data and cBioPortal headers required to be merged. 

```

#### Example
```
from create_summary_from_redcap_reports import RedcapToCbioportalFormat


# Create Redcap formatting object from configuration files and pathnames
obj_redcap_to_cbio = RedcapToCbioportalFormat(fname_report_api='/path/to/api_map.csv', 
                                              path_config='/path/to/transformation/config/files',
                                              fname_report_map='/path/to/report_map.csv', 
                                              fname_variables='/path/to/variables.csv', 
                                              path_save='/path/to/headers/and/data')
# Create out-of-box summary tables from Redcap reports
obj_redcap_to_cbio.create_summary_default(patient_or_sample='patient')

# Create out-of-box timeline files
obj_redcap_to_cbio.create_timeline_files()

```

### Custom Summary Data Formatting

If Redcap report data, or any data file requires custom aggregation, cBioPortal formatting can be done manually. 
**Two files** need to be generated:

1) The datafile containing summary data
2) The cBioPortal summary header file 

In addition, **one other file** needs to be modified or created:
3) summary_manifest_patient.csv and/or summary_manifest_sample.csv

#### Header file
The header file is a dataframe containing **5 columns**:
1) `label`: The text shown on the portal summary page
2) `comment`: The "hover-over" text shown when mouse hovers over widet
3) `data_type`: Data type of columns (STRING or NUMBER)
4) `visible`: Mark 0 or 1 to make visible on summary page
5) `heading`: Column names contained in the datafile (below). These columns **MUST** match the datafile!

For summary and header files, the `heading` column must be `PATIENT_ID` or `SAMPLE_ID`. In addition, the `label` column must contain `#Patient Identifier` or `#Sample Identifier`.

#### Datafile
The datafile contains data to be imported. The column header (first row) must match the `heading` values in the header file.

For summary files, the first column must be `PATIENT_ID` or `SAMPLE_ID`

#### Modifying the manifest file
The patient and sample manifest files contain **three** columns:
1) `REPORT_NAME`: The name of the summary file created. Typically taken from API map file, but can be named anything.
2) `SUMMARY_FILENAME`: Complete path, filename of the summary datafile.
3) `SUMMARY_HEADER_FILENAME`: Complete path, filename of the corresponding header file.

For each set of data and header files, a new row must be entered into the manifest file. **This data is required when merging summary data!!**

## Merging formatted files for datahub import
---
Once summary data and header files are created, a Python script is required to merge the summary files. 


### Built-in merge functionality
#### Requirements
Create a virtual environment containing these packages:
- pandas

Alternatively, after creating a virtual environment, install the required packages using the [requirements.txt](https://github.com/msk-mind/data-curation/blob/main/requirements.txt) file using 

`pip install -r /path/to/requirements.txt`

#### Python Function
```
class cbioportalSummaryFileCombiner(fname_manifest, 
                                    fname_current_summary, 
                                    patient_or_sample)

```
[Source Code](https://github.com/msk-mind/data-curation/blob/main/cbioportal-study-merge-tools/cbioportal_summary_file_combiner.py)

##### Parameters:
```
fname_manifest: (str) Filename to patient or sample manifest files. Should be either `summary_manifest_patient.csv` or `summary_manifest_sample.csv`

fname_current_summary: (str) Filename of the current patient or sample summary file (i.e. data_clinical_patient.txt)

patient_or_sample: (str) Options for patient_or_sample include `patient` or `sample` for patient or sample level summary merging.
```

##### Attributes:
```
return_orig(): (tuple)
Returns the header and data in a tuple (header, data)

save_update(fname): (None)
Saves updated/merged summary file to `fname`

```

#### Example
```
import sys
import pandas as pd
sys.path.insert(0, '/path_to/data-curation/cbioportal-study-merge-tools')
from cbioportal_summary_file_combiner import cbioportalSummaryFileCombiner


fname_manifest_sample = 'summary_manifest_sample.csv'
fname_s_sum = '/datahub/you_study/data_clinical_sample_template.txt'

# Sample updates
obj_s_combiner = cbioportalSummaryFileCombiner(fname_manifest=fname_manifest_sample, 
                                               fname_current_summary=fname_s_sum, 
                                               patient_or_sample='sample')

# Return original summary dataframe and header
orig_header_s, orig_summary_s = obj_s_combiner.return_orig()

# Save updated/merged data
obj_s_combiner.save_update(fname=fname_cbio_s_save)

```



### Manual summary merging
Manual merging can be done using the class `cBioPortalSummaryMergeTool`
[Source](https://github.com/msk-mind/data-curation/blob/main/cbioportal-study-merge-tools/cbioportal_summary_merger.py)


More under construction...

