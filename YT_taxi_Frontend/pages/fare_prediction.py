import streamlit as st
import requests
import pandas as pd

def show_fare_page():

    st.title("🚕 Trip Fare + Duration Prediction")

    passenger_count = st.number_input("Passenger Count", 1, 6, 1)
    trip_distance = st.number_input("Trip Distance", 0.1, 50.0, 2.0)
    pickup_hour = st.slider("Pickup Hour", 0, 23, 12)
    pu_location = st.number_input("Pickup Location ID", 1, 265, 79)
    do_location = st.number_input("Drop Location ID", 1, 265, 75)

    if st.button("Predict Trip"):

        payload = {
            "passenger_count": passenger_count,
            "trip_distance": trip_distance,
            "pickup_hour": pickup_hour,
            "PULocationID": pu_location,
            "DOLocationID": do_location
        }

        try:
            response = requests.post(
                "http://127.0.0.1:8000/predict-trip",
                json=payload
            )

            # ✅ DEBUG (VERY IMPORTANT)
            st.write("Status Code:", response.status_code)
            st.write("Raw Response:", response.text)

            # ❌ SAFETY CHECK (prevents JSON crash)
            if response.status_code != 200:
                st.error("Backend error occurred")
                st.stop()

            result = response.json()   # ✅ FIXED

            st.subheader("Prediction Result")

            st.metric("Estimated Fare ($)", result["fare"])
            st.metric("Estimated Duration (min)", result["duration_minutes"])

        except Exception as e:
            st.error(f"Request failed: {e}")