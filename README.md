# fitbit_data_viewer

This project provides Python modules and scripts for extracting and displaying [Fitbit](https://fitbit.com) data, providing useful data visualizations that are not available in the standard [Google Fitbit phone app](https://apps.apple.com/us/app/fitbit-health-fitness/id462638897).

**Contents**

- [Overview](#overview)
  - [Application workflow](#application-workflow)
  - [Data priorities](#data-priorities)
- [Getting started](#getting-started)
- [Suggestions for developers](#suggestions-for-developers)
- [Design decisions](#design-decisions)
- [License](#license)

## Overview

### Application workflow

#### Minimum Viable Product (MVP) goals

Theme: Plot weight trend over time.

1. _Extract_ data from FitBit.
    * Fitbit subscriber downloads their own data manually.
    * See the Fitbit support article, "How do I export my Fitbit data?" (https://support.google.com/fitbit/answer/14236615), for instructions.
    * This export process results in a very large number of JSON files on your local machine.
2. _Transform_ the raw JSON files.
    * Manage the data within a [Polars DataFrame](https://docs.pola.rs/user-guide/concepts/data-types-and-structures/#dataframe).
    * Transform only the files needed for tracking weight.
        * Change date fields from strings to date objects.
        * Save only one weight measurement per day.
    * Save the transformed data to a [Parquet](https://parquet.apache.org/) file on your local file system.
3. Generate a plot of weight over time for a user-definable time period.
4. Deploy a web app dashboard to enable the user to specify a time period, then display the resulting plot.

#### Longer term workflow goals

1. _Extract_ data from FitBit.
    * Upload the raw data to Google Cloud Storage ([GCS](https://cloud.google.com/storage)).
2. _Transform_ the raw JSON files.
    * Save the transformed data to [Parquet](https://parquet.apache.org/) files in [GCS](https://cloud.google.com/storage).
3. Summarize some of the data. For example,
    * Per week: Average calories per day.
    * Per week: Total elapsed minutes of exercise for exercise sessions of at least 30 minutes.
    * Per week: Total Zone Minutes for exercise of at least 30 minutes.
4. Plot some of the data.
    * Individual features.
    * Correlation of features, e.g. elapsed exercise minutes vs weight.
5. Display the analysis in a web app dashboard.

### Data priorities

1. Day: Weight.
1. Week/month: Average weight.
1. Day/week/month: Total elapsed minutes of exercise for exercise of at least 30 minutes.
1. Week/month: Average heart rate for exercise of at least 30 elapsed minutes.
1. Day/week/month: Total Zone Minutes for exercise of at least 30 elapsed minutes.
1. Day: Total calories.
1. Week/month: Average calories per day.

## Getting started

The current project status assumes that you can set up a development environment and run the application from there. We use the [uv](https://github.com/astral-sh/uv) tool to:

* Manage the version of Python used for the project.
* Manage a virtual environment within the project directory.
* Manage package dependencies.
* Run developer tools, such as:
    * [ruff](https://astral.sh/ruff) for linting and formatting; and
    * [pytest](https://pytest.org/) for unit tests.
* Build the 'fitbit_data_viewer' package.

To set up the development environment:

1. Install uv: https://docs.astral.sh/uv/getting-started/installation/
1. Clone the project repository to your workspace:
    ```
    git clone git@github.com:jimtyhurst/fitbit_data_viewer.git
    ```
1. Create a virtual environment within the project directory.
    ```
    cd fitbit_data_viewer
    # Creates a virtual environment whose name defaults to
    # `fitbit_data_viewer`, i.e. the project name.
    uv venv
    # Activates the virtual environment in the current shell instance.
    source .venv/bin/activate
    # Installs package dependencies into the virtual environment.
    uv sync
    ```
    The package dependencies are listed in [pyproject.toml](./pyproject.toml) and the full set of transitive dependencies is saved in [uv.lock](./uv.lock).
1. If you plan to use a Jupyter notebook to explore this package:
    1. Add the new virtual environment to the Jupyter kernels:
        ```
        python -m ipykernel install --user --name=fitbit_data_viewer
        ```
        where 'fitbit_data_viewer' is the name of the project _and_ the name of the virtual environment.
    1. Set up a `.env` file to define environment variables for the directories in your local workspace to hold data. Use the [env.example](./notebooks/env.example) file as a template for your `.env` file.
    1. You can see how the `.env` file is used in the [fitbit-weight-eda.ipynb](./notebooks/fitbit-weight-eda.ipynb) notebook.

## Suggestions for developers

1. Create [pre-commit](https://pre-commit.com/) hooks, so that any changes that you make will conform to the project's code formatting standards.
    ```
    pre-commit install
    ```
1. Make code changes on a branch:
    ```
    git switch -c my-branch
    ```
1. If you make any changes to the code, make sure that the unit tests still pass.
    ```
    uv run pytest -s
    ```
1. To build the package:
    ```
    uv build
    ```

## Design decisions

- See the [tools.md](./docs/tools.md) document for a brief discussion of the selection of packages and tools for this project.

## License

Copyright (c) 2024 [Jim Tyhurst](https://jimtyhurst.com)

This program is free software: you can redistribute it and/or modify
it under the terms of the
[GNU General Public License](https://www.gnu.org/licenses/)
as published by the Free Software Foundation, either version 3 of the License,
or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
