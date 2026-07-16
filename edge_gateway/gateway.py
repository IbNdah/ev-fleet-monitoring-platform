# region Imports

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

# endregion


# region Logging
logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

# endregion


# region Edge Gateway
class EdgeGateway:
    """
    EV Fleet Monitoring Platform

    Edge Gateway

    Responsibilities
    ----------------
    Process incoming telemetry before forwarding it
    to Azure IoT Hub.

    Processing Pipeline
    -------------------
    1. Receive MQTT telemetry
    2. Validate payload
    3. Translate payload
    4. Publish processed telemetry
    5. Forward telemetry to Azure IoT Hub

    Architecture
    ------------
    MQTT Broker
            │
            ▼
       Edge Gateway
            │
      Validation
            │
      Translation
            │
      MQTT Processed Topic
            │
            ▼
       Azure IoT Hub
    """

    # endregion

    # region Constructor

    def __init__(self):
        """
        Initialize all gateway components.
        """

        self.publisher = MQTTPublisher()
        self.publisher.connect()

        self.iot_hub = IoTHubConnector(
            IOT_HUB_CONNECTION_STRING,
        )
        self.iot_hub.connect()

        self.subscriber = MQTTSubscriber(
            self.process_message,
        )

    # endregion

    # region Processing Pipeline
    def process_message(self, payload):
        """
        Process one incoming telemetry message.

        Workflow
        --------
        1. Validate payload.
        2. Translate payload.
        3. Publish processed telemetry.
        4. Forward telemetry to Azure IoT Hub.
        """

        logging.info("Received raw telemetry")

        # -----------------------------------------
        # Validation
        # -----------------------------------------

        if not TelemetryValidator.validate(payload):

            logging.warning("Invalid telemetry received")

            self.publisher.publish(
                REJECTED_TOPIC,
                payload,
            )

            return

        # -----------------------------------------
        # Translation
        # -----------------------------------------

        translated = TelemetryTranslator.translate(
            payload,
        )

        # -----------------------------------------
        # Publish processed telemetry
        # -----------------------------------------

        self.publisher.publish(
            PROCESSED_TOPIC,
            translated,
        )

        logging.info("Published processed telemetry")

        # -----------------------------------------
        # Azure IoT Hub
        # -----------------------------------------

        try:

            logging.info(f"Sending vehicle {translated['vehicleId']}")

            self.iot_hub.send_telemetry(
                json.dumps(translated),
            )

            logging.info("Telemetry sent to Azure IoT Hub")

        except Exception as ex:

            logging.exception(f"Azure IoT Hub error: {ex}")

    # endregion

    # region Public API

    def start(self):
        """
        Start the Edge Gateway.
        """

        logging.info("Edge Gateway started")

        logging.info(f"Listening on: {RAW_TOPIC}")

        logging.info(f"Publishing to: {PROCESSED_TOPIC}")

        self.subscriber.start(
            RAW_TOPIC,
        )

    # endregion


# endregion


# region Entry Point
if __name__ == "__main__":

    gateway = EdgeGateway()
    gateway.start()

# endregion
