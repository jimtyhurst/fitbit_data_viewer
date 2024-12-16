import fitbit_data_viewer as fdv
from pathlib import Path


def test_date_string_to_date_object_replace_column():
    """
    Expects 'date' column to be converted from string to date object.
    """
    raw_df = fdv.read_raw_files(
        global_export_data_dir_name=Path('.').joinpath(
            'tests', 'test_data', 'extractable_data'
        ),
        file_prefix='weight-',
        file_suffix='.json',
    )
    expected_date = raw_df['date'][0]  # compare first row
    date_formatted_df = fdv.date_string_to_date_object(raw_df)
    actual_date = date_formatted_df['date'][0]
    print(f'\n{raw_df["date"][0]=}')
    print(f'{date_formatted_df["date"][0]=}')
    assert expected_date == actual_date.strftime(fdv.FITBIT_DATE_FORMAT)


def test_date_string_to_date_object_new_column():
    """
    Expects 'date' column to be converted from string to date object.
    """
    raw_df = fdv.read_raw_files(
        global_export_data_dir_name=Path('.').joinpath(
            'tests', 'test_data', 'extractable_data'
        ),
        file_prefix='weight-',
        file_suffix='.json',
    )
    last_row_index = raw_df.shape[0] - 1
    expected_date = raw_df['date'][last_row_index]  # compare last row
    date_formatted_df = fdv.date_string_to_date_object(
        raw_df, string_column_name='date', object_column_name='date_object'
    )
    actual_date = date_formatted_df['date_object'][last_row_index]
    print(f'\n{raw_df["date"][last_row_index]=}')
    print(f'{date_formatted_df["date_object"][last_row_index]=}')
    assert expected_date == actual_date.strftime(fdv.FITBIT_DATE_FORMAT)
