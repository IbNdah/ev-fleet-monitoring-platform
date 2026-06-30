from edge_gateway.translator import TelemetryTranslator


def test_translation():

    payload = {
        "deviceId": "BATT-EV-001",
        "temperature": 30,
        "current": 5,
        "voltage": 3.7,
        "soc": 80,
        "state": "DRIVING",
        "faultCode": None,
        "timestamp": "2026-01-01T00:00:00Z",
        "vehicleId": "EV-001",
        "vehicleState": "DRIVING",
    }

    translated = TelemetryTranslator.translate(payload)

    assert translated["batterySoc"] == 80

    assert translated["vehicleId"] == "EV-001"

    assert translated["schemaVersion"] == "1.0"
