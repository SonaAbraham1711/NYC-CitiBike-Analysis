# 🚲 NYC Citi Bike Strategic Dashboard Project (2022)

## 📊 Project Overview
This project provides a comprehensive descriptive and geospatial analysis of NYC Citi Bike trip data from 2022. By processing over 30 million rows of data, the analysis identifies high-traffic commuter corridors, seasonal ridership trends, and geospatial demand to provide actionable recommendations for station rebalancing and infrastructure optimization.

## 📍 Live Dashboard
**View the interactive app here:** [INSERT YOUR STREAMLIT CLOUD URL HERE]

The dashboard is built with **Streamlit** and **Plotly**, allowing for real-time exploration of NYC's bike-share network.

### Key Features:
* **Interactive 3D Geospatial Map:** A Kepler.gl integration showing high-volume "power routes" using 3D Arcs.
* **Weather & Demand Correlation:** A dual-axis line chart illustrating the relationship between daily average temperature and total ridership.
* **Top 20 Station Analysis:** A dynamic bar chart identifying the busiest starting stations, filterable by season.
* **Strategic Recommendations:** Data-driven insights for logistical and infrastructure improvements.

## 🔍 Key Findings
* **Temperature Sensitivity:** Ridership shows a near-perfect correlation with average temperature, peaking in Summer and requiring seasonal fleet adjustments.
* **Commuter Hubs:** High trip density is concentrated near major transit hubs like Penn Station and Grand Central Terminal.
* **Power Corridors:** Massive flows across the Williamsburg and Manhattan Bridges highlight the essential role of bike-share for inter-borough travel.

## 🛠️ Tech Stack
* **Dashboarding:** `streamlit`, `plotly`
* **Geospatial:** `keplergl` (3D Arc Layers)
* **Data Science:** `pandas`, `numpy`
* **Image Processing:** `Pillow`

## 📂 Repository Structure
* `st_dashboard_Part_2.py`: The main Streamlit script for the interactive dashboard.
* `NYC_CitiBike_Geospatial_Map.ipynb`: Notebook detailing the data cleaning, sampling, and Kepler.gl map creation.
* `NYC_CitiBike_Final_Map.html`: Standalone interactive 3D map.
* `reduced_data_to_plot_7.csv`: Optimized dataset (0.1% random sample) for high-speed cloud performance.
* `NYC_Bikes.jpg`: Dashboard cover image.

## 🚀 How to Run Locally
1. **Clone the Repo:**
   ```bash
   git clone [https://github.com/SonaAbraham1711/NYC-CitiBike-Analysis.git](https://github.com/SonaAbraham1711/NYC-CitiBike-Analysis.git)