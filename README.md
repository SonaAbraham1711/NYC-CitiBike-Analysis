# NYC Citi Bike Strategic Dashboard Project (2022)

## Project Overview
This project involves a descriptive analysis of NYC Citi Bike trip data from 2022. As the lead analyst, the goal is to identify distribution patterns and logistics issues (such as station shortages or overflows) to provide actionable recommendations for the business strategy team. This analysis is enriched with 2022 weather data sourced from the NOAA API.

## Data Sources
- **Citi Bike Trip Data:** 2022 open-source trip data from the [Citi Bike S3 Bucket](https://s3.amazonaws.com/tripdata/index.html).
- **Weather Data:** 2022 Daily Global Historical Climatology Network data from [NOAA](https://www.ncdc.noaa.gov/cdo-web/api/v2/data) (Station: LaGuardia Airport, GHCND:USW00014732).

## Research Questions
- What are the most popular start and end stations in NYC?
- How does the daily average temperature and precipitation affect trip volume?
- At which stations do we see the largest imbalance between bike pickups and drop-offs?
- How do usage patterns differ between casual riders and annual members?

## Libraries & Tools
- **Environment:** Python 3.x (Virtual Environment: `citibike_env`)
- **Data Manipulation:** `pandas`, `numpy`
- **Data Sourcing:** `requests`, `json`, `os`
- **Visualization:** `matplotlib`, `seaborn`, `plotly`
- **Geospatial:** `kepler.gl`
- **Dashboard:** `streamlit`

## How to Navigate this Repo
- `NYC-CitiBike-Analysis.ipynb`: The main Jupyter Notebook containing data sourcing, cleaning, and merging logic.
- `nyc_weather_2022.csv`: The cleaned weather data extracted via API.
- `data/`: (Excluded from Git) Directory containing raw Citi Bike CSV files.
