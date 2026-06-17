from pydantic import BaseModel

class DriverPositioningRequest(BaseModel):
    current_zone: int
    hour: int
    day_of_week: str
    max_distance: float
    top_zones_only: bool = False