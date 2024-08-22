from ..loader import DatasetLoader

_loader = DatasetLoader()

def load_data_clinical_patient():
    return _loader._load_impact_data_clinical_patient()

def load_data_clinical_sample():
    return _loader._load_impact_data_clinical_sample()

def load_data_timeline_surgery():
    return _loader._load_impact_data_timeline_surgery()

def load_data_timeline_radiation():
    return _loader._load_impact_data_timeline_radiation()

def load_data_timeline_treatment():
    return _loader._load_impact_data_timeline_treatment()

def load_data_timeline_diagnosis():
    return _loader._load_impact_data_timeline_diagnosis()

def load_data_timeline_specimen():
    return _loader._load_impact_data_timeline_specimen()

def load_data_timeline_specimen_surgery():
    return _loader._load_impact_data_timeline_specimen_surgery()

def load_data_timeline_gleason():
    return _loader._load_impact_data_timeline_gleason()

def load_data_timeline_pdl1():
    return _loader._load_impact_data_timeline_pdl1()

def load_data_timeline_mmr():
    return _loader._load_impact_data_timeline_mmr()

def load_data_timeline_prior_meds():
    return _loader._load_impact_data_timeline_prior_meds()

def load_data_timeline_tumor_sites():
    return _loader._load_impact_data_timeline_tumor_sites()

def load_data_timeline_follow_up():
    return _loader._load_impact_data_timeline_follow_up()

def load_data_timeline_progression():
    return _loader._load_impact_data_timeline_progression()

def load_data_timeline_cancer_presence():
    return _loader._load_impact_data_timeline_cancer_presence()

def load_data_timeline_ecog_kps():
    return _loader._load_impact_data_timeline_ecog_kps()
