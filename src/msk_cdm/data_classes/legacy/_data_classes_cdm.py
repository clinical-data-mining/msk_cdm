"""
data_classes_cdm.py

"""

import os
from dataclasses import dataclass


root_path: str = "/gpfs/mindphidata/cdm_repos/github"


@dataclass
class CDMProcessingVariables:
    ##############################################################################
    # Pathnames
    ##############################################################################
    root_path_cdm_utils: str = os.path.join(root_path, "msk_cdm")
    root_path_treatments: str = os.path.join(root_path, "cdm-treatments")
    root_path_pathology: str = os.path.join(root_path, "pathology_report_segmentation")
    root_path_diagnosis: str = os.path.join(
        root_path, "diagnosis_event_abstraction_icd"
    )
    root_path_radiology: str = os.path.join(root_path, "radiology_met_prediction")
    root_path_progression: str = os.path.join(root_path, "progression-predict")
    root_path_sql: str = os.path.join(root_path, "cdm-idb-queries")
    root_path_disparities: str = os.path.join(root_path, "cdm-disparities")
    root_path_prior_meds: str = os.path.join(root_path, "prior-tx-identification")

    ##############################################################################
    # Utilities
    ##############################################################################
    script_redcap_pull: str = os.path.join(
        root_path_cdm_utils, "redcap/redcap_api_report_pull.py "
    )

    minio_env: str = "/gpfs/mindphidata/fongc2/minio_env.txt"
    venv: str = "/mind_data/cdm_repos/env_cdm/bin/python "

    xmap_met_sites_icd: str = os.path.join(
        root_path_cdm_utils, "organ_site_mappings/xwalk_met_site_to_billing_codes.csv"
    )
    xmap_met_sites_impact: str = os.path.join(
        root_path_cdm_utils,
        "organ_site_mappings/xwalk_met_site_to_impact_site_name.csv",
    )

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
    fname_cbio_sid: str = "/gpfs/mindphidata/cdm_repos/datahub/msk-impact/msk_solid_heme/data_clinical_sample.txt"
    study_id: str = "mskimpact"
    script_cbio_ids: str = os.path.join(
        root_path_cdm_utils, "cbioportal/cbioportal_api_pull_ids.py "
    )
    script_cbio_summary: str = os.path.join(
        root_path_diagnosis, "processing/run_sample_summary.py"
    )
    bash_cmd_cbio_ids: str = f"""
                           {venv} {script_cbio_ids} -t {{{{ params.token }}}} -dest {{{{ params.dest }}}} -s {{{{ params.study }}}} -m {{{{ params.minio }}}}
                       """
    fname_cbio_samples_clean: str = "cbioportal/mskimpact_ids_clean.tsv"
    fname_cbio_sample_summary_clean: str = "cbioportal/mskimpact_ids_summary.tsv"

    ##############################################################################
    # SQL for IDB queries
    ##############################################################################

    # idb_config = 'darwin_prod_legacy'     ## Use this for data dojo based IDB query scripts
    idb_config: str = os.path.join(root_path_sql, "config_ddp_query.txt")
    script_query_to_minio: str = os.path.join(root_path_sql, "run_query_to_minio.py")
    script_query_rrpts: str = os.path.join(root_path_sql, "radiology_reports/query_radiology_reports.py")

    ## General bash script
    bash_script_template = f""" {venv} {script_query_to_minio} --user {{{{ params.user }}}} --pw {{{{ params.pw }}}} --db2c {{{{ params.dbconfig }}}} --minio {{{{ params.minio }}}} --sql {{{{ params.sql }}}} --fsave {{{{ params.fsave }}}}  --fbkup {{{{ params.fbkup }}}} """

    bash_script_template_no_bkup = f""" {venv} {script_query_to_minio} --user {{{{ params.user }}}} --pw {{{{ params.pw }}}} --db2c {{{{ params.dbconfig }}}} --minio {{{{ params.minio }}}} --sql {{{{ params.sql }}}} --fsave {{{{ params.fsave }}}} """

    bash_script_template_with_mrns = f""" {venv} {script_query_to_minio} --user {{{{ params.user }}}} --pw {{{{ params.pw }}}} --db2c {{{{ params.dbconfig }}}} --minio {{{{ params.minio }}}} --sql {{{{ params.sql }}}} --fsave {{{{ params.fsave }}}}  --fbkup {{{{ params.fbkup }}}} --fmrn {{{{ params.fname_mrn_list }}}} --colmrn {{{{ params.col_mrn_sql }}}}  """

    bash_script_query_rrpts = f""" {venv} {script_query_rrpts} --user {{{{ params.user }}}} --pw {{{{ params.pw }}}}"""

    ## SQL files
    sql_demo: str = os.path.join(root_path_sql, "demographics", "demographics.sql")
    sql_surg: str = os.path.join(root_path_sql, "treatments/surgery.sql")
    sql_ir: str = os.path.join(root_path_sql, "treatments/ir.sql")
    sql_pathology: str = os.path.join(root_path_sql, "pathology_reports/pathology_report.sql")
    sql_pathology_accessions: str = os.path.join(
        root_path_sql, "pathology_reports/pathology_report_accessions.sql"
    )
    sql_radiology: str = os.path.join(root_path_sql, "radiology_reports/radiology_report.sql")
    sql_radiology_accessions: str = os.path.join(
        root_path_sql, "radiology_reports/radiology_report_accessions.sql"
    )
    sql_dx: str = os.path.join(root_path_sql, "diagnosis/diagnosis_codes.sql")
    sql_chemo: str = os.path.join(root_path_sql, "treatments/med_chemo.sql")
    sql_radonc: str = os.path.join(root_path_sql, "treatments/radiation.sql")
    sql_clindoc_fu_initial: str = os.path.join(
        root_path_sql, "clindoc/clindoc_initial_and_fu_notes.sql"
    )
    sql_comorbidities: str = os.path.join(
        root_path_sql, "comorbidities/comorbidities.sql"
    )
    sql_bmi: str = os.path.join(root_path_sql, "comorbidities/comorbidities_bmi.sql")
    sql_insurance: str = os.path.join(root_path_sql, "insurance/insurance.sql")
    sql_addresses: str = os.path.join(root_path_sql, "demographics/patient_addresses.sql")
    # sql_labs_myeloid: str = os.path.join(root_path_sql, 'labs/labs_myeloid.sql')
    sql_labs_antigen: str = os.path.join(
        root_path_sql, "labs/cancer_antigen_lab_results.sql"
    )

    ##############################################################################
    # Queried data from IDB
    ##############################################################################
    fname_demo: str = "demographics/ddp_demographics.tsv"
    fname_surg: str = "surgery/ddp_surgery.tsv"
    fname_dx: str = "diagnosis/ddp_dx.tsv"
    fname_meds: str = "medications/ddp_chemo.tsv"
    fname_rt: str = "radonc/ddp_radonc.tsv"
    fname_id_map: str = "id-mapping/ddp_id_mapping_pathology.tsv"
    fname_ir: str = "interventional-radiology/ddp_ir.tsv"
    fname_clindoc_fu_initial: str = "clindoc/ddp_clindoc_initial_and_fu_notes.tsv"
    fname_comorbidities: str = "comorbidities/ddp_comorbidities.tsv"
    fname_insurance: str = "insurance/ddp_insurance.tsv"
    col_mrn_sql_clindoc: str = "CDD_MRN"

    ##############################################################################
    # DIAGNOSIS TABLE derived files
    ##############################################################################
    script_clean_dx: str = os.path.join(
        root_path_diagnosis, "processing/darwin_diagnosis.py"
    )
    script_dx_summary: str = os.path.join(
        root_path_diagnosis, "processing/darwin_summary_diagnosis.py"
    )
    # script_met_summary: str = os.path.join(root_path_diagnosis, 'processing/run_metastatic_events.py')
    script_dx_timeline: str = os.path.join(
        root_path_diagnosis, "processing/dx_timeline.py"
    )
    script_met_site_summary: str = os.path.join(
        root_path_diagnosis, "processing/metastatic_site_summary.py"
    )

    # PATH LOCATION OF DATA FILES
    pathname_datahub: str = "/mind_data/fongc2/clinical-data-mining-datahub"

    ### Clean diagnosis table
    fname_dx_clean: str = "diagnosis/table_diagnosis_clean.tsv"

    ### Patient level summary table
    fname_dx_summary: str = (
        "diagnosis/table_dx_impact_summary.tsv"  # Table of impact sample processed
    )
    fname_met_site_summary: str = "diagnosis/table_met_site_summary.tsv"
    fname_dx_timeline_prim: str = "diagnosis/table_dx_timeline_primary.tsv"
    # fname_dx_timeline_met: str = 'diagnosis/table_dx_timeline_met.tsv'
    # fname_dx_timeline_ln: str = 'diagnosis/table_dx_timeline_ln.tsv'

    fname_demo: str = "demographics/ddp_demographics.tsv"
    fname_pid: str = "id-mapping/ddp_id_mapping_pathology.tsv"
    fname_path_summary: str = (
        "pathology/table_pathology_impact_sample_summary_dop_anno.tsv"
    )

    ##############################################################################
    # PATHOLOGY REPORT derived files
    ##############################################################################
    script_clean_path: str = os.path.join(root_path_pathology, "darwin_pathology.py")
    script_path_id_mapping: str = os.path.join(
        root_path_pathology, "annotations/pathology_id_mapping.py"
    )
    script_seg_path_surg: str = os.path.join(
        root_path_pathology, "segmentation/pathology_parse_surgical.py"
    )
    script_seg_path_mole: str = os.path.join(
        root_path_pathology, "segmentation/pathology_parse_molecular.py"
    )
    script_seg_path_heme: str = os.path.join(
        root_path_pathology, "segmentation/pathology_parse_heme.py"
    )
    script_pathology_heme_sections: str = os.path.join(
        root_path_pathology, "annotations/pathology_parse_heme_section_bm_biopsy.py"
    )
    script_pathology_heme_sections_periph_blood: str = os.path.join(
        root_path_pathology, "annotations/pathology_parse_heme_section_periph_blood.py"
    )
    script_seg_path_spec_sub: str = os.path.join(
        root_path_pathology, "segmentation/pathology_parse_specimen_submitted.py"
    )
    script_seg_path_surg_spec: str = os.path.join(
        root_path_pathology, "segmentation/pathology_parsing_surgical_specimens.py"
    )
    script_path_accessions: str = os.path.join(
        root_path_pathology, "annotations/pathology_extract_accession.py"
    )
    script_path_dop: str = os.path.join(
        root_path_pathology, "annotations/pathology_extract_dop.py"
    )
    script_path_synoptic: str = os.path.join(
        root_path_pathology, "annotations/pathology_synoptic_logistic_model.py"
    )
    script_combine_accession_dop: str = os.path.join(
        root_path_pathology, "annotations/pathology_extract_dop_impact_wrapper.py"
    )
    script_pathology_summary: str = os.path.join(
        root_path_pathology, "annotations/pathology_impact_summary_dop_annotator.py"
    )
    script_pathology_pdl1: str = os.path.join(
        root_path_pathology, "annotations/pathology_extract_pdl1.py"
    )
    script_pathology_gleason: str = os.path.join(
        root_path_pathology, "annotations/pathology_extract_gleason.py"
    )
    script_pathology_mmr: str = os.path.join(
        root_path_pathology, "annotations/pathology_extract_mmr.py"
    )

    ## cBioPortal file generation scripts
    ### Timeline scripts
    script_pathology_sequencing_timeline: str = os.path.join(
        root_path_pathology, "pipeline/cbio_timeline_sequencing.py"
    )
    script_pathology_specimen_timeline: str = os.path.join(
        root_path_pathology, "pipeline/cbio_timeline_specimen.py"
    )
    script_pathology_pdl1_timeline: str = os.path.join(
        root_path_pathology, "pipeline/cbio_timeline_pdl1.py"
    )
    script_pathology_gleason_timeline: str = os.path.join(
        root_path_pathology, "pipeline/cbio_timeline_gleason.py"
    )
    # script_pathology_mmr_timeline: str = os.path.join(root_path_pathology, 'annotations/cbio_timeline_mmr.py')

    ### Patient and sample summary data
    script_pathology_gleason_summary: str = os.path.join(
        root_path_pathology, "pipeline/cbio_gleason_summary.py"
    )

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
    ## Segmentation scripts
    script_radiology_etl: str = os.path.join(
        root_path_radiology, "segmentation/run_radiology_segmentation.py "
    )
    script_radiology_features: str = os.path.join(
        root_path_pathology, "/features/run_feature_extraction.py "
    )

    ## Tumor site prediction scripts
    script_tumor_site_prediction_build: str = os.path.join(
        root_path_radiology, "pipeline/predictions/radiology_tumor_site_pred.py "
    )
    script_bash_predict_tumor_site: str = os.path.join(
        root_path_radiology, "condor/run_infer_met_sites.sh "
    )
    script_tumor_site_prediction_merge: str = os.path.join(
        root_path_radiology, "pipeline/predictions/combine_results.py "
    )
    script_tumor_site_prediction_add_metadata: str = os.path.join(
        root_path_radiology, "pipeline/predictions/add_metadata.py "
    )
    script_tumor_site_prediction_cbio_timeline: str = os.path.join(
        root_path_radiology, "pipeline/timeline_cbio_tumor_sites.py "
    )
    script_tumor_site_prediction_cbio_summary: str = os.path.join(
        root_path_radiology, "pipeline/tumor_site_prediction_summary.py "
    )

    ## Progression prediction scripts
    script_progression_prediction_build: str = os.path.join(
        root_path_progression,
        "pipeline/predictions/cmd_line_radiology_progression_pred.py ",
    )
    script_progression_prediction_merge: str = os.path.join(
        root_path_progression, "pipeline/predictions/combine_results.py "
    )
    script_progression_prediction_add_metadata: str = os.path.join(
        root_path_progression, "pipeline/predictions/add_metadata.py "
    )
    script_bash_predict_progression: str = os.path.join(
        root_path_progression, "condor/cmd_run_condor_infer.sh "
    )

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

    # # Generated feature data
    # fname_rad_embedding: str = (
    #     "/mind_data/fongc2/radiology_met_prediction/assets/clinicalbert_w2v.txt"
    # )

    ## Word embeddings method
    fname_rad_met_feature_impressions: str = (
        "/radiology/radiology_features_embedding_avg_impressions.csv"
    )
    fname_rad_met_feature_findings_parsed: str = (
        "/radiology/radiology_features_embedding_avg_findings_parsed.csv"
    )
    fname_rad_met_feature_findings_all: str = (
        "/radiology/radiology_features_embedding_avg_findings_all.csv"
    )

    ## Tumor sites (ClinicalBERT-based method)
    fname_rad_prediction_all_accessions: str = "/radiology/tumor_sites/impact/intermediate_files/radiology_accessions_for_pred_all.tsv"
    fname_radiology_tumor_site_pred: str = (
        "/radiology/tumor_sites/impact/radiology_tumor_site_predictions_full.tsv"
    )
    fname_radiology_tumor_site_pred_summary: str = "/radiology/tumor_sites/impact/radiology_tumor_site_predictions_full_summary.tsv"
    fname_rad_tumor_prediction_update: str = "/radiology/tumor_sites/impact/intermediate_files/radiology_tumor_site_predictions_updated.tsv"
    fname_radiology_tumor_site_pred_combined: str = "/radiology/tumor_sites/impact/intermediate_files/radiology_tumor_site_predictions_combined.tsv"
    fname_rad_rpts_for_prediction_tumor_sites: str = "/radiology/tumor_sites/impact/intermediate_files/ddp_radiology_reports_for_prediction.tsv"
    log_fname_template_tumor_sites: str = (
        "/gpfs/mindphidata/fongc2/github/radiology_met_prediction/condor/logs/log_infer.txt"
    )
    fname_tumor_sites_timeline_cbio: str = (
        "/radiology/tumor_sites/impact/table_timeline_tumor_sites.tsv"
    )

    ## Progression (RoBERTa-based method)
    fname_progression_prediction_all_accessions: str = "/radiology/progression/impact/intermediate_files/radiology_accessions_for_pred_all.tsv"
    fname_radiology_progression_pred_bkup: str = "/radiology/progression/impact/intermediate_files/radiology_cancer_progression_predictions.tsv.bkup"
    fname_radiology_progression_pred: str = (
        "/radiology/progression/impact/radiology_cancer_progression_predictions.tsv"
    )
    fname_rad_prog_prediction_update: str = "/radiology/progression/impact/intermediate_files/radiology_progression_predictions_updated.tsv"
    fname_rad_prog_prediction_combined: str = "/radiology/progression/impact/intermediate_files/radiology_cancer_progression_predictions_combined.tsv"
    fname_rad_rpts_for_prediction_progression: str = "/radiology/progression/impact/intermediate_files/ddp_radiology_reports_for_prediction_progression.tsv"
    log_fname_template_progression: str = (
        "/gpfs/mindphidata/fongc2/github/progression-predict/condor/logs/log_infer.txt"
    )

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

    ##############################################################################
    # TREATMENT (Medications, surgeries, RT) derived files
    ##############################################################################
    script_meds_clean: str = os.path.join(
        root_path_treatments, "processing/medications_table_cleaning.py"
    )
    script_meds_to_regimens: str = os.path.join(
        root_path_treatments, "processing/run_chemo_to_regimens.py"
    )
    script_meds_timeline: str = os.path.join(
        root_path_treatments, "processing/medications_timeline.py"
    )
    script_surgery_timeline: str = os.path.join(
        root_path_treatments, "processing/surgery_timeline.py"
    )
    script_radiation_timeline: str = os.path.join(
        root_path_treatments, "processing/radiation_timeline.py"
    )

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
    script_prior_meds_timeline: str = os.path.join(
        root_path_prior_meds, "pipeline/prior_medications_timeline.py"
    )
    script_prior_meds_fix_output: str = os.path.join(
        root_path_prior_meds, "pipeline/fix_prior_meds.py"
    )

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
    script_comorbidities_index: str = os.path.join(
        root_path_disparities, "processing/process_cci.py"
    )
    fname_comorbidities_index: str = "comorbidities/ddp_comorbidities_index_summary.tsv"

    script_smoking_status: str = os.path.join(
        root_path_disparities, "processing/process_smoking_history.py"
    )
    fname_clindoc_smoking: str = "comorbidities/ddp_smoking_history.tsv"
    fname_smoking_status: str = "comorbidities/smoking_status_predictions.tsv"

    script_insurance: str = os.path.join(
        root_path_disparities, "processing/process_insurance.py"
    )
    fname_insurance_clean: str = "insurance/ddp_insurance_clean.tsv"
    fname_insurance_summary: str = "insurance/ddp_insurance_summary.tsv"

    script_yost: str = os.path.join(root_path_disparities, "processing/process_yost.py")
    fname_yost: str = "comorbidities/yost_index_results.tsv"


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
