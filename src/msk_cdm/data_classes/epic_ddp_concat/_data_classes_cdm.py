"""
data_classes_cdm.py

"""

import os
from dataclasses import dataclass, field


@dataclass
class CDMProcessingVariables:
    ##############################################################################
    # Codebook CSV file map
    ##############################################################################
    codebook_file_map: dict = field(default_factory=lambda: {
        "metadata": "CDM-Codebook - metadata.csv",
        "tables": "CDM-Codebook - tables.csv",
        "project": "CDM-Codebook - project.csv",
        "nlp_performance": "CDM Model Performance - Summary Results (CDSI).csv",
    })

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
    study_id: str = "mskimpact"

    fname_anchor_dates_reid: str = "epic_ddp_concat/cbioportal/timeline_anchor_dates.tsv"
    fname_overall_survival: str = 'demographics/overall_survival_cbioportal.tsv'

    ##############################################################################
    # Queried data from IDB
    ##############################################################################
    fname_demo: str = "epic_ddp_concat/demographics/t01_epic_ddp_demographics.tsv"
    # fname_surg: str = "epic_ddp_concat/surgery/ddp_surgery.tsv"
    # fname_dx: str = "epic_ddp_concat/diagnosis/ddp_dx.tsv"
    # fname_meds: str = "epic_ddp_concat/medications/ddp_chemo.tsv"
    # fname_rt: str = "epic_ddp_concat/radonc/ddp_radonc.tsv"
    # fname_ir: str = "epic_ddp_concat/interventional-radiology/ddp_ir.tsv"
    # fname_clindoc_fu_initial: str = "epic_ddp_concat/clindoc/ddp_clindoc_initial_and_fu_notes.tsv"
    fname_comorbidities: str = "epic_ddp_concat/comorbidities/t09_epic_ddp_comorbidities.tsv"
    # fname_insurance: str = "epic_ddp_concat/insurance/ddp_insurance.tsv"
    # col_mrn_sql_clindoc: str = "CDD_MRN"

    ##############################################################################
    # DIAGNOSIS TABLE derived files
    #############################################################################
    ### Clean diagnosis table
    fname_dx_clean: str = "epic_ddp_concat/diagnosis/table_diagnosis_clean.tsv"

    ### Patient level summary table
    fname_dx_summary: str = "epic_ddp_concat/diagnosis/table_dx_impact_summary.tsv"  # Table of impact sample processed
    fname_met_site_summary: str = "epic_ddp_concat/diagnosis/table_met_site_summary.tsv"
    fname_dx_timeline_prim: str = "epic_ddp_concat/diagnosis/table_dx_timeline_primary.tsv"
    fname_path_summary: str = "epic_ddp_concat/pathology/table_pathology_impact_sample_summary_dop_anno.tsv"

    fname_timeline_fu: str = "epic_ddp_concat/demographics/table_timeline_follow_up.tsv"

    ##############################################################################
    # PATHOLOGY REPORT derived files
    ##############################################################################
    # Pathology Segmentation tasks
    ### IDB table
    fname_pathology: str = "epic_ddp_concat/pathology/ddp_pathology_reports.tsv"
    fname_pathology_update: str = "epic_ddp_concat/pathology/intermediate_files/ddp_pathology_reports_update.tsv"
    fname_pathology_bkup: str = "epic_ddp_concat/pathology/intermediate_files/ddp_pathology_reports_bkup.tsv"

    ### Clean path table
    fname_path_clean: str = "epic_ddp_concat/pathology/table_pathology_clean.tsv"
    fname_id_map: str = "epic_ddp_concat/id-mapping/epic_ddp_id_mapping_pathology.tsv"

    ## Parsed Pathology data
    ### Main Pathology sections
    fname_darwin_path_molecular: str = "epic_ddp_concat/pathology/table_pathology_molecular_notes_parsed.tsv"
    fname_darwin_path_surgical: str = "epic_ddp_concat/pathology/table_pathology_surgical_notes_parsed.tsv"
    fname_darwin_path_cyto: str = "epic_ddp_concat/pathology/table_pathology_cyto_notes_parsed.tsv"
    fname_darwin_path_heme: str = "epic_ddp_concat/pathology/table_pathology_heme_notes_parsed.tsv"

    ### Specimen submitted
    fname_darwin_path_col_spec_sub: str = "epic_ddp_concat/pathology/table_pathology_col_spec_sub.tsv"
    fname_darwin_path_molecular_note_spec_sub: str = "epic_ddp_concat/pathology/table_pathology_molecular_note_spec_sub.tsv"
    fname_darwin_path_surgical_note_spec_sub: str = "epic_ddp_concat/pathology/table_pathology_surgical_note_spec_sub.tsv"

    fname_darwin_path_dmp: str = "epic_ddp_concat/pathology/table_pathology_impact_dmp_extraction.tsv"
    fname_darwin_path_clean_parsed: str = "epic_ddp_concat/pathology/table_pathology_surgical_samples_parsed.tsv"  # Filename of processed pathology table (variable: fname_darwin_path)
    fname_darwin_path_clean_parsed_specimen: str = "epic_ddp_concat/pathology/table_pathology_surgical_samples_parsed_specimen.tsv"  # Filename of parsed specimen pathology
    fname_darwin_path_clean_parsed_specimen_impact_only: str = "epic_ddp_concat/pathology/table_pathology_impact_only_parsed_specimen.tsv"

    ## Annotations
    ### Table of MSK-IMPACT to source (Surgical/Cytology) accessions
    fname_path_accessions: str = "epic_ddp_concat/pathology/path_accessions.tsv"
    ### Table of MSK-IMPACT to date of procedure
    fname_spec_part_dop: str = "epic_ddp_concat/pathology/pathology_spec_part_dop.tsv"
    ### Table combining MSK-IMPACT report accession, source accession, date of procedure
    fname_combine_dop_accession: str = "epic_ddp_concat/pathology/pathology_dop_impact_summary.tsv"
    ### File "fname_combine_dop_accession" with annotation for source of extraction (IMPACT report, surgical, IR)
    fname_dop_anno: str = "epic_ddp_concat/pathology/table_pathology_impact_sample_summary_dop_anno.tsv"
    fname_darwin_path_heme_parse_bm_biopsy: str = (
        "epic_ddp_concat/pathology/pathology_heme_bm_biopsy.tsv"
    )
    fname_darwin_path_heme_parse_periph_blood: str = (
        "epic_ddp_concat/pathology/pathology_heme_periph_blood.tsv"
    )
    fname_path_pdl1: str = "epic_ddp_concat/pathology/pathology_pdl1_calls.tsv"
    fname_path_gleason: str = "epic_ddp_concat/pathology/pathology_gleason_calls.tsv"
    fname_path_mmr: str = "epic_ddp_concat/pathology/pathology_mmr_calls.tsv"

    ## cBioPortal file generation
    ### Timeline
    fname_path_sequencing_cbio_timeline: str = "epic_ddp_concat/pathology/table_timeline_sequencing.tsv"
    fname_path_specimen_surgery_cbio_timeline: str = (
        "epic_ddp_concat/pathology/table_timeline_specimen_surgery.tsv"
    )
    fname_path_gleason_cbio_timeline: str = (
        "epic_ddp_concat/pathology/table_timeline_gleason_scores.tsv"
    )
    fname_path_mmr_cbio_timeline: str = (
        "epic_ddp_concat/pathology/table_timeline_mmr_calls.tsv"
    )
    fname_path_pdl1_cbio_timeline: str = "epic_ddp_concat/pathology/table_timeline_pdl1_calls.tsv"
    fname_path_gleason_summary_patient: str = (
        "epic_ddp_concat/pathology/table_summary_gleason_patient.tsv"
    )
    fname_path_gleason_summary_sample: str = (
        "epic_ddp_concat/pathology/table_summary_gleason_sample.tsv"
    )
    fname_path_pdl1_summary_patient: str = "epic_ddp_concat/pathology/table_summary_pdl1_patient.tsv"
    fname_path_pdl1_summary_sample: str = "epic_ddp_concat/pathology/table_summary_pdl1_sample.tsv"

    col_pathology_id: str = "ACCESSION_NUMBER"

    ##############################################################################
    # RADIOLOGY REPORT derived files
    ##############################################################################
    # Radiology Filenames, raw and segmentations
    fname_radiology: str = (
        "epic_ddp_concat/radiology/radiology_report_segmentation/impact/ddp_radiology_reports.tsv"
    )
    fname_radiology_bkup: str = "epic_ddp_concat/radiology/radiology_report_segmentation/impact/intermediate_files_for_qc/ddp_radiology_reports_bkup.tsv"
    fname_radiology_update: str = "epic_ddp_concat/radiology/radiology_report_segmentation/impact/intermediate_files_for_qc/ddp_radiology_reports_update.tsv"
    fname_radiology_to_segment: str = "epic_ddp_concat/radiology/radiology_report_segmentation/impact/intermediate_files_for_qc/ddp_radiology_reports_for_segmentation.tsv"
    fname_radiology_metadata: str = "epic_ddp_concat/radiology/radiology_report_segmentation/impact/intermediate_files_for_qc/radiology_clean_annotations.tsv"
    fname_radiology_impression: str = "epic_ddp_concat/radiology/radiology_report_segmentation/impact/intermediate_files_for_qc/radiology_parse_impression.tsv"
    fname_radiology_findings: str = "epic_ddp_concat/radiology/radiology_report_segmentation/impact/intermediate_files_for_qc/radiology_parse_findings.tsv"
    fname_radiology_findings_long: str = "epic_ddp_concat/radiology/radiology_report_segmentation/impact/intermediate_files_for_qc/radiology_parse_findings_long.tsv"
    fname_radiology_headers = "epic_ddp_concat/radiology/radiology_report_segmentation/impact/intermediate_files_for_qc/radiology_parse_headers.tsv"
    fname_radiology_full_parsed: str = "epic_ddp_concat/radiology/radiology_report_segmentation/impact/ddp_radiology_reports_full_parsed.tsv"

    ## Tumor sites (ClinicalBERT-based method)
    fname_rad_prediction_all_accessions: str = "epic_ddp_concat/radiology/tumor_sites/impact/intermediate_files/radiology_accessions_for_pred_all.tsv"
    fname_radiology_tumor_site_pred: str = (
        "epic_ddp_concat/radiology/tumor_sites/impact/radiology_tumor_site_predictions_full.tsv"
    )
    fname_radiology_tumor_site_pred_summary: str = "epic_ddp_concat/radiology/tumor_sites/impact/radiology_tumor_site_predictions_full_summary.tsv"
    fname_rad_tumor_prediction_update: str = "epic_ddp_concat/radiology/tumor_sites/impact/intermediate_files/radiology_tumor_site_predictions_updated.tsv"
    fname_radiology_tumor_site_pred_combined: str = "epic_ddp_concat/radiology/tumor_sites/impact/intermediate_files/radiology_tumor_site_predictions_combined.tsv"
    fname_rad_rpts_for_prediction_tumor_sites: str = "epic_ddp_concat/radiology/tumor_sites/impact/intermediate_files/ddp_radiology_reports_for_prediction.tsv"
    fname_tumor_sites_timeline_cbio: str = (
        "/radiology/tumor_sites/impact/table_timeline_tumor_sites.tsv"
    )

    ## Progression (RoBERTa-based method)
    fname_progression_prediction_all_accessions: str = "epic_ddp_concat/radiology/progression/impact/intermediate_files/radiology_accessions_for_pred_all.tsv"
    fname_radiology_progression_pred_bkup: str = "epic_ddp_concat/radiology/progression/impact/intermediate_files/radiology_cancer_progression_predictions.tsv.bkup"
    fname_radiology_progression_pred: str = (
        "epic_ddp_concat/radiology/progression/impact/radiology_cancer_progression_predictions.tsv"
    )
    fname_progression_timeline_cbio: str = (
        "epic_ddp_concat/radiology/progression/impact/table_timeline_radiology_cancer_progression_predictions.tsv"
    )
    fname_rad_prog_prediction_update: str = "epic_ddp_concat/radiology/progression/impact/intermediate_files/radiology_progression_predictions_updated.tsv"
    fname_rad_prog_prediction_combined: str = "epic_ddp_concat/radiology/progression/impact/intermediate_files/radiology_cancer_progression_predictions_combined.tsv"
    fname_rad_rpts_for_prediction_progression: str = "epic_ddp_concat/radiology/progression/impact/intermediate_files/ddp_radiology_reports_for_prediction_progression.tsv"

    ## Training Labels
    ### Metastatic sites (GENIE)
    ### Progression (GENIE)
    fname_labels_genie_progression: str = "epic_ddp_concat/labels/progression/genie_lung_crc_breast_prostate_pancreas_progression_labels_20200923.tsv"

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
    fname_radiology_cancer_presence_predictions = "epic_ddp_concat/radiology/cancer_presence/impact/radiology_cancer_presence_prediction.tsv"
    fname_radiology_cancer_presence_timeline = "epic_ddp_concat/radiology/cancer_presence/impact/table_timeline_cancer_presence.tsv"

    ##############################################################################
    # TREATMENT (Medications, surgeries, RT) derived files
    ##############################################################################
    fname_meds_clean: str = "epic_ddp_concat/medications/table_medications_clean.tsv"
    fname_meds_intervals: str = "epic_ddp_concat/medications/table_medication_intervals.tsv"
    fname_meds_regimens: str = "epic_ddp_concat/medications/table_medication_regimens.tsv"

    fname_timeline_surg: str = "epic_ddp_concat/surgery/table_timeline_surgery.tsv"
    fname_timeline_rt: str = "epic_ddp_concat/radonc/table_timeline_radiation.tsv"
    fname_timeline_meds: str = "epic_ddp_concat/medications/table_timeline_medications.tsv"

    fname_tx_summary_patient: str = "epic_ddp_concat/medications/table_tx_summary_patient.tsv"
    fname_tx_summary_sample: str = "epic_ddp_concat/medications/table_tx_summary_sample.tsv"

    ##############################################################################
    # PRIOR MEDICATIONS PREDICTIONS
    ##############################################################################
    fname_prior_meds_predictions_prefix: str = "epic_ddp_concat/medications/prior_tx_inferences/prior_tx_inferences_impact"
    fname_prior_meds_predictions_comb: str = "epic_ddp_concat/medications/prior_tx_inferences/prior_tx_inferences_impact_combined.tsv"
    fname_prior_meds_predictions_comb_bkup: str = "epic_ddp_concat/medications/prior_tx_inferences/prior_tx_inferences_impact_combined.tsv.bkup"
    fname_prior_meds_predictions_timeline: str = "epic_ddp_concat/medications/prior_tx_inferences/prior_tx_inferences_impact_cbio_timeline.tsv"

    ##############################################################################
    # SDoH derived files
    ##############################################################################
    fname_comorbidities_index: str = "epic_ddp_concat/comorbidities/epic_ddp_comorbidities_index_summary.tsv"
    # fname_clindoc_smoking: str = "epic_ddp_concat/comorbidities/ddp_smoking_history.tsv"
    # fname_smoking_status: str = "epic_ddp_concat/comorbidities/smoking_status_predictions.tsv"
    #
    # fname_insurance_clean: str = "epic_ddp_concat/insurance/ddp_insurance_clean.tsv"
    # fname_insurance_summary: str = "epic_ddp_concat/insurance/ddp_insurance_summary.tsv"
    # fname_yost: str = "epic_ddp_concat/comorbidities/yost_index_results.tsv"
    #
    # fname_ecog_predictions: str = "epic_ddp_concat/clindoc/ecog/impact/ecog_kps_predictions.tsv"
    # fname_ecog_timeline_cbio: str = "epic_ddp_concat/clindoc/ecog/impact/table_timeline_ecog_kps.tsv"
    # fname_ecog_summary_cbio: str = "epic_ddp_concat/clindoc/ecog/impact/table_summary_ecog_patient.tsv"

