# World Traffic Analyzer 🌍🚦

This project explores live traffic conditions anywhere in the world using the TomTom Traffic Flow API and Reverse Geocoding API.

The goal was to practice making API requests, working with JSON data, organizing the results in pandas, and creating an interactive traffic visualization.

## What I did

- Pulled live traffic data for user-selected locations around the world
- Stored the results in a pandas DataFrame
- Compared current speeds with free-flow speeds
- Calculated congestion ratios and traffic risk
- Created an interactive Folium map
- Retrieved the road name and city for each selected location

## Traffic Metrics

This project compares several traffic metrics returned by the TomTom Traffic Flow API, including:

- **Current Speed** – The current traffic speed at the selected location.
- **Free-Flow Speed** – The expected speed under normal traffic conditions.
- **Congestion Ratio** – The current speed divided by the free-flow speed. Lower values indicate heavier traffic.
- **Traffic Risk** – A simple score calculated from the congestion ratio to estimate overall traffic conditions.
- **Road Name** – The name of the selected road.
- **City** – The city where the selected road is located.

## Tech Stack

- Python
- Streamlit
- Jupyter Notebook
- pandas
- requests
- Folium
- TomTom Traffic Flow API
- TomTom Reverse Geocoding API

## Preview

Below is an example showing traffic data for New York City. Users can click anywhere in the world to view live traffic conditions for that location.

![NYC Traffic Map Example](traffic_map.png)

## Setup Instructions

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Get a TomTom API key

Sign up at:

https://developer.tomtom.com

### 3. Create a `.streamlit/secrets.toml` file

```toml
TOMTOM_API_KEY = "your_api_key_here"
```

### 4. Run the application

```bash
streamlit run app.py
```
