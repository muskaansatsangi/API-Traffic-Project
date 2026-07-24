# Send requests to the TomTom API.
import requests

# Access the API key from Streamlit Cloud or a local .env file.
import os
import streamlit as st

# Load the local .env file.
from dotenv import load_dotenv

# Load the API keys stored in the main project folder.
load_dotenv("../.env")

# Use Streamlit Secrets when deployed.
# Use the shared .env file when running locally.
try:
    TOMTOM_API_KEY = st.secrets["TOMTOM_API_KEY"]
except Exception:
    TOMTOM_API_KEY = os.getenv("TOMTOM_API_KEY")


# Get traffic information for a clicked location.
def get_flow(lat, lng):

    url = (
        "https://api.tomtom.com/traffic/services/4/"
        f"flowSegmentData/relative0/10/json?"
        f"point={lat},{lng}&key={TOMTOM_API_KEY}"
    )

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        return data.get("flowSegmentData")

    except requests.exceptions.RequestException as error:
        print("Traffic API error:", error)
        return None


# Get the road name and city for a clicked location.
def get_place_info(lat, lng):

    url = (
        "https://api.tomtom.com/search/2/reverseGeocode/"
        f"{lat},{lng}.json?key={TOMTOM_API_KEY}"
    )

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        # Get the first address TomTom found.
        addresses = data.get("addresses", [])

        if addresses:
            address = addresses[0]["address"]

            return {
                "road": address.get("streetName", "Unknown Road"),
                "city": address.get("municipality", "Unknown City")
            }

    except requests.exceptions.RequestException as error:
        print("Place API error:", error)

    return {
        "road": "Unknown Road",
        "city": "Unknown City"
    }