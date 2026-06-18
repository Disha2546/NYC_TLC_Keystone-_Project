import streamlit as st
import requests
import pandas as pd
import plotly.express as px

API_URL = "http://localhost:8000/dashboard"

def show_dashboard_page():

    st.title("🚖 Real-Time Analytics & Decision Support Dashboard")

    try:

        data = requests.get(API_URL).json()

        forecast_df = pd.DataFrame(data["forecast"])
        hotspot_df = pd.DataFrame(data["hotspots"])

        # =========================
        # KPI SECTION
        # =========================

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "📈 Forecast Records",
                len(forecast_df)
            )

        with col2:
            st.metric(
                "🔥 Hotspots",
                len(hotspot_df)
            )

        with col3:
            st.metric(
                "🚖 Peak Demand",
                int(hotspot_df["pickup_count"].max())
            )

        st.divider()

        # =========================
        # FORECAST CHART
        # =========================

        st.subheader("📈 Demand Forecast")

        fig1 = px.line(
            forecast_df,
            x="hour",
            y="forecasted_demand",
            markers=True
        )

        st.plotly_chart(
            fig1,
            use_container_width=True
        )

        st.divider()

        # =========================
        # HOTSPOTS
        # =========================

        st.subheader("🔥 Top Pickup Hotspots")

        st.dataframe(
            hotspot_df,
            use_container_width=True
        )

        st.divider()

        # =========================
        # ALERTS
        # =========================

        st.subheader("🚨 Alerts")

        for item in data["anomalies"]:
            st.warning(item["message"])

        st.divider()

        # =========================
        # DECISION SUPPORT
        # =========================

        st.subheader("🎯 Decision Support Recommendation")

        top_zone = hotspot_df.sort_values(
            by="pickup_count",
            ascending=False
        ).iloc[0]

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Recommended Zone",
                top_zone["zone"]
            )

        with col2:
            st.metric(
                "Expected Demand",
                int(top_zone["pickup_count"])
            )

        with col3:
            st.metric(
                "Priority",
                "HIGH"
            )

        st.success(
            f"Deploy additional drivers to {top_zone['zone']} "
            f"to maximize trip opportunities."
        )

    except Exception as e:

        st.error(
            f"Dashboard API Error: {e}"
        )
