import pandas as pd


def get_hotspots(top_n: int):

    hotspot_df = pd.read_csv(
        "data/zone_hotspot_coordinates.csv"
    )

    hotspot_df = hotspot_df.sort_values(
        by="pickup_count",
        ascending=False
    )

    hotspot_df = hotspot_df.head(top_n)

    return hotspot_df.to_dict(
        orient="records"
    )