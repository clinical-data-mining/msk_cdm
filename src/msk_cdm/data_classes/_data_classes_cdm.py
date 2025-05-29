import yaml
import os

CONFIG_PATH = os.getenv("CDM_CONFIG_PATH", "config_cdm.yaml")

def load_config(path):
    try:
        with open(path, "r") as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Config file not found at path: {path}")

_config = load_config(CONFIG_PATH)

class CDMProcessingVariables:
    pass

# Dynamically assign each config key as a class attribute
for key, value in _config.items():
    setattr(CDMProcessingVariables, key, value)
