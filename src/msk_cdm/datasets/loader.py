import os
import pandas as pd

from msk_cdm.minio import MinioAPI
from msk_cdm.data_classes.legacy import CDMProcessingVariables as c_path

# Global variable to track authentication status
_connnected = False
_obj_minio = None


path_minio_cbio = "cbioportal"
summary_p = "data_clinical_patient.txt"
summary_s = "data_clinical_sample.txt"
timeline_surg = "data_timeline_surgery.txt"
timeline_rt = "data_timeline_radiation.txt"
timeline_meds = "data_timeline_treatment.txt"
timeline_disease_status = "data_timeline_disease_status.txt"
timeline_dx_primary = "data_timeline_diagnosis.txt"
timeline_spec = "data_timeline_specimen.txt"
timeline_spec_surg = "data_timeline_specimen_surgery.txt"
timeline_gleason = "data_timeline_gleason.txt"
timeline_pdl1 = "data_timeline_pdl1.txt"
timeline_pathology_mmr = 'data_timeline_mmr.txt'
timeline_prior_meds = "data_timeline_prior_meds.txt"
timeline_tumor_sites = "data_timeline_tumor_sites.txt"
timeline_follow_up: str = "data_timeline_timeline_follow_up.txt"
timeline_progression: str = 'data_timeline_progression.txt'
timeline_cancer_presence: str = 'data_timeline_cancer_presence.txt'
timeline_ecog_kps: str = 'data_timeline_ecog_kps.txt'
##############################################################################
# Generated data files for cbioportal (MinIO)
##############################################################################
fname_summary_patient_minio: str = os.path.join(path_minio_cbio, summary_p)
fname_summary_sample_minio: str = os.path.join(path_minio_cbio, summary_s)
fname_save_surg_timeline_minio: str = os.path.join(path_minio_cbio, timeline_surg)
fname_save_rt_timeline_minio: str = os.path.join(path_minio_cbio, timeline_rt)
fname_save_meds_timeline_minio: str = os.path.join(path_minio_cbio, timeline_meds)
fname_save_dx_prim_timeline_minio: str = os.path.join(path_minio_cbio, timeline_dx_primary)
fname_save_spec_timeline_minio: str = os.path.join(path_minio_cbio, timeline_spec)
fname_save_spec_surg_timeline_minio: str = os.path.join(path_minio_cbio, timeline_spec_surg)
fname_save_timeline_gleason_minio: str = os.path.join(path_minio_cbio, timeline_gleason)
fname_save_timeline_pdl1_minio: str = os.path.join(path_minio_cbio, timeline_pdl1)
fname_save_timeline_prior_meds_minio: str = os.path.join(path_minio_cbio, timeline_prior_meds)
fname_save_timeline_tumor_sites_minio: str = os.path.join(path_minio_cbio, timeline_tumor_sites)
fname_save_timeline_follow_up_minio: str = os.path.join(path_minio_cbio, timeline_follow_up)

fname_save_timeline_progression_minio: str = os.path.join(path_minio_cbio, timeline_progression)
fname_save_timeline_pathology_mmr_minio: str = os.path.join(path_minio_cbio, timeline_pathology_mmr)
fname_save_timeline_cancer_presence_minio: str = os.path.join(path_minio_cbio, timeline_cancer_presence)
fname_save_timeline_ecog_minio: str = os.path.join(path_minio_cbio, timeline_ecog_kps)

# fname_summary_patient_minio_phi =
# fname_summary_sample_minio_phi
fname_save_surg_timeline_minio_phi = c_path.fname_timeline_surg
fname_save_rt_timeline_minio_phi = c_path.fname_timeline_rt
fname_save_meds_timeline_minio_phi = c_path.fname_timeline_meds
fname_save_dx_prim_timeline_minio_phi = c_path.fname_dx_timeline_prim
fname_save_spec_timeline_minio_phi = c_path.fname_path_sequencing_cbio_timeline
fname_save_spec_surg_timeline_minio_phi = c_path.fname_path_specimen_surgery_cbio_timeline
fname_save_timeline_gleason_minio_phi = c_path.fname_path_gleason_cbio_timeline
fname_save_timeline_pdl1_minio_phi = c_path.fname_path_pdl1_cbio_timeline
fname_save_timeline_prior_meds_minio_phi = c_path.fname_prior_meds_predictions_timeline
fname_save_timeline_tumor_sites_minio_phi: c_path.fname_tumor_sites_timeline_cbio
fname_save_timeline_follow_up_minio_phi = c_path.fname_timeline_fu

