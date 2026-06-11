import sys
from pathlib import Path

sys.path.append(
    str(
        Path(__file__).resolve().parent.parent
    )
)

from main import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_forecast():

    response = client.post(
        "/forecast",
        json={
            "forecast_horizon": 24
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 24