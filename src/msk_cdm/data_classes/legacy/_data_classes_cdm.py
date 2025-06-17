"""
data_classes_cdm.py

"""

import os
from dataclasses import dataclass


@dataclass
class CDMProcessingVariables:
    ##############################################################################
    # Utilities
    ##############################################################################
    #minio_env: str = "/gpfs/mindphidata/fongc2/minio_env.txt"

    ##############################################################################
    # Column names of interest
    ##############################################################################
    col_id: str = "ACCESSION_NUMBER"
    col_findings_label: str = "FINDINGS_LABEL_OR_ORGAN"
    column_text: str = "RRPT_REPORT_TXT"
    column_imp: str = "IMPRESSION"

    ##############################################################################
    # Queried data from the cBioPortal API
    ##############################################################################
    fname_cbio_sid_api: str = "cbioportal/mskimpact_ids.tsv"
    #fname_cbio_sid: str = "/gpfs/mindphidata/cdm_repos/datahub/msk-impact/msk_solid_heme/data_clinical_sample.txt"
    study_id: str = "mskimpact"
    fname_cbio_samples_clean: str = "cbioportal/mskimpact_ids_clean.tsv"
    fname_cbio_sample_summary_clean: str = "cbioportal/mskimpact_ids_summary.tsv"

    fname_anchor_dates_reid: str = "cbioportal/timeline_anchor_dates.tsv"
    fname_overall_survival: str = 'demographics/overall_survival_cbioportal.tsv'

    ##############################################################################
    # Queried data from IDB
    ##############################################################################
    fname_demo: str = "demographics/ddp_demographics.tsv"
    fname_surg: str = "surgery/ddp_surgery.tsv"
    fname_dx: str = "diagnosis/ddp_dx.tsv"
    fname_meds: str = "medications/ddp_chemo.tsv"
    fname_rt: str = "radonc/ddp_radonc.tsv"
    fname_ir: str = "interventional-radiology/ddp_ir.tsv"
    fname_clindoc_fu_initial: str = "clindoc/ddp_clindoc_initial_and_fu_notes.tsv"
    fname_comorbidities: str = "comorbidities/ddp_comorbidities.tsv"
    fname_insurance: str = "insurance/ddp_insurance.tsv"
    col_mrn_sql_clindoc: str = "CDD_MRN"

    ##############################################################################
    # DIAGNOSIS TABLE derived files
    #############################################################################
    ### Clean diagnosis table
    fname_dx_clean: str = "diagnosis/table_diagnosis_clean.tsv"

    ### Patient level summary table
    fname_dx_summary: str = (
        "diagnosis/table_dx_impact_summary.tsv"  # Table of impact sample processed
    )
    fname_met_site_summary: str = "diagnosis/table_met_site_summary.tsv"
    fname_dx_timeline_prim: str = "diagnosis/table_dx_timeline_primary.tsv"
    fname_path_summary: str = (
        "pathology/table_pathology_impact_sample_summary_dop_anno.tsv"
    )

    fname_timeline_fu: str = "demographics/table_timeline_follow_up.tsv"

    ##############################################################################
    # PATHOLOGY REPORT derived files
    ##############################################################################
    # Pathology Segmentation tasks
    ### Pathology table from copath
    fname_path_synoptic_labels: str = (
        "pathology/table_pathology_surgical_synoptic_labels.csv"
    )
    fname_path_synoptic: str = "pathology/path_synoptic_predictions.tsv"

    ### IDB table
    fname_pathology: str = "pathology/ddp_pathology_reports.tsv"
    fname_pathology_update: str = (
        "pathology/intermediate_files/ddp_pathology_reports_update.tsv"
    )
    fname_pathology_bkup: str = (
        "pathology/intermediate_files/ddp_pathology_reports_bkup.tsv"
    )

    ### Clean path table
    fname_path_clean: str = "pathology/table_pathology_clean.tsv"
    fname_id_map: str = "id-mapping/ddp_id_mapping_pathology.tsv"

    ## Parsed Pathology data
    ### Main Pathology sections
    fname_darwin_path_molecular: str = (
        "pathology/table_pathology_molecular_notes_parsed.tsv"
    )
    fname_darwin_path_surgical: str = (
        "pathology/table_pathology_surgical_notes_parsed.tsv"
    )
    fname_darwin_path_cyto: str = "pathology/table_pathology_cyto_notes_parsed.tsv"
    fname_darwin_path_heme: str = "pathology/table_pathology_heme_notes_parsed.tsv"

    ### Specimen submitted
    fname_darwin_path_col_spec_sub: str = "pathology/table_pathology_col_spec_sub.tsv"
    fname_darwin_path_molecular_note_spec_sub: str = (
        "pathology/table_pathology_molecular_note_spec_sub.tsv"
    )
    fname_darwin_path_surgical_note_spec_sub: str = (
        "pathology/table_pathology_surgical_note_spec_sub.tsv"
    )

    fname_darwin_path_dmp: str = "pathology/table_pathology_impact_dmp_extraction.tsv"
    fname_darwin_path_clean_parsed: str = "pathology/table_pathology_surgical_samples_parsed.tsv"  # Filename of processed pathology table (variable: fname_darwin_path)
    fname_darwin_path_clean_parsed_specimen: str = "pathology/table_pathology_surgical_samples_parsed_specimen.tsv"  # Filename of parsed specimen pathology
    fname_darwin_path_clean_parsed_specimen_impact_only: str = (
        "pathology/table_pathology_impact_only_parsed_specimen.tsv"
    )

    ## Annotations
    ### Table of MSK-IMPACT to source (Surgical/Cytology) accessions
    fname_path_accessions: str = "pathology/path_accessions.tsv"
    ### Table of MSK-IMPACT to date of procedure
    fname_spec_part_dop: str = "pathology/pathology_spec_part_dop.tsv"
    ### Table combining MSK-IMPACT report accession, source accession, date of procedure
    fname_combine_dop_accession: str = "pathology/pathology_dop_impact_summary.tsv"
    ### File "fname_combine_dop_accession" with annotation for source of extraction (IMPACT report, surgical, IR)
    fname_dop_anno: str = "pathology/table_pathology_impact_sample_summary_dop_anno.tsv"
    fname_darwin_path_heme_parse_bm_biopsy: str = (
        "pathology/pathology_heme_bm_biopsy.tsv"
    )
    fname_darwin_path_heme_parse_periph_blood: str = (
        "pathology/pathology_heme_periph_blood.tsv"
    )
    fname_path_pdl1: str = "pathology/pathology_pdl1_calls.tsv"
    fname_path_gleason: str = "pathology/pathology_gleason_calls.tsv"
    fname_path_mmr: str = "pathology/pathology_mmr_calls.tsv"

    ## cBioPortal file generation
    ### Timeline
    fname_path_sequencing_cbio_timeline: str = "pathology/table_timeline_sequencing.tsv"
    fname_path_specimen_surgery_cbio_timeline: str = (
        "pathology/table_timeline_specimen_surgery.tsv"
    )
    fname_path_gleason_cbio_timeline: str = (
        "pathology/table_timeline_gleason_scores.tsv"
    )
    fname_path_mmr_cbio_timeline: str = (
        "pathology/table_timeline_mmr_calls.tsv"
    )
    fname_path_pdl1_cbio_timeline: str = "pathology/table_timeline_pdl1_calls.tsv"
    fname_path_gleason_summary_patient: str = (
        "pathology/table_summary_gleason_patient.tsv"
    )
    fname_path_gleason_summary_sample: str = (
        "pathology/table_summary_gleason_sample.tsv"
    )
    fname_path_pdl1_summary_patient: str = "pathology/table_summary_pdl1_patient.tsv"
    fname_path_pdl1_summary_sample: str = "pathology/table_summary_pdl1_sample.tsv"

    col_pathology_id: str = "ACCESSION_NUMBER"

    ##############################################################################
    # RADIOLOGY REPORT derived files
    ##############################################################################
    # Radiology Filenames, raw and segmentations
    fname_radiology: str = (
        "/radiology/radiology_report_segmentation/impact/ddp_radiology_reports.tsv"
    )
    fname_radiology_bkup: str = "/radiology/radiology_report_segmentation/impact/intermediate_files_for_qc/ddp_radiology_reports_bkup.tsv"
    fname_radiology_update: str = "/radiology/radiology_report_segmentation/impact/intermediate_files_for_qc/ddp_radiology_reports_update.tsv"
    fname_radiology_to_segment: str = "/radiology/radiology_report_segmentation/impact/intermediate_files_for_qc/ddp_radiology_reports_for_segmentation.tsv"
    fname_radiology_metadata: str = "/radiology/radiology_report_segmentation/impact/intermediate_files_for_qc/radiology_clean_annotations.tsv"
    fname_radiology_impression: str = "/radiology/radiology_report_segmentation/impact/intermediate_files_for_qc/radiology_parse_impression.tsv"
    fname_radiology_findings: str = "/radiology/radiology_report_segmentation/impact/intermediate_files_for_qc/radiology_parse_findings.tsv"
    fname_radiology_findings_long: str = "/radiology/radiology_report_segmentation/impact/intermediate_files_for_qc/radiology_parse_findings_long.tsv"
    fname_radiology_headers = "/radiology/radiology_report_segmentation/impact/intermediate_files_for_qc/radiology_parse_headers.tsv"
    fname_radiology_full_parsed: str = "/radiology/radiology_report_segmentation/impact/ddp_radiology_reports_full_parsed.tsv"

    ## Tumor sites (ClinicalBERT-based method)
    fname_rad_prediction_all_accessions: str = "/radiology/tumor_sites/impact/intermediate_files/radiology_accessions_for_pred_all.tsv"
    fname_radiology_tumor_site_pred: str = (
        "/radiology/tumor_sites/impact/radiology_tumor_site_predictions_full.tsv"
    )
    fname_radiology_tumor_site_pred_summary: str = "/radiology/tumor_sites/impact/radiology_tumor_site_predictions_full_summary.tsv"
    fname_rad_tumor_prediction_update: str = "/radiology/tumor_sites/impact/intermediate_files/radiology_tumor_site_predictions_updated.tsv"
    fname_radiology_tumor_site_pred_combined: str = "/radiology/tumor_sites/impact/intermediate_files/radiology_tumor_site_predictions_combined.tsv"
    fname_rad_rpts_for_prediction_tumor_sites: str = "/radiology/tumor_sites/impact/intermediate_files/ddp_radiology_reports_for_prediction.tsv"
    #log_fname_template_tumor_sites: str = (
    #    "/gpfs/mindphidata/fongc2/github/radiology_met_prediction/condor/logs/log_infer.txt"
    #)
    fname_tumor_sites_timeline_cbio: str = (
        "/radiology/tumor_sites/impact/table_timeline_tumor_sites.tsv"
    )

    ## Progression (RoBERTa-based method)
    fname_progression_prediction_all_accessions: str = "/radiology/progression/impact/intermediate_files/radiology_accessions_for_pred_all.tsv"
    fname_radiology_progression_pred_bkup: str = "/radiology/progression/impact/intermediate_files/radiology_cancer_progression_predictions.tsv.bkup"
    fname_radiology_progression_pred: str = (
        "/radiology/progression/impact/radiology_cancer_progression_predictions.tsv"
    )
    fname_progression_timeline_cbio: str = (
        "radiology/progression/impact/table_timeline_radiology_cancer_progression_predictions.tsv"
    )
    fname_rad_prog_prediction_update: str = "/radiology/progression/impact/intermediate_files/radiology_progression_predictions_updated.tsv"
    fname_rad_prog_prediction_combined: str = "/radiology/progression/impact/intermediate_files/radiology_cancer_progression_predictions_combined.tsv"
    fname_rad_rpts_for_prediction_progression: str = "/radiology/progression/impact/intermediate_files/ddp_radiology_reports_for_prediction_progression.tsv"
    #log_fname_template_progression: str = (
    #    "/gpfs/mindphidata/fongc2/github/progression-predict/condor/logs/log_infer.txt"
    #)

    ## Training Labels
    ### Metastatic sites (GENIE)
    ### Progression (GENIE)
    fname_labels_genie_progression: str = "labels/progression/genie_lung_crc_breast_prostate_pancreas_progression_labels_20200923.tsv"

    # Column names of interest
    col_radiology_id: str = "ACCESSION_NUMBER"
    col_radiology_findings_label: str = "FINDINGS_LABEL_OR_ORGAN"
    col_radiology_text: str = "RRPT_REPORT_TXT"
    col_radiology_impressions: str = "IMPRESSION"
    col_radiology_findings: str = "FINDINGS"
    col_radiology_findings_long: str = "FINDINGS_DESC"
    col_radiology_proc_type: str = "PROCEDURE_TYPE"
    col_radiology_patient_id: str = "MRN"
    col_radiology_date: str = "RADIOLOGY_PERFORMED_DATE"

    ## Cancer Presence inference
    fname_radiology_cancer_presence_predictions = "radiology/cancer_presence/impact/radiology_cancer_presence_prediction.tsv"
    fname_radiology_cancer_presence_timeline = "radiology/cancer_presence/impact/table_timeline_cancer_presence.tsv"

    ##############################################################################
    # TREATMENT (Medications, surgeries, RT) derived files
    ##############################################################################
    fname_meds_clean: str = "medications/table_medications_clean.tsv"
    fname_meds_intervals: str = "medications/table_medication_intervals.tsv"
    fname_meds_regimens: str = "medications/table_medication_regimens.tsv"

    fname_timeline_surg: str = "surgery/table_timeline_surgery.tsv"
    fname_timeline_rt: str = "radonc/table_timeline_radiation.tsv"
    fname_timeline_meds: str = "medications/table_timeline_medications.tsv"

    fname_tx_summary_patient: str = "medications/table_tx_summary_patient.tsv"
    fname_tx_summary_sample: str = "medications/table_tx_summary_sample.tsv"

    ##############################################################################
    # PRIOR MEDICATIONS PREDICTIONS
    ##############################################################################
    fname_prior_meds_predictions_prefix: str = (
        "medications/prior_tx_inferences/prior_tx_inferences_impact"
    )
    fname_prior_meds_predictions_comb: str = (
        "medications/prior_tx_inferences/prior_tx_inferences_impact_combined.tsv"
    )
    fname_prior_meds_predictions_comb_bkup: str = (
        "medications/prior_tx_inferences/prior_tx_inferences_impact_combined.tsv.bkup"
    )
    fname_prior_meds_predictions_timeline: str = (
        "medications/prior_tx_inferences/prior_tx_inferences_impact_cbio_timeline.tsv"
    )

    ##############################################################################
    # SDoH derived files
    ##############################################################################
    fname_comorbidities_index: str = "comorbidities/ddp_comorbidities_index_summary.tsv"
    fname_clindoc_smoking: str = "comorbidities/ddp_smoking_history.tsv"
    fname_smoking_status: str = "comorbidities/smoking_status_predictions.tsv"

    fname_insurance_clean: str = "insurance/ddp_insurance_clean.tsv"
    fname_insurance_summary: str = "insurance/ddp_insurance_summary.tsv"
    fname_yost: str = "comorbidities/yost_index_results.tsv"

    fname_ecog_predictions: str = "clindoc/ecog/impact/ecog_kps_predictions.tsv"
    fname_ecog_timeline_cbio: str = "clindoc/ecog/impact/table_timeline_ecog_kps.tsv"
    fname_ecog_summary_cbio: str = "clindoc/ecog/impact/table_summary_ecog_patient.tsv"


