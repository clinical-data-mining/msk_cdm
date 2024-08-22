from ...loader import DatasetLoader

_loader = DatasetLoader()

# Expose phi datasets
def load_demographics_idb():
    return _loader._load_phi_idb_demographics()

def load_radiology_reports_idb():
    return _loader._load_phi_idb_radiology_reports()

def load_pathology_reports_idb():
    return _loader._load_phi_idb_pathology_reports()

def load_surgeries_idb():
    return _loader._load_phi_idb_surgeries()

def load_diagnosis_idb():
    return _loader._load_phi_idb_diagnosis()

def load_medications_idb():
    return _loader._load_phi_idb_medications()

def load_radiation_idb():
    return _loader._load_phi_idb_radiation()

def load_interventional_radiology_idb():
    return _loader._load_phi_idb_interventional_radiology()