from ...loader import DatasetLoader

_loader = DatasetLoader()

def load_data_timeline_surgery_phi():
    return _loader._load_phi_impact_data_timeline_surgery()

def load_data_timeline_radiation_phi():
    return _loader._load_phi_impact_data_timeline_radiation()

def load_data_timeline_treatment_phi():
    return _loader._load_phi_impact_data_timeline_treatment()

def load_data_timeline_diagnosis_phi():
    return _loader._load_phi_impact_data_timeline_diagnosis()

def load_data_timeline_specimen_phi():
    return _loader._load_phi_impact_data_timeline_specimen()

def load_data_timeline_specimen_surgery_phi():
    return _loader._load_phi_impact_data_timeline_specimen_surgery()

def load_data_timeline_gleason_phi():
    return _loader._load_phi_impact_data_timeline_gleason()

def load_data_timeline_pdl1_phi():
    return _loader._load_phi_impact_data_timeline_pdl1()

def load_data_timeline_prior_meds_phi():
    return _loader._load_phi_impact_data_timeline_prior_meds()

def load_data_timeline_tumor_sites_phi():
    return _loader._load_phi_impact_data_timeline_tumor_sites()

def load_data_timeline_follow_up_phi():
    return _loader._load_phi_impact_data_timeline_follow_up()

def load_data_timeline_progression_phi():
    return _loader._load_phi_impact_data_timeline_progression()

def load_data_timeline_mmr_phi():
    return _loader._load_phi_impact_data_timeline_mmr()

def load_data_timeline_cancer_presence_phi():
    return _loader._load_phi_impact_data_timeline_cancer_presence()

def load_data_timeline_ecog_kps_phi():
    return _loader._load_phi_impact_data_timeline_ecog_kps()

def load_data_id_mapping_phi():
    return _loader._load_phi_impact_id_mapping()

def load_data_anchor_dates_phi():
    return _loader._load_phi_impact_anchor_dates()
