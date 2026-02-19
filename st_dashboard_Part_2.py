import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from PIL import Image
import os

# 1. Page Configuration
st.set_page_config(page_title="NYC Citi Bike Strategy Dashboard", layout="wide")

# 2. Load and Prepare Data
@st.cache_data
def load_data():
    # 1. Load the data
    df = pd.read_csv('reduced_data_to_plot_7.csv')
    
    # 2. Convert column names to lowercase
    df.columns = [c.lower() for c in df.columns]
    
    # 3. Fix Date: Convert and drop invalid rows (like duplicate headers)
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df = df.dropna(subset=['date'])
    
    # 4. Fix Temperature: Force to numeric
    # This identifies the temp column even if it's named 'avgtemp' or 'avg_temp'
    temp_col = 'avgtemp' if 'avgtemp' in df.columns else 'avg_temp'
    if temp_col in df.columns:
        df[temp_col] = pd.to_numeric(df[temp_col], errors='coerce')
    
    # 5. Fix Value: Force to numeric
    if 'value' in df.columns:
        df['value'] = pd.to_numeric(df['value'], errors='coerce')
    else:
        df['value'] = 1
        
    # 6. Final Clean: Drop any row that now has NaN in critical columns
    df = df.dropna(subset=[temp_col, 'value'])
        
    # 7. Handle seasons (same as before)
    if 'season' not in df.columns:
        def get_season(month):
            if month in [12, 1, 2]: return 'Winter'
            elif month in [3, 4, 5]: return 'Spring'
            elif month in [6, 7, 8]: return 'Summer'
            else: return 'Autumn'
        df['season'] = df['date'].dt.month.apply(get_season)
        
    return df

df = load_data()

# 3. Sidebar Navigation
st.sidebar.title("Dashboard Menu")
page = st.sidebar.selectbox('Select an aspect of the analysis',
   ["Intro page", 
    "Weather component and bike usage",
    "Most popular stations",
    "Interactive map with aggregated bike trips", 
    "Recommendations"])

# 4. Define Pages

# --- PAGE 1: INTRO ---
if page == "Intro page":
    st.title("NYC Citi Bike Strategic Analysis")
    st.markdown("### Optimizing Bike Supply in the City That Never Sleeps")
    
    # Check if the local file exists
    if os.path.exists("NYC_Bikes.jpg"):
        st.image("NYC_Bikes.jpg", caption="Citi Bike stations are a vital part of NYC transit.", use_container_width=True)
    else:
        # Professional placeholder if the image is missing
        st.info("📊 Welcome to the NYC Citi Bike Analysis Dashboard. Use the sidebar to explore the data.")

    st.markdown("""
    #### Project Background
    As NYC's premier bike-share program, Citi Bike faces a constant rebalancing challenge...
    """)
 

# --- PAGE 2: WEATHER ---
elif page == "Weather component and bike usage":
    st.header("The Impact of Temperature on Ridership")
    
    # Aggregate data by date
    # Note: Using .get() ensures we find 'avgtemp' even if the case changed
    temp_col = 'avgtemp' if 'avgtemp' in df.columns else 'avgtemp' 
    df_daily = df.groupby('date').agg({'value': 'sum', temp_col: 'mean'}).reset_index()
    
    # Create Dual-Axis Line Chart
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Scatter(x=df_daily['date'], y=df_daily['value'], name="Daily Trips", line=dict(color="#1f77b4")),
        secondary_y=False,
    )
    
    fig.add_trace(
        go.Scatter(x=df_daily['date'], y=df_daily[temp_col], name="Avg Temp (°C)", line=dict(color="#ff7f0e")),
        secondary_y=True,
    )

    fig.update_layout(title_text="Ridership vs. Temperature (2022)")
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    **Interpretation:** There is a near-perfect correlation between temperature and usage. Ridership remains low in Q1, 
    climbs steadily through Spring, and peaks in Summer. This suggests that supply shortages are 
    **seasonal** and predictable. Maintenance schedules should be shifted to Winter months 
    to ensure 100% fleet availability during the Summer peak.
    """)

# --- PAGE 3: POPULAR STATIONS ---
elif page == "Most popular stations":
    st.header("Top 20 High-Pressure Starting Stations")
    
    # Sidebar Filter for Season
    seasons = df['season'].unique()
    season_selection = st.sidebar.multiselect('Filter by Season', options=seasons, default=seasons)
    
    df_filtered = df[df['season'].isin(season_selection)]
    
    # Calculate Top 20
    top20 = df_filtered.groupby('start_station_name')['value'].sum().nlargest(20).reset_index()
    
    # Bar Chart
    fig_bar = go.Figure(go.Bar(
        x=top20['value'], 
        y=top20['start_station_name'], 
        orientation='h',
        marker=dict(color=top20['value'], colorscale='Blues')
    ))
    
    fig_bar.update_layout(yaxis={'categoryorder':'total ascending'}, height=600)
    st.plotly_chart(fig_bar, use_container_width=True)
    
    st.markdown("""
    **Interpretation:** Major transit hubs like **W 21 St & 6 Ave** and **West St & Chambers St** consistently show 
    the highest demand. These stations are "hot zones" where bikes disappear within minutes of 
    the morning commute starting. Rebalancing vans should prioritize these locations between 6:00 AM and 9:00 AM.
    """)

# --- PAGE 4: MAP ---
elif page == "Interactive map with aggregated bike trips":
    st.header("Geospatial Flow Analysis")
    st.write("Visualizing the 'Power Corridors' of NYC through 3D trip arcs.")
    
    # Display the Kepler map (HTML)
    if os.path.exists("NYC_CitiBike_Final_Map.html"):
        with open("NYC_CitiBike_Final_Map.html", 'r') as f:
            html_data = f.read()
        st.components.v1.html(html_data, height=800)
    else:
        st.warning("Kepler map HTML file not found.")
        
    st.markdown("""
    **Interpretation:** The map highlights intense activity across the **Manhattan and Williamsburg Bridges**. 
    Additionally, the **Hudson River Greenway** acts as a major artery for both commuters 
    and leisure riders. This suggests that infrastructure (docks) should be expanded along 
    waterfront pathways to reduce sidewalk congestion.
    """)

# --- PAGE 5: RECOMMENDATIONS ---
else:
    st.header("Strategic Recommendations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1. Dynamic Rebalancing")
        st.write("""
        Shift rebalancing efforts to a "Transit-First" model. Prioritize the top 20 stations 
        identified in the bar chart for replenishment during the early morning hours.
        """)
        
        st.subheader("2. Seasonal Workforce")
        st.write("""
        Increase the rebalancing van fleet by 30% between May and October to match the 
        temperature-driven demand surge shown in our weather analysis.
        """)

    with col2:
        st.subheader("3. Dock Expansion")
        st.write("""
        Invest in high-capacity "Super-Stations" at bridge entry points (Manhattan/Williamsburg). 
        These are high-flow corridors that currently lack sufficient docking capacity.
        """)
        
        st.subheader("4. Incentivized Riding")
        st.write("""
        Offer "Angel Points" or credits to users who ride bikes from high-supply stations 
        to empty stations in the morning to reduce reliance on manual rebalancing vans.
        """)