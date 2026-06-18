import streamlit as st
import requests
import pandas as pd
import numpy as np
import plotly.express as px
import time

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="NYC Taxi Real-Time Dashboard",
    layout="wide"
)

st.title("🚖 NYC Taxi Demand - Real-Time Analytics Dashboard")

API_BASE = "http://localhost:8000"   # change if needed


# =========================
# MOCK DATA (fallback mode)
# =========================
def get_mock_demand():
    zones = [f"Zone {i}" for i in range(1, 11)]
    demand = np.random.randint(20, 200, size=10)
    return pd.DataFrame({"zone": zones, "demand": demand})


def get_mock_forecast():
    t = list(range(10))
    values = np.random.randint(50, 200, size=10)
    return pd.DataFrame({"time": t, "predicted_demand": values})


def get_mock_hotspots():
    return pd.DataFrame({
        "zone": [f"Zone {i}" for i in range(1, 11)],
        "lat": np.random.uniform(40.7, 40.9, 10),
        "lon": np.random.uniform(-74.0, -73.9, 10),
        "demand": np.random.randint(20, 200, 10)
    })


def get_mock_anomalies():
    return [
        "⚠️ Sudden spike in Zone 3",
        "⚠️ Unusual drop in Zone 7"
    ]


# =========================
# SAFE API CALL WRAPPER
# =========================
def safe_get(endpoint, fallback_func):
    try:
        response = requests.get(f"{API_BASE}/{endpoint}", timeout=2)
        if response.status_code == 200:
            return pd.DataFrame(response.json())
    except:
        pass
    return fallback_func()


# =========================
# AUTO REFRESH
# =========================
st_autorefresh = st.empty()


# =========================
# KPI SECTION
# =========================
col1, col2, col3 = st.columns(3)

demand_df = safe_get("live-demand", get_mock_demand)

with col1:
    st.metric("🚖 Total Zones", len(demand_df))

with col2:
    st.metric("📊 Avg Demand", int(demand_df["demand"].mean()))

with col3:
    st.metric("🔥 Max Demand", int(demand_df["demand"].max()))


st.divider()


# =========================
# MAIN LAYOUT
# =========================
col1, col2 = st.columns([2, 1])

# -------------------------
# 📊 Demand Bar Chart
# -------------------------
with col1:
    st.subheader("📊 Zone-wise Demand")

    fig = px.bar(
        demand_df,
        x="zone",
        y="demand",
        color="demand",
        text="demand"
    )
    st.plotly_chart(fig, use_container_width=True)


# -------------------------
# ⚠️ Alerts Panel
# -------------------------
with col2:
    st.subheader("⚠️ Live Alerts")

    anomalies = safe_get("anomalies", lambda: pd.DataFrame({"msg": get_mock_anomalies()}))

    if isinstance(anomalies, pd.DataFrame):
        for a in anomalies.iloc[:, 0]:
            st.warning(a)
    else:
        for a in anomalies:
            st.warning(a)


st.divider()


# =========================
# FORECAST SECTION
# =========================
st.subheader("📈 Demand Forecast (Next 10 Steps)")

forecast_df = safe_get("forecast", get_mock_forecast)

fig2 = px.line(
    forecast_df,
    x="time",
    y="predicted_demand",
    markers=True
)

st.plotly_chart(fig2, use_container_width=True)


st.divider()


# =========================
# HOTSPOT MAP
# =========================
st.subheader("🗺️ Demand Hotspot Map")

hotspots = safe_get("hotspots", get_mock_hotspots)

fig3 = px.scatter_mapbox(
    hotspots,
    lat="lat",
    lon="lon",
    size="demand",
    color="demand",
    zoom=10,
    mapbox_style="open-street-map",
    hover_name="zone"
)

st.plotly_chart(fig3, use_container_width=True)


st.divider()


# =========================
# DECISION SUPPORT ENGINE
# =========================
st.subheader("🎯 Decision Support System")

if len(demand_df) > 0:
    top_zone = demand_df.loc[demand_df["demand"].idxmax(), "zone"]
    low_zone = demand_df.loc[demand_df["demand"].idxmin(), "zone"]

    col1, col2 = st.columns(2)

    with col1:
        st.success(f"📍 Recommended High Demand Zone: {top_zone}")

    with col2:
        st.info(f"📍 Low Demand Zone: {low_zone}")

    st.write("💡 Recommendation:")
    st.write(f"➡️ Deploy more drivers to **{top_zone}**")
    st.write(f"➡️ Reduce allocation in **{low_zone}**")


# =========================
# AUTO REFRESH CONTROL
# =========================
st.caption("🔄 Auto-refreshing every 5 seconds (mock real-time simulation)")
time.sleep(5)
st.rerun()