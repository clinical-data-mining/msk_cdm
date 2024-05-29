"""
_data_locations.py

"""

import os
from dataclasses import dataclass


root_path: str = "/mind_data/cdm_repos/"


@dataclass
class DataLocationsPathologySegmentation:
    ##############################################################################
    # Pathnames
    ##############################################################################
    root_path_pathology: str = os.path.join(root_path, "pathology_report_segmentation")

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
    fname_path_pdl1_cbio_timeline: str = "pathology/table_timeline_pdl1_calls.tsv"
    fname_path_gleason_summary_patient: str = (
        "pathology/table_summary_gleason_patient.tsv"
    )
    fname_path_gleason_summary_sample: str = (
        "pathology/table_summary_gleason_sample.tsv"
    )
    fname_path_pdl1_summary_patient: str = "pathology/table_summary_pdl1_patient.tsv"
    fname_path_pdl1_summary_sample: str = "pathology/table_summary_pdl1_sample.tsv"


@dataclass
class DataLocationsDisparities:
    root_path_cbio_etl: str = os.path.join(root_path, "cdm-cbioportal-etl")
    ##############################################################################
    # SDoH derived files
    ##############################################################################
    fname_comorbidities_index: str = "comorbidities/ddp_comorbidities_index_summary.tsv"
    fname_clindoc_smoking: str = "comorbidities/ddp_smoking_history.tsv"
    fname_smoking_status: str = "comorbidities/smoking_status_predictions.tsv"
    fname_insurance_clean: str = "insurance/ddp_insurance_clean.tsv"
    fname_insurance_summary: str = "insurance/ddp_insurance_summary.tsv"
    fname_yost: str = "comorbidities/yost_index_results.tsv"


@dataclass
class DataLocationsCbioportalFormatting:
    root_path_cbio_etl: str = os.path.join(root_path, "cdm-cbioportal-etl")

    ##############################################################################
    # cBioPortal setup files
    ##############################################################################
    # path_datahub_testing: str = '/mind_data/cdm_repos/datahubs/cdm/msk-chord/'
    # template_summary_p: str = 'template/data_clinical_patient_template_cdsi.txt'
    # template_summary_s: str = 'template/data_clinical_sample_template_cdsi.txt'
    # fname_p_sum_template: str = os.path.join(path_datahub, template_summary_p)
    # fname_s_sum_template: str = os.path.join(path_datahub, template_summary_s)

    # For IMPACT transition with cbioportal backend team
    path_datahub: str = "/mind_data/cdm_repos/datahubs/cdm/msk-chord/"
    fname_cbio_header_template_p: str = (
        "cbioportal/cbioportal_summary_header_patient.tsv"
    )
    fname_cbio_header_template_s: str = (
        "cbioportal/cbioportal_summary_header_sample.tsv"
    )
    fname_p_sum_template_cdsi: str = (
        "cbioportal/intermediate_files/data_clinical_patient_template_cdsi.txt"
    )
    fname_s_sum_template_cdsi: str = (
        "cbioportal/intermediate_files/data_clinical_sample_template_cdsi.txt"
    )

    ##############################################################################
    # Generated data files for cbioportal (Datahub)
    ##############################################################################
    summary_p = "data_clinical_patient.txt"
    summary_s = "data_clinical_sample.txt"
    timeline_surg = "data_timeline_surgery.txt"
    timeline_rt = "data_timeline_radiation.txt"
    timeline_meds = "data_timeline_treatment.txt"
    timeline_disease_status = "data_timeline_disease_status.txt"
    timeline_dx_primary = "data_timeline_diagnosis.txt"
    # timeline_dx_met = 'data_timeline_indication_of_mets.txt'         # 2023/10/18 Turned off
    # timeline_dx_ln = 'data_timeline_ln.txt'         # 2023/10/18 Turned off
    timeline_spec = "data_timeline_specimen.txt"
    timeline_spec_surg = "data_timeline_specimen_surgery.txt"
    # timeline_progression = 'data_timeline_progression.txt'         # 2023/10/18 Turned off
    # timeline_cea = 'data_timeline_cea.txt'         # 2023/10/18 Turned off
    timeline_gleason = "data_timeline_gleason.txt"
    timeline_pdl1 = "data_timeline_pdl1.txt"
    timeline_prior_meds = "data_timeline_prior_meds.txt"
    timeline_tumor_sites = "data_timeline_tumor_sites.txt"

    fname_timeline_fu: str = "demographics/table_timeline_follow_up.tsv"
    timeline_follow_up: str = "data_timeline_timeline_follow_up.txt"

    fname_summary_patient: str = os.path.join(path_datahub, summary_p)
    fname_summary_sample: str = os.path.join(path_datahub, summary_s)
    fname_save_surg_timeline: str = os.path.join(path_datahub, timeline_surg)
    fname_save_rt_timeline: str = os.path.join(path_datahub, timeline_rt)
    fname_save_meds_timeline: str = os.path.join(path_datahub, timeline_meds)
    # fname_save_disease_status_timeline: str = os.path.join(path_datahub, timeline_disease_status)         # 2023/10/18 Turned off
    fname_save_dx_prim_timeline: str = os.path.join(path_datahub, timeline_dx_primary)
    # fname_save_dx_met_timeline: str = os.path.join(path_datahub, timeline_dx_met)         # 2023/10/18 Turned off
    # fname_save_dx_ln_timeline: str = os.path.join(path_datahub, timeline_dx_ln)         # 2023/10/18 Turned off
    fname_save_spec_timeline: str = os.path.join(path_datahub, timeline_spec)
    fname_save_spec_surg_timeline: str = os.path.join(path_datahub, timeline_spec_surg)
    # fname_save_progression: str = os.path.join(path_datahub, timeline_progression)         # 2023/10/18 Turned off
    # fname_save_labs_cea: str = os.path.join(path_datahub, timeline_cea)         # 2023/10/18 Turned off
    fname_save_timeline_gleason: str = os.path.join(path_datahub, timeline_gleason)
    fname_save_timeline_pdl1: str = os.path.join(path_datahub, timeline_pdl1)
    fname_save_timeline_prior_meds: str = os.path.join(
        path_datahub, timeline_prior_meds
    )
    fname_save_timeline_tumor_sites: str = os.path.join(
        path_datahub, timeline_tumor_sites
    )
    fname_save_timeline_follow_up: str = os.path.join(path_datahub, timeline_follow_up)

    ##############################################################################
    # Generated data files for cbioportal (MinIO)
    ##############################################################################
    path_minio_cbio = "cbioportal"
    fname_summary_patient_minio: str = os.path.join(path_minio_cbio, summary_p)
    fname_summary_sample_minio: str = os.path.join(path_minio_cbio, summary_s)
    fname_save_surg_timeline_minio: str = os.path.join(path_minio_cbio, timeline_surg)
    fname_save_rt_timeline_minio: str = os.path.join(path_minio_cbio, timeline_rt)
    fname_save_meds_timeline_minio: str = os.path.join(path_minio_cbio, timeline_meds)
    # fname_save_disease_status_timeline_minio: str = os.path.join(path_minio_cbio, timeline_disease_status)         # 2023/10/18 Turned off
    fname_save_dx_prim_timeline_minio: str = os.path.join(
        path_minio_cbio, timeline_dx_primary
    )
    # fname_save_dx_met_timeline_minio: str = os.path.join(path_minio_cbio, timeline_dx_met)         # 2023/10/18 Turned off
    # fname_save_dx_ln_timeline_minio: str = os.path.join(path_minio_cbio, timeline_dx_ln)         # 2023/10/18 Turned off
    fname_save_spec_timeline_minio: str = os.path.join(path_minio_cbio, timeline_spec)
    fname_save_spec_surg_timeline_minio: str = os.path.join(
        path_minio_cbio, timeline_spec_surg
    )
    # fname_save_progression_minio: str = os.path.join(path_minio_cbio, timeline_progression)         # 2023/10/18 Turned off
    # fname_save_labs_cea_minio: str = os.path.join(path_minio_cbio, timeline_cea)         # 2023/10/18 Turned off
    fname_save_timeline_gleason_minio: str = os.path.join(
        path_minio_cbio, timeline_gleason
    )
    fname_save_timeline_pdl1_minio: str = os.path.join(path_minio_cbio, timeline_pdl1)
    fname_save_timeline_prior_meds_minio: str = os.path.join(
        path_minio_cbio, timeline_prior_meds
    )
    fname_save_timeline_tumor_sites_minio: str = os.path.join(
        path_minio_cbio, timeline_tumor_sites
    )
    fname_save_timeline_follow_up_minio: str = os.path.join(
        path_minio_cbio, timeline_follow_up
    )


