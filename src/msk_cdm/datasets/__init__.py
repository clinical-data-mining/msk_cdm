# __init__.py

from .loader import DatasetLoader

# Create a global instance of DatasetLoader
_loader = DatasetLoader()

# Define functions to load datasets directly from the module
def connect_to_db(auth_file):
    _loader.connect_to_db(auth_file=auth_file)

