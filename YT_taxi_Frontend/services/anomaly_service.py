import joblib
import numpy as np
import json
import os


class AnomalyService:

    def __init__(self):

        self.model = joblib.load("models/isolation_forest.pkl")

        feature_path = "/home/ed/Desktop/NYC_Taxi_Demand_Forecasting/YT_taxi_Frontend/config/anomaly_feature.json"

        with open(feature_path, "r") as f:
            self.feature_order = json.load(f)

    def build_features(self, request):

        dt = request.pickup_datetime

        base_features = {
            "passenger_count": 1,
            "passenger_missing": 0,
            "trip_distance": abs(request.pickup_zone - request.drop_zone) * 0.8,
            "trip_duration": 10,
            "speed": 1.5,
            "fare_amount": 20,
            "tip_amount": 3,
            "total_amount": 25,
            "fare_per_mile": 2,
            "fare_per_minute": 1,
            "tip_percentage": 10,
            "revenue_per_minute": 2,
            "extra_charges": 0,
            "pickup_frequency": 5,
            "dropoff_frequency": 5,
            "route_frequency": 3,
            "hour_sin": np.sin(2 * np.pi * dt.hour / 24),
            "hour_cos": np.cos(2 * np.pi * dt.hour / 24),
            "is_weekend": 1 if dt.weekday() >= 5 else 0,
            "is_night_trip": 1 if dt.hour >= 22 or dt.hour <= 5 else 0,
            "RatecodeID": 1,
            "payment_type": 1
        }

        return base_features

    def predict(self, request):

        features = self.build_features(request)

        X = np.array([features[f] for f in self.feature_order]).reshape(1, -1)

        score_raw = self.model.decision_function(X)[0]

        anomaly_score = float(1 - (score_raw + 1) / 2)

        label = "Anomaly" if anomaly_score > 0.75 else "Normal"

        return {
            "anomaly_score": anomaly_score,
            "label": label,
            "reasons": self.explain(features, anomaly_score)
        }

    def explain(self, features, score):

        reasons = []

        if score > 0.8:
            reasons.append("Strong deviation from normal patterns")

        if features["is_night_trip"]:
            reasons.append("Night-time travel detected")

        if features["trip_distance"] < 1:
            reasons.append("Very short trip anomaly")

        return reasons