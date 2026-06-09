import json
import paho.mqtt.client as mqtt

from shared.config import (
    MQTT_BROKER,
    MQTT_PORT,
    MQTT_KEEPALIVE
)


class MQTTPublisher:
    """Publishes telemetry data to an MQTT broker."""

    def __init__(self):

        self.client = mqtt.Client(
            mqtt.CallbackAPIVersion.VERSION2
        )

    def connect(self):
        """Connect to the MQTT broker."""

        self.client.connect(
            MQTT_BROKER,
            MQTT_PORT,
            MQTT_KEEPALIVE
        )

    def publish(self, topic, payload):
        """Publish telemetry data."""

        self.client.publish(
            topic,
            json.dumps(payload)
        )

    def disconnect(self):
        """Disconnect from the MQTT broker."""

        self.client.disconnect()


# -----------------------------------
# Quick test
# -----------------------------------

if __name__ == "__main__":

    publisher = MQTTPublisher()

    publisher.connect()

    publisher.publish(
        "evfleet/test",
        {
            "message": "hello mqtt"
        }
    )

    publisher.disconnect()