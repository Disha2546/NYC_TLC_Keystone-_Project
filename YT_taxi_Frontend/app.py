import streamlit as st

from pages.demand_forecasting import show_forecasting_page
from pages.fare_prediction import show_fare_page 
from pages.hotspot_detection import show_hotspot_page
from pages.driver_positioning import run_app
from pages.anomaly_detection import show_anomaly_page
from pages.real_time_dashboard import show_dashboard_page

st.set_page_config(

    page_title="NYC Taxi Demand Forecasting",
    page_icon="🚕",
    layout="wide"

)

st.sidebar.title("NYC Taxi Analytics")

page = st.sidebar.radio(

    "Select Use Case",

    [

        "Taxi Demand Forecasting",

        "Fare + Duration Prediction",

        "Pickup Hotspot Detection",

        "Driver Position Recommendation",

        "Anomaly Detection",

        "Real-Time Analytics Dashboard"

    ]
)

if page == "Taxi Demand Forecasting":
    show_forecasting_page()

elif page == "Fare + Duration Prediction":
    show_fare_page()

elif page == "Pickup Hotspot Detection":
    show_hotspot_page()

elif page == "Driver Position Recommendation":
    run_app()

elif page == "Anomaly Detection":
    show_anomaly_page()

elif page == "Real-Time Analytics Dashboard":
    show_dashboard_page()