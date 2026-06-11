import json

from azure.iot.device import (
    IoTHubDeviceClient,
    Message
)


class IoTHubConnector:
    """
    Sends telemetry to Azure IoT Hub.
    """

    def __init__(
        self,
        connection_string: str
    ):

        self.client = (
            IoTHubDeviceClient.create_from_connection_string(
                connection_string
            )
        )

    def connect(self):
        """
        Connect to Azure IoT Hub.
        """

        self.client.connect()


    
    
    
    def send_telemetry(
        self,
        payload: str
    ):
        """
        Send telemetry message to Azure IoT Hub.
        """

        message = Message(
            payload
        )

        self.client.send_message(
            message
        )

    def disconnect(self):
        """
        Disconnect from Azure IoT Hub.
        """

        self.client.disconnect()