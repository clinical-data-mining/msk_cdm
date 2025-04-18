import pandas as pd
import importlib.resources

def _load_csv(filename: str) -> pd.DataFrame:
    # Load CSV using importlib.resources to make it work with installed packages
    with importlib.resources.files("msk_cdm.docs.codebook").joinpath(filename).open("r", encoding="utf-8") as f:
        return pd.read_csv(f)

def load_metadata_tab() -> pd.DataFrame:
    return _load_csv("CDM-Codebook - metadata.csv")

def load_tables_tab() -> pd.DataFrame:
    return _load_csv("CDM-Codebook - tables.csv")

def load_project_tab() -> pd.DataFrame:
    return _load_csv("CDM-Codebook - project.csv")

def load_nlp_performance_tab() -> pd.DataFrame:
    return _load_csv("CDM-Codebook - project.csv")
