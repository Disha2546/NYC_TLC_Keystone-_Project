import pandas as pd
import numpy as np

def build_features(data: dict):
    df = pd.DataFrame([data])

    # ------------------------
    # TIME FEATURES
    # ------------------------
    df["pickup_hour"] = df["pickup_hour"]
    df["pickup_dayofweek"] = 0  # placeholder (or derive from timestamp)
    df["pickup_month"] = 1      # placeholder (or derive if timestamp exists)

    # ------------------------
    # BOOLEAN FEATURES
    # ------------------------
    df["is_weekend"] = 0
    df["is_night"] = (df["pickup_hour"] < 6).astype(int)
    df["is_rush_hour"] = df["pickup_hour"].isin([7, 8, 9, 17, 18, 19]).astype(int)

    # ------------------------
    # STATIC / DEFAULT FEATURES
    # ------------------------
    df["RatecodeID"] = 1
    df["cbd_congestion_fee"] = 0

    # ------------------------
    # LOCATION FEATURE
    # ------------------------
    df["Location_Pair"] = (
        df["PULocationID"].astype(str) + "_" + df["DOLocationID"].astype(str)
    )

    return df