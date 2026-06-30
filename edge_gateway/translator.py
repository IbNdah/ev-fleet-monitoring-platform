from datetime import UTC, datetime


class TelemetryTranslator:
    """
    Translates raw telemetry into
    a normalized telemetry schema.
    """

    @staticmethod
    def translate(data):

        return {
            "schemaVersion": "1.0",
            "vehicleId": data["vehicleId"],
            "deviceId": data["deviceId"],
            "vehicleState": data["vehicleState"],
            "batteryState": data["state"],
            "batterySoc": data["soc"],
            "batteryTemperature": data["temperature"],
            "batteryVoltage": data["voltage"],
            "batteryCurrent": data["current"],
            "faultCode": data["faultCode"],
            "telemetryTimestamp": data["timestamp"],
            "processedTimestamp": datetime.now(UTC).isoformat(),
        }


# -----------------------------------
# Quick test
# -----------------------------------

if __name__ == "__main__":

    telemetry = {
        "deviceId": "BATT-EV-001",
        "temperature": 31.4,
        "current": -0.04,
        "voltage": 3.67,
        "soc": 79.77,
        "state": "DRIVING",
        "faultCode": None,
        "timestamp": "2026-06-05T16:08:20.227267+00:00",
        "vehicleId": "EV-001",
        "vehicleState": "DRIVING",
    }

    translated = TelemetryTranslator.translate(telemetry)

    print(translated)
