from azure.iot.device import (
    IoTHubDeviceClient,
    Message
)


class IoTHubConnector:

    def __init__(self, connection_string):

        self.connection_string = connection_string
        self.client = None

    def connect(self):

        self.client = (
            IoTHubDeviceClient.create_from_connection_string(
                self.connection_string
            )
        )

        self.client.connect()

    def send_telemetry(self, payload):

        message = Message(payload)

        self.client.send_message(
            message
        )

    def disconnect(self):

        if self.client:
            self.client.disconnect()