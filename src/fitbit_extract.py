import os
from pathlib import Path
import polars as pl


def read_files(
    global_export_data_dir_name: Path, file_prefix: str, file_suffix: str
) -> pl.DataFrame | None:
    df = None
    with os.scandir(global_export_data_dir_name) as ged_dir_entries:
        for entry in ged_dir_entries:
            if (
                entry.name.startswith(file_prefix)
                and entry.name.endswith(file_suffix)
                and entry.is_file()
            ):
                entry_as_df = pl.read_json(
                    os.path.join(global_export_data_dir_name, entry.name)
                )
                df = entry_as_df if df is None else df.vstack(entry_as_df)
    return df
