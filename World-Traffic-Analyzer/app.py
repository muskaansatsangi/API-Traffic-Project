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


# Store the clicked location so the map remembers it.
# Streamlit reruns the entire app after a map click, so session state keeps the location.
if "clicked_location" not in st.session_state:
    st.session_state.clicked_location = None


# Create a map centered on the clicked location if available.
# If the user has clicked a location before, zoom into that area.
# Otherwise, show the full world map.
if st.session_state.clicked_location is not None:
    world_map = folium.Map(
        location=[
            st.session_state.clicked_location["lat"],
            st.session_state.clicked_location["lng"]
        ],
        zoom_start=14
    )
else:
    world_map = folium.Map(
        location=[20, 0],
        zoom_start=2
    )


# Add the previous clicked location marker if it exists.
# This keeps the pin visible after Streamlit reruns the app.
if st.session_state.clicked_location is not None:

    latitude = st.session_state.clicked_location["lat"]
    longitude = st.session_state.clicked_location["lng"]

    # Get the road and city information from TomTom.
    place = get_place_info(latitude, longitude)

    # Get live traffic information from TomTom.
    traffic = get_flow(latitude, longitude)

    if traffic is not None:

        # Save traffic values from the API response.
        current_speed = traffic["currentSpeed"]
        free_flow_speed = traffic["freeFlowSpeed"]
        travel_time = traffic["currentTravelTime"]
        road_closed = traffic["roadClosure"]
        confidence = traffic["confidence"]

        # Convert speeds from km/h to mph.
        current_speed_mph = round(current_speed * 0.621371)
        free_flow_speed_mph = round(free_flow_speed * 0.621371)

        # Compare current speed with normal free flow speed.
        if free_flow_speed > 0:
            speed_ratio = current_speed / free_flow_speed
        else:
            speed_ratio = 0

        # Classify the current traffic level.
        if speed_ratio >= 0.8:
            traffic_level = "Light Traffic"
        elif speed_ratio >= 0.5:
            traffic_level = "Moderate Traffic"
        else:
            traffic_level = "Heavy Traffic"


        # Create the text that appears inside the map popup.
        popup_text = f"""
        Road: {place['road']}<br>
        City: {place['city']}<br>
        Speed: {current_speed_mph} mph<br>
        Traffic: {traffic_level}<br>
        Confidence: {confidence}
        """

        # Add the clicked location marker back to the map.
        folium.Marker(
            [latitude, longitude],
            popup=popup_text,
            icon=folium.DivIcon(
                html="<div style='font-size: 35px;'>📍</div>"
            )
        ).add_to(world_map)


# Display the map and save click information.
map_data = st_folium(
    world_map,
    width=700,
    height=500
)


# Check whether the user clicked somewhere on the map.
# Save the clicked coordinates so the app can reuse them after rerunning.
if map_data["last_clicked"] is not None:

    st.session_state.clicked_location = {
        "lat": map_data["last_clicked"]["lat"],
        "lng": map_data["last_clicked"]["lng"]
    }

    # Rerun the app so the map can reload using the new clicked location.
    st.rerun()


# Show traffic information.
if st.session_state.clicked_location is not None:

    latitude = st.session_state.clicked_location["lat"]
    longitude = st.session_state.clicked_location["lng"]

    # Display the selected coordinates.
    st.write("Latitude:", round(latitude, 4))
    st.write("Longitude:", round(longitude, 4))

    # Display location information.
    place = get_place_info(latitude, longitude)

    st.markdown(f"**Road:** {place['road']}")
    st.markdown(f"**City:** {place['city']}")

    # Get live traffic data.
    traffic = get_flow(latitude, longitude)

    if traffic is None:
        st.error(
            "No traffic data was found. "
            "Try clicking directly on a major road."
        )

    else:

        # Save traffic values.
        current_speed = traffic["currentSpeed"]
        free_flow_speed = traffic["freeFlowSpeed"]
        travel_time = traffic["currentTravelTime"]
        road_closed = traffic["roadClosure"]
        confidence = traffic["confidence"]

        # Convert speeds from km/h to mph.
        current_speed_mph = round(current_speed * 0.621371)
        free_flow_speed_mph = round(free_flow_speed * 0.621371)

        # Compare current speed with free flow speed.
        if free_flow_speed > 0:
            speed_ratio = current_speed / free_flow_speed
        else:
            speed_ratio = 0

        # Decide traffic level.
        if speed_ratio >= 0.8:
            traffic_level = "Light Traffic"
        elif speed_ratio >= 0.5:
            traffic_level = "Moderate Traffic"
        else:
            traffic_level = "Heavy Traffic"


        # Display traffic information.
        st.subheader("Traffic Information")

        st.metric("Current Speed", f"{current_speed_mph} mph")
        st.metric("Free Flow Speed", f"{free_flow_speed_mph} mph")
        st.metric("Travel Time", f"{travel_time} sec")


        # Display traffic level with different colors.
        if traffic_level == "Light Traffic":
            st.success(f"Traffic Level: {traffic_level}")
        elif traffic_level == "Moderate Traffic":
            st.warning(f"Traffic Level: {traffic_level}")
        else:
            st.error(f"Traffic Level: {traffic_level}")


        st.write(f"Road Closed: {road_closed}")
        st.write(f"Confidence: {confidence}")


        # Explain the meaning of each traffic metric.
        with st.expander("What do these metrics mean?"):
            st.write("**Current Speed:** The vehicle speed currently detected on the road.")
            st.write("**Free Flow Speed:** The expected speed when traffic is moving normally without congestion.")
            st.write("**Travel Time:** The estimated time needed to travel the road segment.")
            st.write("**Traffic Level:** A classification based on the current speed compared to the normal free-flow speed.")
            st.write("**Road Closed:** Shows whether TomTom detected a road closure on this segment.")
            st.write("**Confidence:** TomTom's confidence score showing how reliable the traffic data is.")