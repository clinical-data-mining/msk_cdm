# __init__.py

from .loader import DatasetLoader

# Create a global instance of DatasetLoader
_loader = DatasetLoader()

# Define functions to load datasets directly from the module
def authenticate(auth_file):
    _loader.authenticate(auth_file)

# Impact datasets
impact_data_clinical_patient = _loader._load_impact_data_clinical_patient
# impact_dataset2 = _loader.load_impact_dataset2

# Phi datasets
phi_demographics = _loader._load_phi_demographics
# phi_dataset2 = _loader.load_phi_dataset2