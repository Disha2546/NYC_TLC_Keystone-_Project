import joblib
import pandas as pd

# Load duration model
duration_model = joblib.load("models/xgb_optimized_model.pkl")


def build_features(input_data: dict):

    df = pd.DataFrame([input_data])

    df["Location_Pair"] = (
        df["PULocationID"].astype(str)
        + "_"
        + df["DOLocationID"].astype(str)
    )

    if "pickup_day" not in df:
        df["pickup_day"] = 15     # default day of month

    if "pickup_dayofweek" not in df:
        df["pickup_dayofweek"] = 2

    if "pickup_month" not in df:
        df["pickup_month"] = 6

    if "is_weekend" not in df:
        df["is_weekend"] = 0

    if "is_night" not in df:
        df["is_night"] = 0

    if "is_rush_hour" not in df:
        df["is_rush_hour"] = 1

    if "RatecodeID" not in df:
        df["RatecodeID"] = 1

    if "cbd_congestion_fee" not in df:
        df["cbd_congestion_fee"] = 0.0

    return df


def predict_trip_duration(input_data):
    """
    input_data is already a dict.
    """

    X = build_features(input_data)

    prediction = duration_model.predict(X)[0]

    return {
        "predicted_duration": float(prediction)
    }