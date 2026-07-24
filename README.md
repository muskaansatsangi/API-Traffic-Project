# API Projects 🚀

A collection of projects I built to practice working with APIs, data analysis, and visualization.

## World Traffic Analyzer 🌍🚦

This is a project where I explored live traffic data from anywhere in the world using the TomTom Traffic Flow API and Reverse Geocoding API.

The goal was to practice making API requests, organizing the results in pandas, comparing traffic speeds, and creating an interactive web application.

### What I did

- Pulled live traffic data for user-selected locations around the world
- Stored the results in a pandas DataFrame
- Compared current speeds with free-flow speeds
- Calculated congestion and traffic risk
- Visualized the locations on an interactive Folium map
- Displayed the road name and city using reverse geocoding

### Tech Stack

- Python
- Jupyter Notebook
- Streamlit
- pandas
- requests
- Folium
- TomTom Traffic Flow API
- TomTom Reverse Geocoding API

📁 Project folder: [World-Traffic-Analyzer](World-Traffic-Analyzer/)

---

## RouteWise 🌦️🚗

RouteWise combines live traffic, weather, and air-quality data to give a clearer view of travel conditions in New York City.

The goal was to practice working with multiple APIs and turn the data into a simple overall travel risk score.

### What I did

- Combined traffic data from the TomTom Traffic API with weather and air-quality data from Open-Meteo
- Used rain chance, wind gusts, and air quality in the travel-risk calculation
- Calculated traffic, weather, air-quality, and overall travel risk
- Converted official Open-Meteo weather codes into easy-to-read weather icons
- Created an interactive weather map with clickable weather markers

### Tech Stack

- Python
- Jupyter Notebook
- pandas
- requests
- Folium
- TomTom Traffic API
- Open-Meteo Weather API
- Open-Meteo Air Quality API

📁 Project folder: [Travel-Risk-Project](Travel-Risk-Project/)