from pydantic import BaseModel

class DashboardRequest(BaseModel):
    forecast_horizon: int = 10
    top_n_hotspots: int = 5