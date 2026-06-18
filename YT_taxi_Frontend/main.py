from fastapi import FastAPI

from schemas.forecast_schema import ForecastRequest
from schemas.trip_schema import TripRequest
from schemas.hotspot_schema import HotspotRequest

from services.forecasting_service import generate_forecast
from services.trip_prediction import predict_trip_duration
from services.hotspot_services import get_hotspots

from schemas.driver_positioning_schema import DriverPositioningRequest
from services.driver_positioning_service import DriverPositioningService

from schemas.anomaly_schema import AnomalyRequest, AnomalyResponse
from services.anomaly_service import AnomalyService



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


from schemas.trip_schema import TripRequest
from services.trip_prediction import predict_trip_duration

@app.post("/predict-duration")
def predict_duration_api(request: TripRequest):

    try:
        input_data = request.model_dump()

        result = predict_trip_duration(input_data)

        return result

    except Exception as e:
        return {
            "error": str(e)
        }
    

@app.post("/hotspots")
def hotspots(
    request: HotspotRequest
):

    try:
        results = get_hotspots(request.top_n)

        return {
            "hotspots": results
        }

    except Exception as e:

        return {
            "error": str(e)
        }
    

driver_service = DriverPositioningService()

@app.post("/recommend-driver-position")
def recommend_driver_position(
    request: DriverPositioningRequest
):

    result = driver_service.compute_positioning(
        request.model_dump()
    )

    return result

service = None


@app.on_event("startup")
def load_model():
    global service
    service = AnomalyService()


@app.post("/anomaly/predict", response_model=AnomalyResponse)
def detect_anomaly(request: AnomalyRequest):
    return service.predict(request)

@app.get("/live-demand")
def live_demand():
    """
    Simulated real-time demand (you can later replace with DB or streaming data)
    """

    import random

    zones = [f"Zone {i}" for i in range(1, 11)]

    data = [
        {
            "zone": zone,
            "demand": random.randint(20, 200)
        }
        for zone in zones
    ]

    return data