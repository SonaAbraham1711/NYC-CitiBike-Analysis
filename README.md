# NYC Citi Bike Strategic Dashboard Project (2022)

## Project Overview
This project involves a descriptive and geospatial analysis of NYC Citi Bike trip data from 2022. The goal is to identify distribution patterns, logistics issues, and high-traffic commuter corridors to provide actionable recommendations for bike rebalancing and infrastructure.

## 📍 Geospatial Analysis (New)
The latest phase of this project utilizes **Kepler.gl** to visualize the flow of over 30 million trips across New York City using 3D Arc layers.

### Key Geospatial Findings:
* **Commuter Arteries:** Massive trip density identified near Penn Station and Grand Central, confirming Citi Bike's role in "last-mile" transit.
* **Recreational Hubs:** High volumes along the Hudson River Greenway and Central Park West highlight seasonal and leisure usage.
* **Inter-Borough Flow:** Analysis of bridge crossings (Williamsburg/Manhattan Bridges) reveals critical cycling links between Brooklyn and Manhattan.

## 📊 Key Visualizations
- **Geospatial Map:** 3D Arc visualization of station-to-station paths using Kepler.gl.
- **Temperature vs. Ridership:** Dual-axis time-series plot showing correlation between weather and trip volume.
- **User Demographics:** Analysis of 'Member vs. Casual' riders and bike type preferences.
- **Top 20 Stations:** High-traffic start locations identified for rebalancing logistics.

## 🛠️ Libraries & Tools
- **Geospatial:** `keplergl`, `setuptools`
- **Data Manipulation:** `pandas`, `numpy`
- **Visualization:** `matplotlib`, `seaborn`
- **Environment:** Python 3.11/3.12 (Virtual Env: `citibike_env_new`)

## 📂 How to Navigate this Repo
- `NYC_CitiBike_Geospatial_Map.ipynb`: **[NEW]** Notebook containing the Kepler.gl map creation and geospatial analysis.
- `NYC_CitiBike_Final_Map.html`: **[NEW]** Standalone interactive map (Open in Chrome/Safari).
- `config.json`: **[NEW]** Saved Kepler map configuration.
- `NYC-CitiBike-Visual-Analysis.ipynb`: Matplotlib and Seaborn visualization suite.
- `nyc_weather_2022.csv`: Cleaned weather data.