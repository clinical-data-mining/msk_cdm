from datetime import date
from pathlib import Path
from typing import Optional

from pydantic import BaseModel, ConfigDict, model_validator


SAVE_FNAME = "cdm_metadata.json"


class DatasetMetadata(BaseModel):
    model_config = ConfigDict(extra="allow")

    ####################################################################################
    # Standard fields
    ####################################################################################

    # Unique human-readable name for the project this dataset is used for (like the name
    # of a model, e.g. "site-of-met"), shared across different/comparable versions of
    # data for the same general system.
    cdm_project_id: str

    # Number of documents/record in dataset (the exact semantics of this number may
    # vary based on the project).
    dataset_size: int

    # Human-readable description of the data to help interpret/understand
    description: Optional[str] = None

    # Date of oldest record in training set.
    # Can be "YYYY-MM-DD", datetime.date, unixtime in float/int.
    oldest_train_record_date: Optional[date] = None

    # Date of most recent record in training set.
    # Can be "YYYY-MM-DD", datetime.date, unixtime in float/int.
    newest_train_record_date: Optional[date] = None

    ####################################################################################
    # Serialization/deserialization
    ####################################################################################

    def as_json(self, indent=None):
        return self.model_dump_json(indent=indent)

    def as_dict(self):
        return self.model_dump()

    def save_to_dir(self, output_dir):
        # TODO check/warn/crash on already-existing metadata file
        (Path(output_dir) / SAVE_FNAME).write_text(self.as_json(indent=2))

    @classmethod
    def from_dir(cls, input_dir):
        return cls.model_validate_json((Path(input_dir) / SAVE_FNAME).read_text())

    ####################################################################################
    # Validators
    ####################################################################################

    @model_validator(mode="after")
    def check_newest_date_after_oldest_date(self) -> "DatasetMetadata":
        if self.oldest_train_record_date and self.newest_train_record_date:
            if self.newest_train_record_date < self.oldest_train_record_date:
                raise ValueError(
                    f"newest_train_record_date ({self.newest_train_record_date}) must "
                    "not be before oldest_train_record_date "
                    f"({self.oldest_train_record_date})"
                )
        return self
