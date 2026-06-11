import streamlit as st
import pandas as pd
import requests
import plotly.express as px


def show_forecasting_page():

    st.title(
        "🚕 NYC Taxi Demand Forecasting"
    )

    st.markdown(
        """
        Forecast hourly taxi demand
        for NYC Zone 79.
        """
    )

    forecast_horizon = st.selectbox(

        "Forecast Horizon",

        [
            24,
            48,
            72
        ]

    )

    if st.button(
        "Generate Forecast"
    ):

        try:

            with st.spinner(
                "Generating forecast..."
            ):

                response = requests.post(

                    "http://127.0.0.1:8000/forecast",

                    json={
                        "forecast_horizon":
                        forecast_horizon
                    }

                )

                response.raise_for_status()

        except requests.exceptions.RequestException as e:

            st.error(
                f"Error connecting to API: {e}"
            )

            st.stop()

        forecast_df = pd.DataFrame(
            response.json()
        )

        st.subheader(
            "Forecast Results"
        )

        st.dataframe(
            forecast_df,
            width='stretch'
        )

        st.subheader(
            "Forecast Summary"
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Average Demand",
            round(
                forecast_df[
                    "forecasted_demand"
                ].mean()
            )
        )

        col2.metric(
            "Maximum Demand",
            forecast_df[
                "forecasted_demand"
            ].max()
        )

        col3.metric(
            "Minimum Demand",
            forecast_df[
                "forecasted_demand"
            ].min()
        )

# ==========================================
# Forecast Graph
# ==========================================
        # ==========================================
# Forecast Visualization using Plotly
# ==========================================

        st.subheader(
            "Forecast Demand Trend"
        )

        # Create an interactive line chart
        fig = px.line(

            forecast_df,

            x="hour",

            y="forecasted_demand",

            markers=True,

            title="Taxi Demand Forecast for Zone 79"

        )

        # Customize axis labels
        fig.update_layout(

            xaxis_title="Forecast Hour",

            yaxis_title="Forecasted Demand",

            hovermode="x unified"

        )

        # Display chart in Streamlit
        st.plotly_chart(

            fig,

            width='content'

        )