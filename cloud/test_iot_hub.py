from azure.iot.device import (
    IoTHubDeviceClient,
    Message
)

from shared.config import (
    IOT_HUB_CONNECTION_STRING
)


client = (
    IoTHubDeviceClient.create_from_connection_string(
        IOT_HUB_CONNECTION_STRING
    )
)

print("Connecting...")

client.connect()

print("Connected")

message = Message(
    '{"test":"hello azure"}'
)

client.send_message(
    message
)

print("Message sent")
client.disconnect()
print("Disconnected")