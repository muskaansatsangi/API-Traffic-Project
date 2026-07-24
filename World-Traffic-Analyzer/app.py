# Use Streamlit to build the website.
import streamlit as st

# Use Folium to create the interactive map.
import folium

# Connect the Folium map to Streamlit.
from streamlit_folium import st_folium

# Import the functions that get traffic and place data from TomTom.
from traffic_api import get_flow, get_place_info


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

    # Get the road name and city for the clicked coordinates.
    place = get_place_info(latitude, longitude)

    st.markdown(f"**Road:** {place['road']}")
    st.markdown(f"**City:** {place['city']}")

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

        # Convert speeds from km/h to mph.
        current_speed_mph = round(current_speed * 0.621371)
        free_flow_speed_mph = round(free_flow_speed * 0.621371)

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

        st.metric("Current Speed", f"{current_speed_mph} mph")
        st.metric("Free Flow Speed", f"{free_flow_speed_mph} mph")
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

        # Explain what each metric means.
        with st.expander("What do these metrics mean?"):
            st.write("**Current Speed:** The vehicle speed currently detected on the road.")
            st.write("**Free Flow Speed:** The expected speed when traffic is moving normally without congestion.")
            st.write("**Travel Time:** The estimated time needed to travel the road segment.")
            st.write("**Traffic Level:** A classification based on the current speed compared to the normal free-flow speed.")
            st.write("**Road Closed:** Shows whether TomTom detected a road closure on this segment.")
            st.write("**Confidence:** TomTom's confidence score showing how reliable the traffic data is.")