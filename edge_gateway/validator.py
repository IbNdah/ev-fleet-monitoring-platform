class TelemetryValidator:
    """
    Validates incoming telemetry payloads.
    """

    REQUIRED_FIELDS = [
        "deviceId",
        "vehicleId",
        "timestamp",
        "soc",
        "voltage",
        "temperature"
    ]

    @staticmethod
    def validate(data):
        """
        Validate telemetry payload.

        Returns:
            bool: True if valid, False otherwise.
        """

        # Check required fields
        for field in TelemetryValidator.REQUIRED_FIELDS:

            if field not in data:
                return False

        # Validate SOC
        if not 0 <= data["soc"] <= 100:
            return False

        # Validate temperature
        if not -40 <= data["temperature"] <= 120:
            return False

        # Validate voltage
        if data["voltage"] <= 0:
            return False

        return True


# -----------------------------------
# Quick test
# -----------------------------------

if __name__ == "__main__":

    telemetry = {
        "deviceId": "BATT-EV-001",
        "vehicleId": "EV-001",
        "timestamp": "2026-06-05T12:00:00Z",
        "soc": 80,
        "voltage": 3.7,
        "temperature": 30
    }

    print(
        TelemetryValidator.validate(
            telemetry
        )
    )