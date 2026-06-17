import sys
from pathlib import Path

sys.path.append(
    str(
        Path(__file__).resolve().parent.parent
    )
)

from main import app
from fastapi.testclient import TestClient
from services.hotspot_services import get_hotspots

client = TestClient(app)


def test_get_hotspots():

    hotspots = get_hotspots(5)

    assert isinstance(hotspots, list)
    assert len(hotspots) <= 5

    if hotspots:

        hotspot = hotspots[0]

        assert "latitude" in hotspot
        assert "longitude" in hotspot
        assert "pickup_count" in hotspot


def test_hotspots_endpoint():

    response = client.post(
        "/hotspots",
        json={
            "top_n": 5
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "hotspots" in data
    assert isinstance(data["hotspots"], list)
    assert len(data["hotspots"]) <= 5