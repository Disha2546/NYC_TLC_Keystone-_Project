# ==========================================================
# NYC Taxi Demand Forecasting - Forecasting Service
# ==========================================================

import pandas as pd
import numpy as np
import joblib
import json
from pathlib import Path


# ==========================================================
# Define File Paths
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = (
    BASE_DIR
    / "models"
    / "final_xgboost_model.pkl"
)

FEATURE_PATH = (
    BASE_DIR
    / "config"
    / "feature_order.json"
)

DATA_PATH = (
    BASE_DIR
    / "data"
    / "hourly_demand.parquet"
)


# ==========================================================
# Load Model
# ==========================================================

def load_model():

    return joblib.load(
        MODEL_PATH
    )


# ==========================================================
# Load Historical Data
# ==========================================================

def load_data():

    return pd.read_parquet(
        DATA_PATH
    )


# ==========================================================
# Load Feature Order
# ==========================================================

def load_feature_order():

    with open(
        FEATURE_PATH,
        "r"
    ) as file:

        return json.load(
            file
        )


# ==========================================================
# Forecast Function
# ==========================================================

def generate_forecast(
    forecast_horizon: int
):

    model = load_model()

    hourly_df = load_data()

    feature_order = load_feature_order()

    ZONE_ID = 79

    zone_data = (

        hourly_df[
            hourly_df[
                "PULocationID"
            ] == ZONE_ID
        ]

        .sort_values(
            "hour"
        )

        .reset_index(
            drop=True
        )

    )

    zone_data = zone_data.iloc[:-1]

    history = (
        zone_data[
            "demand"
        ].tolist()
    )

    last_timestamp = (
        zone_data[
            "hour"
        ].max()
    )

    future_predictions = []

    future_hours = []

    for step in range(
        forecast_horizon
    ):

        future_time = (

            last_timestamp

            +

            pd.Timedelta(
                hours=step + 1
            )

        )

        lag_1 = history[-1]

        lag_24 = history[-24]

        lag_168 = history[-168]

        rolling_mean_24 = np.mean(
            history[-24:]
        )

        rolling_mean_168 = np.mean(
            history[-168:]
        )

        features = pd.DataFrame({

            "PULocationID": [
                ZONE_ID
            ],

            "hour_of_day": [
                future_time.hour
            ],

            "day_of_week": [
                future_time.dayofweek
            ],

            "day_name": [
                future_time.dayofweek
            ],

            "month": [
                future_time.month
            ],

            "week": [
                future_time.isocalendar().week
            ],

            "is_weekend": [

                int(
                    future_time.dayofweek >= 5
                )

            ],

            "lag_1": [
                lag_1
            ],

            "lag_24": [
                lag_24
            ],

            "lag_168": [
                lag_168
            ],

            "rolling_mean_24": [
                rolling_mean_24
            ],

            "rolling_mean_168": [
                rolling_mean_168
            ]

        })

        features = features[
            feature_order
        ]

        prediction = (
            model.predict(
                features
            )[0]
        )

        prediction = max(
            0,
            prediction
        )

        future_predictions.append(
            int(
                round(
                    prediction
                )
            )
        )

        future_hours.append(
            future_time
        )

        history.append(
            prediction
        )

    forecast_df = pd.DataFrame({

        "hour": future_hours,

        "forecasted_demand":
        future_predictions

    })

    return forecast_df.to_dict(
        orient="records"
    )