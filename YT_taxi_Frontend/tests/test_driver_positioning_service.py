import pytest
from services.driver_positioning_service import DriverPositioningService


def test_driver_positioning_basic():

    service = DriverPositioningService()

    sample_input = {
        "PULocationID": 42,
        "predicted_demand": 120.5,
        "revenue_factor": 1.8
    }

    result = service.compute_positioning(sample_input)

    # -------------------------
    # CHECK OUTPUT STRUCTURE
    # -------------------------
    assert "recommended_zone" in result
    assert "score" in result

    # -------------------------
    # CHECK TYPES
    # -------------------------
    assert isinstance(result["recommended_zone"], int)
    assert isinstance(result["score"], float)