fname_save_timeline_progression_minio_phi = c_path.fname_progression_timeline_cbio
fname_save_timeline_pathology_mmr_minio_phi = c_path.fname_path_mmr_cbio_timeline
fname_save_timeline_cancer_presence_minio_phi = c_path.fname_radiology_cancer_presence_timeline
fname_save_timeline_ecog_minio_phi = c_path.fname_ecog_timeline_cbio

## Mapping files
fname_impact_id_mapping = c_path.fname_id_map
fname_impact_anchor_dates = c_path.fname_anchor_dates_reid

## Datasets from queries directly from IDB
fname_idb_demo = c_path.fname_demo


class DatasetLoader(object):
    # Consider refactoring below to not have so many functions
    # def __init__(self):
    #     self.datasets = {
    #         'impact': {
    #             'dataset1': self._load_impact_dataset1,
    #             'dataset2': self._load_impact_dataset2
    #             # Add more "impact" datasets here
    #         },
    #         'phi': {
    #             'dataset1': self._load_phi_dataset1,
    #             'dataset2': self._load_phi_dataset2
    #             # Add more "phi" datasets here
    #         }
    #     }

    def connect_to_db(self, auth_file):
        """Authenticate using a file containing credentials."""
        global _connnected, _obj_minio
        if not os.path.exists(auth_file):
            raise FileNotFoundError(f"Authentication file '{auth_file}' not found.")

        try:
            obj_minio = MinioAPI(fname_minio_env=auth_file)
            _obj_minio = obj_minio
            _connnected = True
        except:
            print("Cannot connect")

        return None

    def load_from_object_path(self, path_object, sep='\t'):
        self._ensure_connnected()
        obj = _obj_minio.load_obj(path_object=path_object)
        df = pd.read_csv(obj, sep=sep, low_memory=False)

        return df

    def close_connection(self):
        global _obj_minio
        return _obj_minio.close_connection()

    # Define each function corresponding to each file name (without .txt)
    def _load_impact_data_clinical_patient(self):
        return self.load_from_object_path(path_object=fname_summary_patient_minio)

    def _load_impact_data_clinical_sample(self):
        return self.load_from_object_path(path_object=fname_summary_sample_minio)

    def _load_impact_data_timeline_surgery(self):
        return self.load_from_object_path(path_object=fname_save_surg_timeline_minio)

    def _load_impact_data_timeline_radiation(self):
        return self.load_from_object_path(path_object=fname_save_rt_timeline_minio)

    def _load_impact_data_timeline_treatment(self):
        return self.load_from_object_path(path_object=fname_save_meds_timeline_minio)

    def _load_impact_data_timeline_diagnosis(self):
        return self.load_from_object_path(path_object=fname_save_dx_prim_timeline_minio)

    def _load_impact_data_timeline_specimen(self):
        return self.load_from_object_path(path_object=fname_save_spec_timeline_minio)

    def _load_impact_data_timeline_specimen_surgery(self):
        return self.load_from_object_path(path_object=fname_save_spec_surg_timeline_minio)

    def _load_impact_data_timeline_gleason(self):
        return self.load_from_object_path(path_object=fname_save_timeline_gleason_minio)

    def _load_impact_data_timeline_pdl1(self):
        return self.load_from_object_path(path_object=fname_save_timeline_pdl1_minio)

    def _load_impact_data_timeline_mmr(self):
        return self.load_from_object_path(path_object=fname_save_timeline_pathology_mmr_minio)

    def _load_impact_data_timeline_prior_meds(self):
        return self.load_from_object_path(path_object=fname_save_timeline_prior_meds_minio)

    def _load_impact_data_timeline_tumor_sites(self):
        return self.load_from_object_path(path_object=fname_save_timeline_tumor_sites_minio)

    def _load_impact_data_timeline_follow_up(self):
        return self.load_from_object_path(path_object=fname_save_timeline_follow_up_minio)

    def _load_impact_data_timeline_progression(self):
        return self.load_from_object_path(path_object=fname_save_timeline_progression_minio)

    def _load_impact_data_timeline_cancer_presence(self):
        return self.load_from_object_path(path_object=fname_save_timeline_cancer_presence_minio)

    def _load_impact_data_timeline_ecog_kps(self):
        return self.load_from_object_path(path_object=fname_save_timeline_ecog_minio)

    #### IMPACT timelines above, in the PHI data format
    def _load_phi_impact_data_timeline_surgery(self):
        return self.load_from_object_path(path_object=fname_save_surg_timeline_minio_phi)

    def _load_phi_impact_data_timeline_radiation(self):
        return self.load_from_object_path(path_object=fname_save_rt_timeline_minio_phi)

    def _load_phi_impact_data_timeline_treatment(self):
        return self.load_from_object_path(path_object=fname_save_meds_timeline_minio_phi)

    def _load_phi_impact_data_timeline_diagnosis(self):
        return self.load_from_object_path(path_object=fname_save_dx_prim_timeline_minio_phi)

    def _load_phi_impact_data_timeline_specimen(self):
        return self.load_from_object_path(path_object=fname_save_spec_timeline_minio_phi)

    def _load_phi_impact_data_timeline_specimen_surgery(self):
        return self.load_from_object_path(path_object=fname_save_spec_surg_timeline_minio_phi)

    def _load_phi_impact_data_timeline_gleason(self):
        return self.load_from_object_path(path_object=fname_save_timeline_gleason_minio_phi)

    def _load_phi_impact_data_timeline_pdl1(self):
        return self.load_from_object_path(path_object=fname_save_timeline_pdl1_minio_phi)

    def _load_phi_impact_data_timeline_prior_meds(self):
        return self.load_from_object_path(path_object=fname_save_timeline_prior_meds_minio_phi)

    def _load_phi_impact_data_timeline_tumor_sites(self):
        return self.load_from_object_path(path_object=fname_save_timeline_tumor_sites_minio_phi)

    def _load_phi_impact_data_timeline_follow_up(self):
        return self.load_from_object_path(path_object=fname_save_timeline_follow_up_minio_phi)

    def _load_phi_impact_data_timeline_progression(self):
        return self.load_from_object_path(path_object=fname_save_timeline_progression_minio_phi)

    def _load_phi_impact_data_timeline_mmr(self):
        return self.load_from_object_path(path_object=fname_save_timeline_pathology_mmr_minio_phi)

    def _load_phi_impact_data_timeline_cancer_presence(self):
        return self.load_from_object_path(path_object=fname_save_timeline_cancer_presence_minio_phi)

    def _load_phi_impact_data_timeline_ecog_kps(self):
        return self.load_from_object_path(path_object=fname_save_timeline_ecog_minio_phi)

    ###### Datasets for ID and interval mapping
    def _load_phi_impact_id_mapping(self):
        return self.load_from_object_path(path_object=fname_impact_id_mapping)

    def _load_phi_impact_anchor_dates(self):
        return self.load_from_object_path(path_object=fname_impact_anchor_dates)

    ###### Datasets directly from IDB queries
    def _load_phi_idb_demographics(self):
        return self.load_from_object_path(path_object=fname_idb_demo)

    def _ensure_connnected(self):
        global _connnected
        if not _connnected:
            raise PermissionError("Connection required. Please connect first.")


# Example usage:
# loader = DatasetLoader()
# loader.connect_to_db('path/to/auth_file.txt')
# iris_df = loader.load('iris')
# custom_df = loader.load_from_object_path('https://example.com/data.csv', 'data.csv')
