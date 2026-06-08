from edge_gateway.validator import (
    TelemetryValidator
)


def test_valid_payload():

    payload = {
        "deviceId": "BATT-EV-001",
        "vehicleId": "EV-001",
        "timestamp": "2026-01-01T00:00:00Z",
        "soc": 80,
        "voltage": 3.7,
        "temperature": 25
    }

    assert (
        TelemetryValidator.validate(
            payload
        ) is True
    )


def test_invalid_soc():

    payload = {
        "deviceId": "BATT-EV-001",
        "vehicleId": "EV-001",
        "timestamp": "2026-01-01T00:00:00Z",
        "soc": 150,
        "voltage": 3.7,
        "temperature": 25
    }

    assert (
        TelemetryValidator.validate(
            payload
        ) is False
    )