# Send requests to the TomTom API.
import requests

# Access environment variables, like the API key.
import os

# Load variables from the .env file into Python.
from dotenv import load_dotenv


# Read the .env file so Python can access the API key.
load_dotenv()

# Get the TomTom API key from the .env file.
TOMTOM_API_KEY = os.getenv("TOMTOM_API_KEY")


# Get traffic flow data for a specific latitude and longitude.
def get_flow(lat, lng):

    # Build the TomTom API URL using the latitude, longitude, and API key.
    url = (
        "https://api.tomtom.com/traffic/services/4/"
        f"flowSegmentData/relative0/10/json?point={lat},{lng}&key={TOMTOM_API_KEY}"
    )

    try:
        # Send the request to TomTom.
        response = requests.get(url, timeout=10)

        # Check whether the request was successful.
        response.raise_for_status()

        # Convert the response into a Python dictionary.
        data = response.json()


        # Return only the traffic flow information.
        return data.get("flowSegmentData")

    except requests.exceptions.RequestException as error:

        # Print the error in the terminal.
        print("TomTom request error:", error)

        # Return nothing if the request fails.
        return None