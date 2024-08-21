import os
import pandas as pd

from msk_cdm.minio import MinioAPI
from msk_cdm.data_classes.legacy import CDMProcessingVariables as c_var

# Global variable to track authentication status
_authenticated = False

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
fname_timeline_fu: str = "demographics/table_timeline_follow_up.tsv"
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



class DatasetLoader(object):

    def __init__(self):
        # self.datasets = {
        #     'impact': {
        #         'data_clinical_patient': ,
        #         'data_clinical_sample': self.load_from_object_path(path_object=fname_summary_sample_minio),
        #         'data_timeline_surgery': self.load_from_object_path(path_object=fname_save_surg_timeline_minio),
        #         'data_timeline_radiation': self.load_from_object_path(path_object=fname_save_rt_timeline_minio),
        #         # Add more "impact" datasets here
        #     },
        #     'phi': {
        #         'demographics_idb': self.load_from_object_path(path_object=c_var.fname_demo),
        #         'pathology_reports_idb': self.load_from_object_path(path_object=c_var.fname_pathology),
        #         'radiology_reports_idb': self.load_from_object_path(path_object=c_var.fname_radiology)
        #         # Add more "phi" datasets here
        #     }
        # }
        self._obj_minio = None

    def authenticate(self, auth_file):
        """Authenticate using a file containing credentials."""
        global _authenticated
        if not os.path.exists(auth_file):
            raise FileNotFoundError(f"Authentication file '{auth_file}' not found.")

        try:
            obj_minio = MinioAPI(fname_minio_env=auth_file)
            self._obj_minio = obj_minio
            _authenticated = True
        except:
            print("Cannot authenticate")

        return None

    def load_from_object_path(self, path_object, sep='\t'):
        self._ensure_authenticated()
        obj = self._obj_minio.load_obj(path_object=path_object)
        df = pd.read_csv(obj, sep=sep, low_memory=False)

        return df

    def _load_impact_data_clinical_patient(self):
        self._ensure_authenticated()
        return self.load_from_object_path(path_object=fname_summary_patient_minio)

    def _load_phi_demographics(self):
        self._ensure_authenticated()
        return self.load_from_object_path(path_object=c_var.fname_demo)

    def _ensure_authenticated(self):
        global _authenticated
        if not _authenticated:
            raise PermissionError("Authentication required. Please authenticate first.")
        else:
            print("Authenticated.")


# Example usage:
# loader = DatasetLoader()
# loader.authenticate('path/to/auth_file.txt')
# iris_df = loader.load('iris')
# custom_df = loader.fetch_from_object_path('https://example.com/data.csv', 'data.csv')