from pydantic import BaseModel, Field

class TripRequest(BaseModel):
    passenger_count: int = Field(..., ge=1, le=6)
    trip_distance: float = Field(..., gt=0)
    pickup_hour: int = Field(..., ge=0, le=23)
    PULocationID: int
    DOLocationID: int