from ...loader import DatasetLoader

_loader = DatasetLoader()

# Expose phi datasets
def load_demographics_idb():
    return _loader._load_phi_idb_demographics()
# dataset2 = _loader.load_phi_dataset2