@dataclass
class DataLocationsRedcapLabels:
    """
    Configuration files used for pulling data from the Redcap API
    """

    # Redcap: AI/ML IMPACT Curation Efforts
    fname_api_keys_ai_ml_impact: str = "config/redcap_report_api_map_ai_ml_impact.csv"
    path_vars_file_ai_ml_impact: str = "config/redcap_variables_ai_ml_impact.csv"

    ##############################################################################
    # GENIE BPC Redcap Reports - Tumor Sites
    ##############################################################################
    fname_genie_rc_met_sites_breast: str = "redcap_exports/genie_bpc_breast/19-368__GENIE_BPC_-_BREAST_Cohort_Imaging_Metastatic_Events.tsv"
    fname_genie_rc_met_sites_crc: str = "redcap_exports/genie_bpc_crc/19-368__GENIE_BPC_-_CRC_Production_Cohort_Imaging_Metastatic_Events.tsv"
    fname_genie_rc_met_sites_lung: str = "redcap_exports/genie_bpc_lung/MED19-213__Genie_BPC_Lung_Production_Imaging_Metastatic_Events.tsv"
    fname_genie_rc_met_sites_lung2: str = "redcap_exports/genie_bpc_lung_additional/19-368__Genie_BPC_Lung_Cohort_Additional_Data_Imaging_Metastatic_Events.tsv"
    fname_genie_rc_met_sites_pancreas: str = "redcap_exports/genie_bpc_pancreas/19-368__GENIE_BPC_-_Pancreas_Cohort_Imaging_Metastatic_Events.tsv"
    fname_genie_rc_met_sites_prostate: str = "redcap_exports/genie_bpc_prostate/19-368__GENIE_BPC_-_Prostate_Cohort_Imaging_Metastatic_Events.tsv"

    ##############################################################################
    # AI/ML Curation Efforts
    ##############################################################################
    fname_ai_ml_curation_toxicities: str = "redcap_exports/ai_ml_impact/AI_ML_IMPACT_Curation_Efforts_Treatments_and_toxicities.tsv"
