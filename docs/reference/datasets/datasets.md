# msk_cdm.datasets

Utilities to load various clinical datasets related to the MSK-IMPACT cohort (de-identified and PHI versions), and datasets derived from IDB queries.


## MSK-IMPACT Datasets (De-identified)

| Function Name                           | Description                                                     |
|----------------------------------------|-----------------------------------------------------------------|
| `load_impact_data_clinical_patient`     | Load the clinical patient summary data from the IMPACT dataset. |
| `load_impact_data_clinical_sample`      | Load the clinical sample summary data from the IMPACT dataset.  |
| `load_impact_data_timeline_surgery`     | Load the surgical timeline data from the IMPACT dataset.         |
| `load_impact_data_timeline_radiation`   | Load the radiation therapy timeline data from the IMPACT dataset.|
| `load_impact_data_timeline_treatment`   | Load the treatment timeline data from the IMPACT dataset.         |
| `load_impact_data_timeline_diagnosis`   | Load the diagnosis timeline data from the IMPACT dataset.         |
| `load_impact_data_timeline_specimen`    | Load the specimen timeline data from the IMPACT dataset.          |
| `load_impact_data_timeline_specimen_surgery` | Load the specimen surgery timeline data from the IMPACT dataset.|
| `load_impact_data_timeline_gleason`     | Load the Gleason score timeline data from the IMPACT dataset.     |
| `load_impact_data_timeline_pdl1`        | Load the PD-L1 timeline data from the IMPACT dataset.             |
| `load_impact_data_timeline_mmr`         | Load the MMR timeline data from the IMPACT dataset.               |
| `load_impact_data_timeline_prior_meds`  | Load the prior medications timeline data from the IMPACT dataset. |
| `load_impact_data_timeline_tumor_sites` | Load the tumor sites timeline data from the IMPACT dataset.       |
| `load_impact_data_timeline_follow_up`   | Load the follow-up timeline data from the IMPACT dataset.         |
| `load_impact_data_timeline_progression` | Load the progression timeline data from the IMPACT dataset.       |
| `load_impact_data_timeline_cancer_presence` | Load the cancer presence timeline data from the IMPACT dataset. |
| `load_impact_data_timeline_ecog_kps`    | Load the ECOG-KPS timeline data from the IMPACT dataset.          |

## MSK-IMPACT Datasets (Contains PHI)

| Function Name                           | Description                                                     |
|----------------------------------------|-----------------------------------------------------------------|
| `load_phi_impact_data_timeline_surgery` | Load the surgical timeline data in the PHI IMPACT format.        |
| `load_phi_impact_data_timeline_radiation` | Load the radiation therapy timeline data in the PHI IMPACT format.|
| `load_phi_impact_data_timeline_treatment` | Load the treatment timeline data in the PHI IMPACT format.       |
| `load_phi_impact_data_timeline_diagnosis` | Load the diagnosis timeline data in the PHI IMPACT format.       |
| `load_phi_impact_data_timeline_specimen`  | Load the specimen timeline data in the PHI IMPACT format.        |
| `load_phi_impact_data_timeline_specimen_surgery` | Load the specimen surgery timeline data in the PHI IMPACT format.|
| `load_phi_impact_data_timeline_gleason`   | Load the Gleason score timeline data in the PHI IMPACT format.   |
| `load_phi_impact_data_timeline_pdl1`      | Load the PD-L1 timeline data in the PHI IMPACT format.           |
| `load_phi_impact_data_timeline_prior_meds`| Load the prior medications timeline data in the PHI IMPACT format.|
| `load_phi_impact_data_timeline_tumor_sites`| Load the tumor sites timeline data in the PHI IMPACT format.     |
| `load_phi_impact_data_timeline_follow_up` | Load the follow-up timeline data in the PHI IMPACT format.       |
| `load_phi_impact_data_timeline_progression` | Load the progression timeline data in the PHI IMPACT format.     |
| `load_phi_impact_data_timeline_mmr`       | Load the MMR timeline data in the PHI IMPACT format.             |
| `load_phi_impact_data_timeline_cancer_presence` | Load the cancer presence timeline data in the PHI IMPACT format.|
| `load_phi_impact_data_timeline_ecog_kps`  | Load the ECOG-KPS timeline data in the PHI IMPACT format.        |
| `load_phi_impact_id_mapping`              | Load the ID mapping data in the PHI IMPACT format.              |
| `load_phi_impact_anchor_dates`            | Load the anchor dates data in the PHI IMPACT format.            |

## Datasets from IDB Queries

| Function Name                           | Description                                                     |
|----------------------------------------|-----------------------------------------------------------------|
| `load_phi_idb_demographics`            | Load the demographics data from IDB queries.                    |
| `load_phi_idb_radiology_reports`       | Load the radiology reports data from IDB queries.                |
| `load_phi_idb_pathology_reports`       | Load the pathology reports data from IDB queries.                |
| `load_phi_idb_surgeries`               | Load the surgeries data from IDB queries.                        |
| `load_phi_idb_diagnosis`               | Load the diagnosis data from IDB queries.                        |
| `load_phi_idb_medications`            | Load the medications data from IDB queries.                      |
| `load_phi_idb_radiation`               | Load the radiation data from IDB queries.                        |
| `load_phi_idb_interventional_radiology`| Load the interventional radiology data from IDB queries.         |