@dataclass
class CDMRedcapConfig:
    ##############################################################################
    # Filenames
    ##############################################################################
    # Redcap: AI/ML IMPACT Curation Efforts
    fname_api_keys_ai_ml_impact: str = "config/redcap_report_api_map_ai_ml_impact.csv"
    path_vars_file_ai_ml_impact: str = "config/redcap_variables_ai_ml_impact.csv"

    ##############################################################################
    # GENIE Redcap Reports
    ##############################################################################
    fname_genie_rc_met_sites_breast: str = "redcap_exports/genie_bpc_breast/19-368__GENIE_BPC_-_BREAST_Cohort_Imaging_Metastatic_Events.tsv"
    fname_genie_rc_met_sites_crc: str = "redcap_exports/genie_bpc_crc/19-368__GENIE_BPC_-_CRC_Production_Cohort_Imaging_Metastatic_Events.tsv"
    fname_genie_rc_met_sites_lung: str = "redcap_exports/genie_bpc_lung/MED19-213__Genie_BPC_Lung_Production_Imaging_Metastatic_Events.tsv"
    fname_genie_rc_met_sites_lung2: str = "redcap_exports/genie_bpc_lung_additional/19-368__Genie_BPC_Lung_Cohort_Additional_Data_Imaging_Metastatic_Events.tsv"
    fname_genie_rc_met_sites_pancreas: str = "redcap_exports/genie_bpc_pancreas/19-368__GENIE_BPC_-_Pancreas_Cohort_Imaging_Metastatic_Events.tsv"
    fname_genie_rc_met_sites_prostate: str = "redcap_exports/genie_bpc_prostate/19-368__GENIE_BPC_-_Prostate_Cohort_Imaging_Metastatic_Events.tsv"
