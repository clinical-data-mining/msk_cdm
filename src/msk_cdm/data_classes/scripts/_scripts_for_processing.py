"""
_scripts_for_processing.py 

"""
import os
from dataclasses import dataclass


root_path: str = "/mind_data/cdm_repos/"


@dataclass
class ScriptsCbioportalFormatting:
    root_path_cbio_etl: str = os.path.join(root_path, "cdm-cbioportal-etl")

    ##############################################################################
    # cBioPortal summary and timeline scripts
    ##############################################################################
    # path_map: str = '/config/redcap_report_api_map_cdm.csv'
    # path_vars: str = '/config/redcap_variables_cdm.csv'
    # redcap_rpt_map: str = 'redcap_exports/cdm_cbioportal_codebook/Extraction_of_Clinical_Data_for_MSK-IMPACT_patients__MSK-MIND__redcap_report_mapping.tsv'
    # path_redcap_dest: str = 'redcap_exports/cdm_cbioportal_codebook'
    # config_redcap: str = '-t {{ params.TOKEN }} -u {{ params.URL }} -map {{ params.ID }} -vars {{params.VARS}} -dest {{ params.PATH }}  -minio {{ params.MINIO }}'

    script_cbio_timeline_deid_files: str = os.path.join(
        root_path_cbio_etl, "timeline/cbioportal_timeline_deid_files.py"
    )
    script_cbio_timeline_seq_spec: str = os.path.join(
        root_path_cbio_etl, "timeline/cbioportal_timeline_specimen.py"
    )
    # script_cbio_timeline_progression: str = os.path.join(root_path_cbio_etl, 'timeline/cbioportal_timeline_progression.py')    # 2023/10/18 Turned off
    script_cbio_timeline_disease_status: str = os.path.join(
        root_path_cbio_etl, "timeline/disease_status_cbioportal_timeline.py"
    )
    # script_cbio_timeline_cea_labs: str = os.path.join(root_path_cbio_etl, 'timeline/cbioportal_timeline_cea_labs.py')          # 2023/10/18 Turned off
    script_timeline_follow_up: str = os.path.join(
        root_path_cbio_etl, "timeline/cbioportal_timeline_follow_up.py"
    )
    script_summary_overall_survival: str = os.path.join(
        root_path_cbio_etl, "summary/cbioportal_overall_survival.py"
    )

    script_create_summary_templates: str = os.path.join(
        root_path_cbio_etl, "summary/cbioportal_template_generator.py "
    )
    script_summary_formatting: str = os.path.join(
        root_path_cbio_etl, "summary/wrapper_cbioportal_summary_creator.py"
    )
    script_copy_to_minio: str = os.path.join(
        root_path_cbio_etl, "utils/wrapper_cbioportal_copy_to_minio.py"
    )
    script_copy_to_cdsi_repo: str = os.path.join(
        root_path_cbio_etl, "utils/copy_cbio_files_to_automation_folder.py"
    )

    script_cbio_etl_git_fetch: str = os.path.join(
        root_path_cbio_etl, "git-tasks/git_fetch.sh "
    )
    script_cbio_etl_git_fetch_cdsi_copy: str = os.path.join(
        root_path_cbio_etl, "git-tasks/git_fetch_impact_pipeline.sh "
    )
    script_cbio_etl_git_push: str = os.path.join(
        root_path_cbio_etl, "git-tasks/git_push.sh "
    )
    script_cbio_etl_git_push_cdsi_copy: str = os.path.join(
        root_path_cbio_etl, "git-tasks/git_push_impact_pipeline.sh "
    )
    script_cbio_etl_git_fetch_impact: str = os.path.join(
        root_path_cbio_etl, "git-tasks/git_fetch_impact_ids.sh "
    )


@dataclass
class ScriptsComborbiditesDisparities:
    root_path_disparities: str = os.path.join(root_path, "cdm-disparities")

    ##############################################################################
    # SDoH derived files
    ##############################################################################
    script_comorbidities_index: str = os.path.join(
        root_path_disparities, "processing/process_cci.py"
    )
    script_smoking_status: str = os.path.join(
        root_path_disparities, "processing/process_smoking_history.py"
    )
    script_insurance: str = os.path.join(
        root_path_disparities, "processing/process_insurance.py"
    )
    script_yost: str = os.path.join(root_path_disparities, "processing/process_yost.py")


@dataclass
class ScriptsPathologySegmentation:
    ##############################################################################
    # Pathnames
    ##############################################################################
    root_path_pathology: str = os.path.join(root_path, "pathology_report_segmentation")

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
