# NYC Citi Bike Strategic Dashboard Project (2022)

## Project Overview
This project involves a descriptive analysis of NYC Citi Bike trip data from 2022. As the lead analyst, the goal is to identify distribution patterns and logistics issues to provide actionable recommendations. This version transitions the project into advanced statistical territory, utilizing Seaborn to analyze user demographics and trip distributions through complex grids and categorical plots.

## Data Sources
- **Citi Bike Trip Data:** 2022 open-source trip data (30M+ records) from the [Citi Bike S3 Bucket](https://s3.amazonaws.com/tripdata/index.html).
- **Weather Data:** 2022 Daily GHCND data from [NOAA](https://www.ncdc.noaa.gov/cdo-web/api/v2/data) (Station: LaGuardia Airport).

## Key Visualizations & Analysis
- **Temperature vs. Ridership:** A dual-axis time-series plot (Object-Oriented Matplotlib) showing the strong positive correlation between daily temperature and trip volume.
- **Trip Duration Distribution:** A histogram with an overlaid Normal Distribution curve (using `scipy`) showing that most urban trips occur within 10-15 minutes.
- **User Demographics:** Comparative bar and pie charts analyzing 'Member vs. Casual' riders and 'Classic vs. Electric' bike preferences.
- **Top 20 Stations**: A horizontal bar chart utilizing a 20-color gradient palette to identify high-traffic start locations for rebalancing logistics.
- **User Type Analysis**: A box plot comparing 'Member vs. Casual' trip durations, highlighting differences in median usage and variance (IQR).
- **Behavioral Faceting**: A FacetGrid analysis crossing 'User Type' with 'Bike Type' to visualize how equipment choice affects trip duration across different segments.

## Libraries & Tools
- **Environment:** Python 3.x (Virtual Environment: `citibike_env`)
- **Data Manipulation:** `pandas`, `numpy`
- **Statistical Analysis:** `scipy`
- **Visualization:** `matplotlib` (Procedural & Object-Oriented paradigms), `seaborn`

## How to Navigate this Repo
- `NYC-CitiBike-Analysis.ipynb`: Notebook for data sourcing, cleaning, and merging.
- `NYC-CitiBike-Visual-Analysis.ipynb`: **[NEW]** Comprehensive visualization suite including Matplotlib dual-axis charts and distribution analysis.
- NYC_CitiBike_Seaborn_Analysis.ipynb:**[NEW]** Statistical visualization suite focusing on categorical distributions, custom Seaborn themes, and faceted grids.
- `nyc_weather_2022.csv`: Cleaned weather data extracted via API.
- **Note:** Large datasets (`merged_citibike_2022.csv`) are excluded from this repo via `.gitignore` due to size constraints.
