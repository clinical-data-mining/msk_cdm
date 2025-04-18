import pandas as pd
import importlib.resources
from msk_cdm.data_classes.epic_ddp_concat import CDMProcessingVariables

_vars = CDMProcessingVariables()


def load_codebook(name: str) -> pd.DataFrame:
    """
    Load a codebook CSV by short name.
    """
    if name not in _vars.codebook_file_map:
        raise ValueError(f"Unknown codebook name: '{name}'. Must be one of {list(_vars.codebook_file_map)}")

    filename = _vars.codebook_file_map[name]
    with importlib.resources.files("msk_cdm.data.codebook").joinpath(filename).open("r", encoding="utf-8") as f:
        return pd.read_csv(f)
