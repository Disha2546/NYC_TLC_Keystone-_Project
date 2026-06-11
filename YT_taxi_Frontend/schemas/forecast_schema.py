from pydantic import BaseModel, Field

# Data Validtion using Pydantic
class ForecastRequest(BaseModel):

    forecast_horizon: int = Field(
        ...,
        ge=24,
        le=168,
        description="Forecast horizon in hours"
    )