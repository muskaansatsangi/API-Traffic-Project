# Use Streamlit to build the website.
import streamlit as st

# Use Folium to create the interactive map.
import folium

# Connect the Folium map to Streamlit.
from streamlit_folium import st_folium

# Import the function that gets traffic data from TomTom.
from traffic_api import get_flow


# Show the page title.
st.title("World Traffic Analyzer")

# Show a short description.
st.write("Click on a road to view live traffic conditions.")


# Create a world map.
world_map = folium.Map(
    location=[20, 0],
    zoom_start=2
)


# Display the map and save click information.
map_data = st_folium(
    world_map,
    width=700,
    height=500
)


# Check whether the user clicked somewhere on the map.
if map_data["last_clicked"] is not None:

    # Save the latitude and longitude of the clicked location.
    latitude = map_data["last_clicked"]["lat"]
    longitude = map_data["last_clicked"]["lng"]

    # Show the selected coordinates rounded to 4 decimal places.
    st.write("Latitude:", round(latitude, 4))
    st.write("Longitude:", round(longitude, 4))

    # Get live traffic data from TomTom.
    traffic = get_flow(latitude, longitude)

    # Check whether TomTom returned traffic data.
    if traffic is None:
        st.error(
            "No traffic data was found. "
            "Try clicking directly on a major road."
        )

    else:
        # Save the traffic values.
        current_speed = traffic["currentSpeed"]
        free_flow_speed = traffic["freeFlowSpeed"]
        travel_time = traffic["currentTravelTime"]
        road_closed = traffic["roadClosure"]
        confidence = traffic["confidence"]

        # Convert speeds from kilometers per hour to miles per hour.
        current_speed_mph = current_speed * 0.621371
        free_flow_speed_mph = free_flow_speed * 0.621371

        # Compare the current speed with the normal speed.
        if free_flow_speed > 0:
            speed_ratio = current_speed / free_flow_speed
        else:
            speed_ratio = 0

        # Decide the traffic level.
        if speed_ratio >= 0.8:
            traffic_level = "Light Traffic"
        elif speed_ratio >= 0.5:
            traffic_level = "Moderate Traffic"
        else:
            traffic_level = "Heavy Traffic"

        # Display the traffic information.
        st.subheader("Traffic Information")

        st.metric("Current Speed", f"{current_speed_mph:.1f} mph")
        st.metric("Free Flow Speed", f"{free_flow_speed_mph:.1f} mph")
        st.metric("Travel Time", f"{travel_time} sec")

        # Display a colored traffic message.
        if traffic_level == "Light Traffic":
            st.success(f"Traffic Level: {traffic_level}")
        elif traffic_level == "Moderate Traffic":
            st.warning(f"Traffic Level: {traffic_level}")
        else:
            st.error(f"Traffic Level: {traffic_level}")

        st.write(f"Road Closed: {road_closed}")
        st.write(f"Confidence: {confidence}")

        # Explain each traffic measurement.
        with st.expander("What does this information mean?"):

            st.markdown("""
**Current Speed**  
The estimated speed vehicles are currently traveling on the selected road.

**Free Flow Speed**  
The estimated speed vehicles would travel if there were little or no traffic.

**Travel Time**  
The estimated time required to drive through the road segment being measured.

**Traffic Level**  
This compares the current speed with the free flow speed.

- **Light Traffic:** Vehicles are moving close to the normal speed.
- **Moderate Traffic:** Vehicles are moving slower than normal.
- **Heavy Traffic:** Vehicles are moving much slower than normal.

**Road Closed**  
- **False:** The road is open.
- **True:** The road is reported as closed.

**Confidence**  
A value between **0 and 1** that represents how confident TomTom is in the traffic data.

- **1.0:** Very high confidence.
- **Closer to 0:** Lower confidence.
""")