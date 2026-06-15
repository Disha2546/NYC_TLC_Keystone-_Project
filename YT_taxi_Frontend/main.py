from fastapi import FastAPI

from schemas.forecast_schema import ForecastRequest
from schemas.trip_schema import TripRequest

from services.forecasting_service import (
    generate_forecast
)

from services.trip_prediction import predict_trip_fare_and_duration

app = FastAPI(
    title="NYC Taxi Demand Forecasting API"
)


@app.get("/")
def home():

    return {
        "message":
        "NYC Taxi Demand Forecasting API"
    }


@app.post("/forecast")
def forecast(
    request: ForecastRequest
):

    forecasts = generate_forecast(
        request.forecast_horizon
    )

    return forecasts


@app.post("/predict-trip")
def predict_trip(request: TripRequest):

    try:
        result = predict_trip_fare_and_duration(request.dict())
        return result

    except Exception as e:
        return {
            "error": str(e)
        }