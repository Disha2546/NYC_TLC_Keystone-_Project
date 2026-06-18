import streamlit as st
from datetime import datetime
import requests


def show_anomaly_page():

    st.title("🚨 NYC Taxi Anomaly Detection")

    API_URL = "http://127.0.0.1:8000/anomaly/predict"

    pickup_zone = st.number_input("Pickup Zone", 1, 265, 10)
    drop_zone = st.number_input("Drop Zone", 1, 265, 50)

    pickup_datetime = st.datetime_input("Pickup Time", datetime.now())

    if st.button("Detect Anomaly"):

        payload = {
            "pickup_zone": pickup_zone,
            "drop_zone": drop_zone,
            "pickup_datetime": pickup_datetime.isoformat()
        }

        try:
            response = requests.post(API_URL, json=payload)

            if response.status_code != 200:
                st.error(response.text)
                return

            result = response.json()

            st.divider()

            if result["label"] == "Anomaly":
                st.error(f"🚨 ANOMALY ({result['anomaly_score']:.2f})")
            else:
                st.success(f"✅ NORMAL ({result['anomaly_score']:.2f})")

            st.progress(min(result["anomaly_score"], 1.0))

            st.subheader("Reasons")
            for r in result["reasons"]:
                st.write("•", r)

        except Exception as e:
            st.error("Backend not reachable")
            st.code(str(e))