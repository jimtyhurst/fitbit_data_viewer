from pathlib import Path
import polars as pl


FITBIT_DATE_FORMAT = '%m/%d/%y'
ISO_8601_DATE_FORMAT = '%Y-%m-%d'


def read_raw_files(
    global_export_data_dir_name: Path, file_prefix: str, file_suffix: str
) -> pl.DataFrame | None:
    """
    Reads all the files matching &lt;file_prefix&gt;*&lt;file_suffix&gt; into a Polars DataFrame.

    :param global_export_data_dir_name: Path for the directory containing the
        files to be read.
    :param file_prefix: string for matching the beginning of a file name.
    :param file_suffix: string for matching the end of a file name, including
        the file type suffix. Examples:
        '.json' to match any file ending in '.json'.
        '-2024.json' to match any file name ending in '-2024.json'.
    :returns: Concatenation of all the matching files into a DataFrame.
        Returns None if there are no matching files.
    """
    df = None
    for entry in global_export_data_dir_name.iterdir():
        if (
            entry.name.startswith(file_prefix)
            and entry.name.endswith(file_suffix)
            and entry.is_file()
        ):
            entry_as_df = pl.read_json(
                global_export_data_dir_name.joinpath(entry.name)
            )
            df = entry_as_df if df is None else df.vstack(entry_as_df)
    return df


def date_string_to_date_object(
    df: pl.DataFrame,
    string_column_name: str = 'date',
    object_column_name: str | None = None,
    date_format: str = FITBIT_DATE_FORMAT,
) -> pl.DataFrame:
    """
    Converts a column of string values to a column of date objects.

    :param df: DataFrame with a column of string values that need to be
        converted to date objects.
    :param string_column_name: The name of the column of string values to be
        converted. Defaults to 'date'.
    :param object_column_name: The name of the column of date object values to
        be added to the DataFrame. Defaults to the same value as
        `string_column_name`, in which case the column of string values is
        replaced by a column of date objects, but the column keeps its name.
    :param date_format: Formatting string used to convert a string value
        to a date object. Defaults to `FITBIT_DATE_FORMAT`.
    :returns: DataFrame with one column of string values converted to a column
        of date objects. The resulting column can replace the original column of
        string values or be appended as a new column, depending on the value of
        the `object_column_name` parameter.
    """
    if object_column_name is None:
        object_column_name = string_column_name
    tx_df = df.with_columns(
        [
            pl.col(string_column_name)
            .str.strptime(
                pl.Date,
                format=date_format,
                strict=False,
            )
            .alias(object_column_name)
        ]
    )
    return tx_df
