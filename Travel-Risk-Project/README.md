# RouteWise 🌦️🚗

RouteWise combines live traffic, weather, and air quality data to provide a simple overview of current travel conditions across New York City.

The goal of this project was to practice working with multiple APIs, combining different data sources, and visualizing the results in an easy-to-understand way.

## What I did

- Combined live traffic data from the TomTom Traffic API with weather and air quality data from Open-Meteo
- Calculated traffic, weather, air quality, and overall travel risk scores
- Evaluated rain probability, wind gusts, and air quality conditions
- Converted official Open-Meteo weather codes into weather icons
- Created an interactive weather map with clickable weather markers
- Generated a simple travel recommendation based on current conditions

## Travel Metrics

This project combines several travel metrics, including:

- **Traffic Risk** – Calculated using live traffic conditions from the TomTom Traffic API.
- **Weather Risk** – Based on rain probability and wind gusts.
- **Air Quality Risk** – Uses the Air Quality Index (AQI) from Open-Meteo.
- **Overall Travel Risk** – Combines traffic, weather, and air quality into a single score.

## Locations

- Times Square
- Central Park South
- Grand Central
- Wall Street
- Brooklyn Bridge

## Tech Stack

- Python
- Jupyter Notebook
- pandas
- requests
- Folium
- TomTom Traffic API
- Open-Meteo Weather API
- Open-Meteo Air Quality API

## Preview



## Setup Instructions

### 1. Install dependencies

```bash
pip install pandas requests folium python-dotenv
```

### 2. Get a TomTom API key

Sign up at:

https://developer.tomtom.com

### 3. Create a `.env` file

```python
with open(".env", "w") as f:
    f.write("TOMTOM_API_KEY=your_key_here\n")
```

Replace `your_key_here` with your TomTom API key.

Open-Meteo does not require an API key.

### 4. Load the key

```python
from dotenv import load_dotenv
import os

load_dotenv()
TOMTOM_API_KEY = os.getenv("TOMTOM_API_KEY")
```
