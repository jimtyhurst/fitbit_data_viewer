import fitbit_data_viewer as fdv
from pathlib import Path
import pytest


def test_extract_multiple_files():
    """
    Expects data from 'weight-*.json' files.
    """

    actual_df = fdv.read_raw_files(
        global_export_data_dir_name=Path('.').joinpath('tests', 'test_data', 'extractable_data'),
        file_prefix='weight-',
        file_suffix='.json',
    )
    assert actual_df.shape[0] == 42
    assert actual_df.shape[1] == 6
    assert actual_df.columns == ['logId', 'weight', 'bmi', 'date', 'time', 'source']


def test_file_not_found():
    """
    Expects FileNotFoundError due to non-existent directory.
    """

    with pytest.raises(FileNotFoundError):
        fdv.read_raw_files(
            global_export_data_dir_name=Path('.').joinpath(
                'tests', 'test_data', 'non_existent_directory'
            ),
            file_prefix='weight-',
            file_suffix='.inaccessible',
        )


def test_unmatched_file_type():
    """
    Expects None is returned, because there are no matching files in the given directory.
    """

    actual_df = fdv.read_raw_files(
        global_export_data_dir_name=Path('.').joinpath('tests', 'test_data', 'extractable_data'),
        file_prefix='weight-',
        file_suffix='.unknown',
    )
    assert actual_df is None


def test_read_complicated_structure():
    """
    Expects read into Polars DataFrame, even though a column contains complex structures.
    """

    actual_df = fdv.read_raw_files(
        global_export_data_dir_name=Path('.').joinpath('tests', 'test_data', 'extractable_data'),
        file_prefix='heart_rate-',
        file_suffix='.json',
    )
    assert actual_df.columns == ['dateTime', 'value']
    assert isinstance(actual_df['value'][0], dict)
    assert actual_df['value'][0]['bpm'] > 0
    assert actual_df['value'][0]['confidence'] >= 0 and actual_df['value'][0]['confidence'] <= 1
