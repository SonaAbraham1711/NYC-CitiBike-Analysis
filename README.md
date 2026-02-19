# 🚲 NYC Citi Bike Strategic Dashboard Project (2022)

## 📊 Project Overview
This project provides a comprehensive descriptive and geospatial analysis of NYC Citi Bike trip data from 2022. By aggregating over 30 million rows of data, the analysis identifies high-traffic commuter corridors, seasonal ridership trends, and geospatial demand to provide actionable recommendations for station rebalancing and infrastructure optimization.

## 📍 New: Interactive Streamlit Dashboard
The latest phase of this project features a live, interactive dashboard built with **Streamlit** and **Plotly**, allowing for real-time exploration of NYC's bike share network.

### Key Features:
* **Interactive 3D Geospatial Map:** A Kepler.gl integration showing high-volume "power routes" using 3D Arcs.
* **Trip Volume vs. Temperature:** A dual-axis line chart illustrating the strong correlation between daily average temperature and total ridership.
* **Top 20 Station Analysis:** A dynamic bar chart identifying the busiest starting stations for logistical prioritizing.

## 🔍 Geospatial & Analytical Findings
* **Commuter "Last-Mile" Hubs:** Massive trip density is concentrated near Penn Station and Grand Central Terminal, confirming Citi Bike’s role as a critical link for commuters.
* **Recreational Corridors:** High volumes along the Hudson River Greenway and Central Park West highlight heavy leisure and tourist usage.
* **Inter-Borough Connectors:** Thick arc clusters crossing the Williamsburg and Manhattan Bridges reveal essential cycling links between Brooklyn and the Lower East Side.

## 🛠️ Tech Stack
* **Dashboarding:** `streamlit`, `plotly`
* **Geospatial:** `keplergl` (3D Arc Layers)
* **Data Science:** `pandas`, `numpy`
* **Environment:** Python 3.11 (`citibike_env_new`)

## 📂 Repository Structure
* `st_dashboard.py`: **[NEW]** The main Streamlit script for the interactive dashboard.
* `NYC_CitiBike_Geospatial_Map.ipynb`: Notebook detailing the Kepler.gl map creation and geospatial analysis.
* `NYC_CitiBike_Final_Map.html`: Standalone interactive 3D map with embedded configuration.
* `reduced_data_to_plot.csv`: Optimized dataset for high-speed dashboard performance.
* `top20.csv`: Aggregated data for station popularity visualizations.
* `config.json`: Exported Kepler.gl settings for visual consistency.

## 🚀 How to Run the Dashboard
1.  **Activate Environment:**
    ```bash
    source citibike_env_new/bin/activate  
    ```
2.  **Install Dependencies:**
    ```bash
    pip install streamlit plotly keplergl
    ```
3.  **Launch Dashboard:**
    ```bash
    streamlit run st_dashboard.py
    ```
4.  **View:** Open your browser to `http://localhost:8501`.

> **Note on Data:** Due to GitHub's file size limits, the raw `merged_citibike_2022.csv` (30M+ rows) is not included. The dashboard runs exclusively on the provided `reduced_data_to_plot.csv` for efficiency.