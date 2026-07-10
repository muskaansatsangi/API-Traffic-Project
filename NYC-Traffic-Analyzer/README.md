# NYC Traffic Analyzer 🚦

This project explores live traffic conditions across several locations in New York City using the TomTom Traffic API.

The goal was to practice making API requests, working with JSON data, organizing the results in pandas, and creating a traffic visualization.

## What I did

- Pulled live traffic data for several NYC locations
- Stored the results in a pandas DataFrame
- Compared current speeds with free-flow speeds
- Calculated congestion ratios and traffic risk
- Created an interactive Folium map

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

## Preview

![NYC Traffic Map](traffic_map.png)

## Setup Instructions

### 1. Install dependencies

```bash
pip install pandas requests folium python-dotenv
```

### 2. Get a TomTom API key

Sign up at:

https://developer.tomtom.com

### 3. Create a `.env` file in the same folder as your notebook

You can create it manually or run this Python code:

```python
with open(".env", "w") as f:
    f.write("TOMTOM_API_KEY=your_key_here\n")
```

Replace `your_key_here` with your actual TomTom API key.

### 4. Load the key in your notebook

```python
from dotenv import load_dotenv
import os

load_dotenv()
TOMTOM_API_KEY = os.getenv("TOMTOM_API_KEY")
```

## Traffic Metrics

This project compares several traffic metrics returned by the TomTom Traffic API, including:

- **Current Speed** – The current traffic speed at each location.
- **Free-Flow Speed** – The expected speed under normal traffic conditions.
- **Congestion Ratio** – The current speed divided by the free-flow speed. Lower values indicate heavier traffic.
- **Traffic Risk** – A simple score calculated from the congestion ratio to estimate overall traffic conditions.
