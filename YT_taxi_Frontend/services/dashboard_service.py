from services.forecasting_service import generate_forecast
from services.hotspot_services import get_hotspots


class DashboardService:

    def get_dashboard_data(self):

        # Use Case 1
        forecast = generate_forecast(10)

        # Use Case 3
        hotspots = get_hotspots(5)

        demand_data = [
            {
                "zone": h["zone"],
                "demand": h["pickup_count"]
            }
            for h in hotspots
        ]

        # Use Case 5 (placeholder)
        anomaly_data = [
            {
                "message": "No major anomalies detected"
            }
        ]

        recommendation = self.generate_recommendation(
            demand_data
        )

        return {
            "forecast": forecast,
            "hotspots": hotspots,
            "anomalies": anomaly_data,
            "recommendation": recommendation
        }

    def generate_recommendation(
        self,
        demand_data
    ):

        if not demand_data:
            return "No demand data available"

        best_zone = max(
            demand_data,
            key=lambda x: x["demand"]
        )

        return (
            f"Deploy additional drivers to "
            f"{best_zone['zone']}"
        )