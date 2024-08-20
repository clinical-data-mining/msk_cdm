from ..loader import DatasetLoader

_loader = DatasetLoader()

def data_clinical_patient():
    return _loader._load_impact_data_clinical_patient()