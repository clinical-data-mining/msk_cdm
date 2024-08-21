# __init__.py

from .loader import DatasetLoader

# Create a global instance of DatasetLoader
_loader = DatasetLoader()

# Define functions to load datasets directly from the module
def authenticate(auth_file):
    _loader.authenticate(auth_file)
    print()

