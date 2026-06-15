from services.trip_prediction import predict_trip_fare_and_duration


def test_trip_prediction():

    sample_input = {
        "passenger_count": 2,
        "trip_distance": 5.2,
        "pickup_hour": 14,
        "PULocationID": 79,
        "DOLocationID": 75
    }

    result = predict_trip_fare_and_duration(sample_input)

    assert "fare" in result
    assert "duration_minutes" in result

    assert result["fare"] > 0
    assert result["duration_minutes"] > 0

    print("Trip prediction test passed ✅")


if __name__ == "__main__":
    test_trip_prediction()