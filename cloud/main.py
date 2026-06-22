import logging
import paho.mqtt.client as mqtt

from shared.config import (
    MQTT_BROKER,
    MQTT_PORT,
    PROCESSED_TOPIC,
    IOT_HUB_CONNECTION_STRING
)

from cloud.iot_hub_connector import (IoTHubConnector)


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# Create Azure IoT Hub connector
iot_connector = IoTHubConnector(
    IOT_HUB_CONNECTION_STRING
)

iot_connector.connect()

def on_connect(client, userdata, flags, rc):
    """
    Called when MQTT connects to the broker.
    """

    if rc == 0:

        logging.info(f"Connected to MQTT Broker: {MQTT_BROKER}")
        client.subscribe(PROCESSED_TOPIC)
        logging.info(f"Subscribed to topic: {PROCESSED_TOPIC}")

    else:

        logging.error(f"MQTT connection failed: {rc}")


def on_message(client, userdata, msg):
    
    """
    Called when a message is received from MQTT.
    """

    try:

        logging.info("Telemetry received from MQTT")
        iot_connector.send_telemetry(payload)
        logging.info("Telemetry sent to Azure IoT Hub")

    except Exception as ex:

        logging.error(f"Failed to send telemetry: {ex}")


# Create MQTT client
mqtt_client = mqtt.Client()

mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message


# Connect to MQTT broker
mqtt_client.connect(MQTT_BROKER, MQTT_PORT)
logging.info("Cloud Connector started")
mqtt_client.loop_forever()