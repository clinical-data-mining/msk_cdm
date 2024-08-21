from ..loader import DatasetLoader

_loader = DatasetLoader()

def data_clinical_patient():
    return _loader._load_impact_data_clinical_patient()

def data_clinical_sample():
    return _loader._load_impact_data_clinical_sample()

def data_timeline_surgery():
    return _loader._load_impact_data_timeline_surgery()

def data_timeline_radiation():
    return _loader._load_impact_data_timeline_radiation()

def data_timeline_treatment():
    return _loader._load_impact_data_timeline_treatment()

def data_timeline_diagnosis():
    return _loader._load_impact_data_timeline_diagnosis()

def data_timeline_specimen():
    return _loader._load_impact_data_timeline_specimen()

def data_timeline_specimen_surgery():
    return _loader._load_impact_data_timeline_specimen_surgery()

def data_timeline_gleason():
    return _loader._load_impact_data_timeline_gleason()

def data_timeline_pdl1():
    return _loader._load_impact_data_timeline_pdl1()

def data_timeline_mmr():
    return _loader._load_impact_data_timeline_mmr()

def data_timeline_prior_meds():
    return _loader._load_impact_data_timeline_prior_meds()

def data_timeline_tumor_sites():
    return _loader._load_impact_data_timeline_tumor_sites()

def data_timeline_follow_up():
    return _loader._load_impact_data_timeline_follow_up()

def data_timeline_progression():
    return _loader._load_impact_data_timeline_progression()

def data_timeline_cancer_presence():
    return _loader._load_impact_data_timeline_cancer_presence()

def data_timeline_ecog_kps():
    return _loader._load_impact_data_timeline_ecog_kps()
