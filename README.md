# fitbit-dashboard

Applications for extracting and displaying [Fitbit](https://fitbit.com) data, providing views that are not available in the standard [Google Fitbit phone app](https://apps.apple.com/us/app/fitbit-health-fitness/id462638897).

**Contents**

- [Overview](#overview)
  - [Data flow](#data-flow)
  - [Data priorities](#data-priorities)
- [License](#license)

## Overview

### Data flow

1. Export data from FitBit.
2. Upload the raw data to Google Cloud Storage (GCS).
3. Transform JSON files into Polars Dataframes.
4. Save the transformed data to Parquet files in GCS.
5. Summarize some of the data. For example,
  * Per week: Average calories per day.
  * Per week: Total elapsed minutes of exercise for exercise of at least 30 minutes.
  * Per week: Total Zone Minutes for exercise of at least 30 minutes.
6. Plot some of the data.
  * Individual features.
  * Correlation of features, e.g. elapsed exercise minutes vs weight.
7. Display the analysis in a web app.

### Data priorities

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
