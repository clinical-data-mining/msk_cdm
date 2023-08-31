from datetime import date

from pydantic import ValidationError
import pytest

from msk_cdm.data.metadata import DatasetMetadata


def test_fields_persisted_across_serialization(fs):
    # fs is a pyfakefs fixture
    output_dir = "/metadata_save/"
    fs.create_dir(output_dir)
    field_vals = {
        "cdm_project_id": "proj_id",
        "dataset_size": 10,
        "description": "this is a description",
        "oldest_train_record_date": "1990-01-12",
        "newest_train_record_date": "1992-03-10",
    }
    orig_metadata = DatasetMetadata(**field_vals)

    orig_metadata.save_to_dir(output_dir)
    read_metadata = DatasetMetadata.from_dir(output_dir)

    for field in field_vals.keys():
        assert getattr(orig_metadata, field) == getattr(read_metadata, field)


def test_datetime_fields_parsed_as_strs():
    metadata = DatasetMetadata(
        cdm_project_id="projid",
        dataset_size=10,
        oldest_train_record_date="1991-02-23",
        newest_train_record_date="2042-12-23",
    )

    assert metadata.oldest_train_record_date == date(1991, 2, 23)
    assert metadata.newest_train_record_date == date(2042, 12, 23)


def test_invalid_datetime_fields_raise_error():
    with pytest.raises(ValidationError):
        DatasetMetadata(
            cdm_project_id="projid",
            dataset_size=10,
            oldest_train_record_date="1991-13-23",
        )

    with pytest.raises(ValidationError):
        DatasetMetadata(
            cdm_project_id="projid",
            dataset_size=10,
            newest_train_record_date="2000-10-230",
        )


def test_newest_date_earlier_than_oldest_raises_error():
    with pytest.raises(ValidationError, match=r"must not be before"):
        DatasetMetadata(
            cdm_project_id="projid",
            dataset_size=10,
            oldest_train_record_date="2023-02-23",
            newest_train_record_date="1991-10-20",
        )


def test_either_newest_or_oldest_date_none_does_not_raise_error():
    DatasetMetadata(
        cdm_project_id="projid",
        dataset_size=10,
        newest_train_record_date="1991-10-20",
    )
    DatasetMetadata(
        cdm_project_id="projid",
        dataset_size=10,
        oldest_train_record_date="2023-02-23",
    )
