# msk_cdm.datasets

Utilities to load various clinical datasets related to the MSK-IMPACT cohort (de-identified and PHI versions), and datasets derived from IDB queries.

## MSK-IMPACT Datasets (De-identified)

| Function Name | Description |
|---|---|
| [`load_impact_data_clinical_patient`](reference/datasets/impact/load_impact_data_clinical_patient.md) | Load the clinical patient summary data from the IMPACT dataset. |
| [`load_impact_data_clinical_sample`](reference/datasets/impact/load_data_clinical_sample.md) | Load the clinical sample summary data from the IMPACT dataset. |
| [`load_impact_data_timeline_surgery`](reference/datasets/impact/load_data_timeline_surgery.md) | Load the surgical timeline data from the IMPACT dataset. |
| [`load_impact_data_timeline_radiation`](reference/datasets/impact/load_data_timeline_radiation.md) | Load the radiation therapy timeline data from the IMPACT dataset. |
| [`load_impact_data_timeline_treatment`](reference/datasets/impact/load_data_timeline_treatment.md) | Load the treatment timeline data from the IMPACT dataset. |
| [`load_impact_data_timeline_diagnosis`](reference/datasets/impact/load_data_timeline_diagnosis.md) | Load the diagnosis timeline data from the IMPACT dataset. |
| [`load_impact_data_timeline_specimen`](reference/datasets/impact/load_data_timeline_specimen.md) | Load the specimen timeline data from the IMPACT dataset. |
| [`load_impact_data_timeline_specimen_surgery`](reference/datasets/impact/load_data_timeline_specimen_surgery.md) | Load the specimen surgery timeline data from the IMPACT dataset. |
| [`load_impact_data_timeline_gleason`](reference/datasets/impact/load_data_timeline_gleason.md) | Load the Gleason score timeline data from the IMPACT dataset. |
| [`load_impact_data_timeline_pdl1`](reference/datasets/impact/load_data_timeline_pdl1.md) | Load the PD-L1 timeline data from the IMPACT dataset. |
| [`load_impact_data_timeline_mmr`](reference/datasets/impact/load_data_timeline_mmr.md) | Load the MMR timeline data from the IMPACT dataset. |
| [`load_impact_data_timeline_prior_meds`](reference/datasets/impact/load_data_timeline_prior_meds.md) | Load the prior medications timeline data from the IMPACT dataset. |
| [`load_impact_data_timeline_tumor_sites`](reference/datasets/impact/load_data_timeline_tumor_sites.md) | Load the tumor sites timeline data from the IMPACT dataset. |
| [`load_impact_data_timeline_follow_up`](reference/datasets/impact/load_data_timeline_follow_up.md) | Load the follow-up timeline data from the IMPACT dataset. |
| [`load_impact_data_timeline_progression`](reference/datasets/impact/load_data_timeline_progression.md) | Load the progression timeline data from the IMPACT dataset. |
| [`load_impact_data_timeline_cancer_presence`](reference/datasets/impact/load_data_timeline_cancer_presence.md) | Load the cancer presence timeline data from the IMPACT dataset. |
| [`load_impact_data_timeline_ecog_kps`](reference/datasets/impact/load_data_timeline_ecog_kps.md) | Load the ECOG-KPS timeline data from the IMPACT dataset. |

## MSK-IMPACT Datasets (Contains PHI)

| Function Name | Description |
|---|---|
| [`load_phi_impact_data_timeline_surgery`](phi_impact/load_data_timeline_surgery_phi.md) | Load the surgical timeline data in the PHI IMPACT format. |
| [`load_phi_impact_data_timeline_radiation`](phi_impact/load_data_timeline_radiation_phi.md) | Load the radiation therapy timeline data in the PHI IMPACT format. |
| [`load_phi_impact_data_timeline_treatment`](phi_impact/load_data_timeline_treatment_phi.md) | Load the treatment timeline data in the PHI IMPACT format. |
| [`load_phi_impact_data_timeline_diagnosis`](phi_impact/load_data_timeline_diagnosis_phi.md) | Load the diagnosis timeline data in the PHI IMPACT format. |
| [`load_phi_impact_data_timeline_specimen`](phi_impact/load_data_timeline_specimen_phi.md) | Load the specimen timeline data in the PHI IMPACT format. |
| [`load_phi_impact_data_timeline_specimen_surgery`](phi_impact/load_data_timeline_specimen_surgery_phi.md) | Load the specimen surgery timeline data in the PHI IMPACT format. |
| [`load_phi_impact_data_timeline_gleason`](phi_impact/load_data_timeline_gleason_phi.md) | Load the Gleason score timeline data in the PHI IMPACT format. |
| [`load_phi_impact_data_timeline_pdl1`](phi_impact/load_data_timeline_pdl1_phi.md) | Load the PD-L1 timeline data in the PHI IMPACT format. |
| [`load_phi_impact_data_timeline_prior_meds`](phi_impact/load_data_timeline_prior_meds_phi.md) | Load the prior medications timeline data in the PHI IMPACT format. |
| [`load_phi_impact_data_timeline_tumor_sites`](phi_impact/load_data_timeline_tumor_sites_phi.md) | Load the tumor sites timeline data in the PHI IMPACT format. |
| [`load_phi_impact_data_timeline_follow_up`](phi_impact/load_data_timeline_follow_up_phi.md) | Load the follow-up timeline data in the PHI IMPACT format. |
| [`load_phi_impact_data_timeline_progression`](phi_impact/load_data_timeline_progression_phi.md) | Load the progression timeline data in the PHI IMPACT format. |
| [`load_phi_impact_data_timeline_mmr`](phi_impact/load_data_timeline_mmr_phi.md) | Load the MMR timeline data in the PHI IMPACT format. |
| [`load_phi_impact_data_timeline_cancer_presence`](phi_impact/load_data_timeline_cancer_presence_phi.md) | Load the cancer presence timeline data in the PHI IMPACT format. |
| [`load_phi_impact_data_timeline_ecog_kps`](phi_impact/load_data_timeline_ecog_kps_phi.md) | Load the ECOG-KPS timeline data in the PHI IMPACT format. |
| [`load_phi_impact_id_mapping`](phi_impact/load_data_id_mapping_phi.md) | Load the ID mapping data in the PHI IMPACT format. |
| [`load_phi_impact_anchor_dates`](phi_impact/load_data_anchor_dates_phi.md) | Load the anchor dates data in the PHI IMPACT format. |

## Datasets from IDB Queries

| Function Name | Description |
|---|---|
| [`load_phi_idb_demographics`](phi_idb/load_demographics_idb.md) | Load the demographics data from IDB queries. |
| [`load_phi_idb_radiology_reports`](phi_idb/load_radiology_reports_idb.md) | Load the radiology reports data from IDB queries. |
| [`load_phi_idb_pathology_reports`](phi_idb/load_pathology_reports_idb.md) | Load the pathology reports data from IDB queries. |
| [`load_phi_idb_surgeries`](phi_idb/load_surgeries_idb.md) | Load the surgeries data from IDB queries. |
| [`load_phi_idb_diagnosis`](phi_idb/load_diagnosis_idb.md) | Load the diagnosis data from IDB queries. |
| [`load_phi_idb_medications`](phi_idb/load_medications_idb.md) | Load the medications data from IDB queries. |
| [`load_phi_idb_radiation`](phi_idb/load_radiation_idb.md) | Load the radiation data from IDB queries. |
| [`load_phi_idb_interventional_radiology`](phi_idb/load_interventional_radiology_idb.md) | Load the interventional radiology data from IDB queries. |
