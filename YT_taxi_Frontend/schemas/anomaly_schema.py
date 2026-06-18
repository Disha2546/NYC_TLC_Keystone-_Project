from pydantic import BaseModel
from datetime import datetime


class AnomalyRequest(BaseModel):
    pickup_zone: int
    drop_zone: int
    pickup_datetime: datetime


class AnomalyResponse(BaseModel):
    anomaly_score: float
    label: str
    reasons: list[str]