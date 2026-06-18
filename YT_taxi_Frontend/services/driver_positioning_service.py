class DriverPositioningService:

    def __init__(self):
        pass

    def compute_positioning(self, data):

        current_zone = data["current_zone"]
        hour = data["hour"]
        max_distance =data["max_distance"]
        zones = range(
            max(1, current_zone - int(max_distance)),
            min(264, current_zone + int(max_distance) + 1)
        )

        results = []

        for z in zones:

            demand = (hour * 10) + (z * 5)

            revenue = max(10, 100 - abs(z - current_zone) * 2)

            score = demand * revenue

            results.append({
                "zone": z,
                "score": round(score, 2)
            })

        results = sorted(
            results,
            key=lambda x: x["score"],
            reverse=True
        )

       
        if not results:
            return {
                "current_zone": current_zone,
                "recommended_zone": best["zone"],
                "score": best["score"],
                "top_zones": results[:3]
            }
        best = results[0]