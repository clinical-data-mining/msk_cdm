import yaml
import os

CONFIG_PATH = os.getenv("CDM_CONFIG_PATH", "config_cdm.yaml")

def load_config(path):
    if not os.path.exists(path):
        print(f"[CDM] No config file found at {path}. Skipping config load.")
        return {}  # Return empty config if file not found
    with open(path, "r") as f:
        return yaml.safe_load(f) or {}

_config = load_config(CONFIG_PATH)

class CDMProcessingVariables:
    pass

# Dynamically assign each config key as a class attribute
for key, value in _config.items():
    setattr(CDMProcessingVariables, key, value)
