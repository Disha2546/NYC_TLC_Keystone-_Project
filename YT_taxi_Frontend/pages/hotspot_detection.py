import streamlit as st
import requests
import pandas as pd
import pydeck as pdk
import folium
from streamlit_folium import folium_static


def show_hotspot_page():

    st.title("🔥 High-Demand Pickup Hotspots")

    top_n = st.slider("Top Hotspots", 5, 50, 20)

    if st.button("Detect Hotspots"):

        payload = {
            "top_n": top_n
        }

        try:
            response = requests.post(
                "http://127.0.0.1:8000/hotspots",
                json={"top_n": top_n}
            )

            # # DEBUG
            # st.write("Status Code:", response.status_code)
            # st.write("Raw Response:", response.text)

            if response.status_code != 200:
                st.error("Backend error occurred")
                st.stop()

            result = response.json()

            if "hotspots" not in result:
                st.error(result.get("error", "Unknown error"))
                st.stop()

            df = pd.DataFrame(result["hotspots"])

            st.success(f"Found {len(df)} hotspots")


            st.dataframe(df)
            
                # ---------------------------
                # MAP VIEW
                # ---------------------------
            nyc_map = folium.Map(
                location=[40.7128, -74.0060],
                zoom_start=11,
                tiles="CartoDB positron"
            )

            for _, row in df.iterrows():

                folium.CircleMarker(
                    location=[row["latitude"], row["longitude"]],
                    radius=8,
                    popup=(
                        f"Zone: {row['Zone']}<br>"
                        f"Borough: {row['Borough']}<br>"
                        f"Pickup Count: {row['pickup_count']:,}"
                    ),
                    color="red",
                    fill=True,
                    fill_opacity=0.8
                ).add_to(nyc_map)
            folium_static(nyc_map, width=1000, height=600)

            # else:
            #     st.error(result["error"])

        except Exception as e:
            st.error(f"Request failed: {e}")