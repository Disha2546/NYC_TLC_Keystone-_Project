from fastapi import FastAPI

from schemas.forecast_schema import (
    ForecastRequest
)

from services.forecasting_service import (
    generate_forecast
)

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

