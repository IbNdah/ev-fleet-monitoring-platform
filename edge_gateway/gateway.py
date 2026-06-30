import json
import logging

from cloud.iot_hub_connector import IoTHubConnector
from edge_gateway.mqtt_publisher import MQTTPublisher
from edge_gateway.mqtt_subscriber import MQTTSubscriber
from edge_gateway.translator import TelemetryTranslator
from edge_gateway.validator import TelemetryValidator
from shared.config import (
    IOT_HUB_CONNECTION_STRING,
    LOG_LEVEL,
    PROCESSED_TOPIC,
    RAW_TOPIC,
    REJECTED_TOPIC,
)

logging.basicConfig(level=LOG_LEVEL, format="%(asctime)s [%(levelname)s] %(message)s")


class EdgeGateway:
    """
    Edge Gateway responsible for:

    - Receiving raw telemetry
    - Validating payloads
    - Translating payloads
    - Republishing processed telemetry
    - Forwarding telemetry to Azure IoT Hub
    """

    def __init__(self):

        self.publisher = MQTTPublisher()
        self.publisher.connect()

        self.iot_hub = IoTHubConnector(IOT_HUB_CONNECTION_STRING)
        self.iot_hub.connect()

        self.subscriber = MQTTSubscriber(self.process_message)

    def process_message(self, payload):
        """
        Process raw telemetry through
        validation and translation pipeline.
        """

        logging.info("Received raw telemetry")

        if not TelemetryValidator.validate(payload):

            logging.warning("Invalid telemetry received")

            self.publisher.publish(REJECTED_TOPIC, payload)

            return

        translated = TelemetryTranslator.translate(payload)

        self.publisher.publish(PROCESSED_TOPIC, translated)

        logging.info("Published processed telemetry")

        try:
            logging.info(f"Sending vehicle {translated['vehicleId']}")

            self.iot_hub.send_telemetry(json.dumps(translated))

            logging.info("Sent telemetry to Azure IoT Hub")

        except Exception as ex:

            logging.error(f"IoT Hub send failed: {ex}")

    def start(self):
        """
        Start Edge Gateway.
        """

        logging.info("Edge Gateway started")

        logging.info(f"Listening on: {RAW_TOPIC}")

        logging.info(f"Publishing to: {PROCESSED_TOPIC}")

        self.subscriber.start(RAW_TOPIC)


if __name__ == "__main__":

    gateway = EdgeGateway()
    gateway.start()
