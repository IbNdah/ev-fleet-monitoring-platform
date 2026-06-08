from edge_gateway.gateway import EdgeGateway


class MockPublisher:
    """
    Fake MQTT publisher used for testing.
    """

    def __init__(self):

        self.topic = None
        self.payload = None

    def publish(
        self,
        topic,
        payload
    ):

        self.topic = topic
        self.payload = payload


def test_process_invalid_payload():

    gateway = EdgeGateway()

    gateway.publisher = MockPublisher()

    payload = {
        "deviceId": "BATT-EV-001",
        "vehicleId": "EV-001",
        "timestamp": "2026-01-01T00:00:00Z",
        "soc": 150,
        "voltage": 3.7,
        "temperature": 30
    }

    gateway.process_message(
        payload
    )

    assert (
        gateway.publisher.topic
        == "evfleet/telemetry/rejected"
    )