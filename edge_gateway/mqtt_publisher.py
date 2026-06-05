import json
import paho.mqtt.client as mqtt


class MQTTPublisher:
    """Publishes telemetry data to an MQTT broker."""

    def __init__(
        self,
        broker_host="localhost",
        broker_port=1883
    ):

        self.client = mqtt.Client(
            mqtt.CallbackAPIVersion.VERSION2
        )

        self.broker_host = broker_host
        self.broker_port = broker_port

    def connect(self):
        """Connect to the MQTT broker."""

        self.client.connect(
            self.broker_host,
            self.broker_port
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
        
# Test        
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