import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# 1. Page Configuration
st.set_page_config(page_title='NYC Citi Bike Strategy Dashboard', layout='wide')

st.title("NYC Citi Bike Strategy Dashboard")
st.markdown("This dashboard provides strategic insights into bike demand and geospatial distribution across NYC, helping optimize station rebalancing and expansion.")

# 2. Load Data
# Using the small files we created in the notebook for speed
top20 = pd.read_csv('top20.csv')
reduced_df = pd.read_csv('reduced_data_to_plot.csv')

# 3. Create the Bar Chart
fig_bar = go.Figure(go.Bar(
    x = top20['start_station_name'], 
    y = top20['value'], 
    marker = {'color': top20['value'], 'colorscale': 'Blues'}
))
fig_bar.update_layout(
    title = 'Top 20 Most Popular Citi Bike Stations in NYC',
    xaxis_title = 'Start Stations',
    yaxis_title = 'Total Trips'
)

# 4. Create the Dual-Axis Line Chart
# Grouping for daily views
df_daily = reduced_df.groupby('date').agg({'value': 'sum', 'avgTemp': 'mean'}).reset_index()

fig_line = make_subplots(specs=[[{"secondary_y": True}]])
fig_line.add_trace(
    go.Scatter(x=df_daily['date'], y=df_daily['value'], name='Daily Bike Rides', line=dict(color='blue')),
    secondary_y=False
)
fig_line.add_trace(
    go.Scatter(x=df_daily['date'], y=df_daily['avgTemp'], name='Daily Temperature', line=dict(color='red', dash='dot')),
    secondary_y=True
)
fig_line.update_layout(title_text='Daily Trips vs. Average Temperature')
fig_line.update_yaxes(title_text="Number of Rides", secondary_y=False)
fig_line.update_yaxes(title_text="Temperature (°F)", secondary_y=True)

# 5. Display the Plotly Charts in Streamlit
# We use columns to place them side-by-side or stacked
st.plotly_chart(fig_bar, use_container_width=True)
st.plotly_chart(fig_line, use_container_width=True)

# 6. Embed the Kepler.gl Map
st.header("Geospatial Distribution of Trips")
st.markdown("Interactive 3D Map showing the density of station-to-station paths.")


path_to_html = "NYC_CitiBike_Final_Map.html"
with open(path_to_html, 'r') as f:
    html_data = f.read()

st.components.v1.html(html_data, height=800)