# fitbit_data_viewer

Python modules and scripts for extracting and displaying [Fitbit](https://fitbit.com) data, providing views that are not available in the standard [Google Fitbit phone app](https://apps.apple.com/us/app/fitbit-health-fitness/id462638897).

**Contents**

- [Overview](#overview)
  - [Application workflow](#application-workflow)
  - [Data priorities](#data-priorities)
- [License](#license)

## Overview

### Application workflow

#### Minimum Viable Product (MVP) goals

Theme: Plot weight trend over time.

1. _Extract_ data from FitBit.
  * Fitbit subscriber downloads their own data manually.
  * See the Fitbit support article, [How do I export my Fitbit data?](https://support.google.com/fitbit/answer/14236615), for instructions.
  * This export process results in a very large number of JSON files on your local machine.
2. _Transform_ the raw JSON files.
  * Manage the data as [Polars DataFrames](https://docs.pola.rs/user-guide/concepts/data-types-and-structures/#dataframe).
  * Transform only weight-related files.
  * Change date fields from strings to date objects.
  * Save only one weight measurement per day.
  * Save the transformed data to [Parquet](https://parquet.apache.org/) files on your local file system.
3. Generate a plot of weight over time for a user-definable time period.
4. Deploy a dashboard to enable the user to specify a time period, then display the resulting plot.

#### Longer term workflow goals

1. _Extract_ data from FitBit.
  * Upload the raw data to [Google Cloud Storage](https://cloud.google.com/storage) (GCS).
2. _Transform_ the raw JSON files.
  * Save the transformed data to [Parquet](https://parquet.apache.org/) files in GCS.
3. Summarize some of the data. For example,
  * Per week: Average calories per day.
  * Per week: Total elapsed minutes of exercise for exercise of at least 30 minutes.
  * Per week: Total Zone Minutes for exercise of at least 30 minutes.
4. Plot some of the data.
  * Individual features.
  * Correlation of features, e.g. elapsed exercise minutes vs weight.
5. Display the analysis in a web app dashboard.

### TODO: Data priorities

1. Day: Weight.
1. Week/month: Average weight.
1. Day/week/month: Total elapsed minutes of exercise for exercise of at least 30 minutes.
1. Week/month: Average heart rate for exercise of at least 30 elapsed minutes.
1. Day/week/month: Total Zone Minutes for exercise of at least 30 elapsed minutes.
1. Day: Total calories.
1. Week/month: Average calories per day.

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
