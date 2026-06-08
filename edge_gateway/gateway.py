import logging

from edge_gateway.validator import TelemetryValidator
from edge_gateway.translator import TelemetryTranslator
from edge_gateway.mqtt_publisher import MQTTPublisher
from edge_gateway.mqtt_subscriber import MQTTSubscriber


RAW_TOPIC = "evfleet/telemetry/raw"
PROCESSED_TOPIC = "evfleet/telemetry/processed"
REJECTED_TOPIC = "evfleet/telemetry/rejected"


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


class EdgeGateway:
    """
    Edge Gateway responsible for:

    - Receiving raw telemetry
    - Validating payloads
    - Translating payloads
    - Republishing processed telemetry
    """

    def __init__(self):

        self.publisher = MQTTPublisher()
        self.publisher.connect()

        self.subscriber = MQTTSubscriber(
            self.process_message
        )

    def process_message(self, payload):
        """
        Process raw telemetry through
        validation and translation pipeline.
        """

        logging.info(
            "Received raw telemetry"
        )

        if not TelemetryValidator.validate(
            payload
        ):

            logging.warning(
                "Invalid telemetry received"
            )

            self.publisher.publish(
                REJECTED_TOPIC,
                payload
            )

            return

        translated = (
            TelemetryTranslator.translate(
                payload
            )
        )

        self.publisher.publish(
            PROCESSED_TOPIC,
            translated
        )

        logging.info(
            "Published processed telemetry"
        )

    def start(self):
        """
        Start Edge Gateway.
        """

        logging.info(
            "Edge Gateway started"
        )

        logging.info(
            f"Listening on: {RAW_TOPIC}"
        )

        logging.info(
            f"Publishing to: {PROCESSED_TOPIC}"
        )

        self.subscriber.start(
            RAW_TOPIC
        )


if __name__ == "__main__":

    gateway = EdgeGateway()

    gateway.start()