import json
import paho.mqtt.client as mqtt


class MQTTSubscriber:
    """
    Subscribes to MQTT topics and
    forwards received payloads
    to a callback function.
    """

    def __init__(
        self,
        message_handler,
        broker_host="localhost",
        broker_port=1883
    ):

        self.message_handler = (
            message_handler
        )

        self.client = mqtt.Client(
            mqtt.CallbackAPIVersion.VERSION2
        )

        self.broker_host = broker_host
        self.broker_port = broker_port

    def on_message(
        self,
        client,
        userdata,
        message
    ):

        payload = json.loads(
            message.payload.decode()
        )

        self.message_handler(
            payload
        )

    def start(
        self,
        topic
    ):

        self.client.on_message = (
            self.on_message
        )

        self.client.connect(
            self.broker_host,
            self.broker_port
        )

        self.client.subscribe(
            topic
        )

        print(
            f"Subscribed to: {topic}"
        )

        self.client.loop_forever()


# -----------------------------------
# Quick test
# -----------------------------------

def test_handler(payload):

    print(payload)


if __name__ == "__main__":

    subscriber = MQTTSubscriber(
        test_handler
    )

    subscriber.start(
        "evfleet/telemetry/raw"
    )