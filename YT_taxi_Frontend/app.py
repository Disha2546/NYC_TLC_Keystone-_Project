import streamlit as st

from pages.demand_forecasting import (
    show_forecasting_page
)

st.set_page_config(

    page_title=
    "NYC Taxi Demand Forecasting",

    page_icon="🚕",

    layout="wide"

)

st.sidebar.title(
    "NYC Taxi Analytics"
)

page = st.sidebar.radio(

    "Select Use Case",

    [
        "Taxi Demand Forecasting"
    ]

)

if page == "Taxi Demand Forecasting":

    show_forecasting_page()