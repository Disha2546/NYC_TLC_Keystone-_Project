import streamlit as st
import requests
import pandas as pd

def show_fare_page():

    st.title("⏱️ Trip Duration Prediction")

    st.write("Predict the estimated trip duration for NYC taxi rides.")

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
                "http://127.0.0.1:8000/predict-duration",
                json=payload
            )

            # ✅ DEBUG (VERY IMPORTANT)
            st.write("Status Code:", response.status_code)
            st.write("Raw Response:", response.text)

            # ❌ SAFETY CHECK (prevents JSON crash)
            if response.status_code == 200:
                result = response.json()

                if "predicted_duration" in result:

                    duration = result["predicted_duration"]

                    st.success(
                        f"Estimated Trip Duration: {duration:.2f} minutes"
                    )

                    st.metric(
                        "Predicted Duration (minutes)",
                        f"{duration:.2f}"
                    )

                elif "error" in result:

                    st.error(result["error"])

                else:

                    st.error("Unexpected API response.")

            else:

                st.error(
                    f"API Error ({response.status_code})"
                )

                st.write(response.text)

        except Exception as e:

            st.error(
                f"Connection Failed: {str(e)}"
            )