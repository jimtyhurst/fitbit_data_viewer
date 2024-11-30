from pathlib import Path
import polars as pl


def read_files(
    global_export_data_dir_name: Path, file_prefix: str, file_suffix: str
) -> pl.DataFrame | None:
    """
    Reads all the files matching &lt;file_prefix&gt;*&lt;file_suffix&gt; into a Polars DataFrame.

    :param global_export_data_dir_name : Path for the directory containing the files to be read.
    :param file_prefix string for matching a file name.
    :param file_suffix string for matching a file name, including the file suffix, such as '.json' to match any file ending in '.json'.
    :returns: concatenation of all the matching files into a DataFrame. Returns None if there are no matching files.
    :rtype: polars.DataFrame
    """
    df = None
    for entry in global_export_data_dir_name.iterdir():
        if (
            entry.name.startswith(file_prefix)
            and entry.name.endswith(file_suffix)
            and entry.is_file()
        ):
            entry_as_df = pl.read_json(global_export_data_dir_name.joinpath(entry.name))
            df = entry_as_df if df is None else df.vstack(entry_as_df)
    return df
