import streamlit as st

from pages.demand_forecasting import show_forecasting_page
from pages.fare_prediction import show_fare_page 

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
        "Fare + Duration Prediction" 
    ]

)

if page == "Taxi Demand Forecasting":
    show_forecasting_page()

elif page == "Fare + Duration Prediction":
    show_fare_page()