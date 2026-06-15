import joblib
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

fare_obj = joblib.load(
    os.path.join(BASE_DIR, "models", "fare_prediction_pipeline.pkl")
)

duration_model = joblib.load(
    os.path.join(BASE_DIR, "models", "final_xgboost_model.pkl")
)

# 🔥 FIX HERE
fare_model = fare_obj["model"]


def predict_trip_fare_and_duration(data: dict):

    X = pd.DataFrame([data])

    fare = fare_model.predict(X)[0]
    duration = duration_model.predict(X)[0]

    return {
        "fare": round(float(fare), 2),
        "duration_minutes": round(float(duration), 2)
    }