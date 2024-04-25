"""
_constants.py

"""

import os
from dataclasses import dataclass


@dataclass
class ConstantsPathologySegmentation:
    col_pathology_id: str = "ACCESSION_NUMBER"
