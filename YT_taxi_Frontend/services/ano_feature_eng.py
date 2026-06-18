class FeatureEngineer:

    def build_features(self, request):

        dt = request.pickup_datetime

        pickup_zone = request.pickup_zone
        drop_zone = request.drop_zone

        hour = dt.hour
        day_of_week = dt.weekday()

        distance = abs(pickup_zone - drop_zone) * 0.8

        # simple proxy features (replace later if needed)
        speed = distance / 15 if distance > 0 else 0
        trip_duration = distance * 3

        return {
            "pickup_zone": pickup_zone,
            "drop_zone": drop_zone,
            "hour": hour,
            "day_of_week": day_of_week,
            "distance": distance,
            "speed": speed,
            "trip_duration": trip_duration
        }