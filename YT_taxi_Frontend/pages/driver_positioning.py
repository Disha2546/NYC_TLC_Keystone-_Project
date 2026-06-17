import streamlit as st
import requests


def run_app():

    st.title("🚖 Optimal Driver Positioning System")

    st.write(
        "Recommend optimal driver positioning based on predicted demand and revenue potential."
    )

    current_zone = st.number_input(
        "🔹 Current Zone",
        min_value=1,
        value=65
    )

    hour = st.slider(
        "🔹 Hour",
        0,
        23,
        18
    )

    day_of_week = st.selectbox(
        "🔹 Day of Week",
        [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
        ]
    )

    max_distance = st.slider(
        "🔹 Max Travel Distance (km)",
        1,
        20,
        5
    )

    top_zones_only = st.checkbox(
        "🔘 Show Top Zones Only"
    )

    if st.button("🚖 Get Recommendation"):

        payload = {

            "current_zone": current_zone,

            "hour": hour,

            "day_of_week": day_of_week,

            "max_distance": max_distance,

            "top_zones_only": top_zones_only
        }

        response = requests.post(
            "http://127.0.0.1:8000/recommend-driver-position",
            json=payload
        )

        if response.status_code == 200:

            result = response.json()

            st.success(
                f"Recommended Zone: {result['recommended_zone']}"
            )

            st.metric(
                "Recommendation Score",
                f"{result['score']:.2f}"
            )

            st.write(
                f"Current Zone: {result['current_zone']}"
            )

            st.subheader(
                "Top Recommended Zones"
            )

            for zone in result["top_zones"]:

                st.write(
                    f"Zone {zone['zone']} → Score: {zone['score']:.2f}"
                )

        else:

            st.error(
                f"API Error: {response.text}"
            )