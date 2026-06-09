import os

IOT_HUB_CONNECTION_STRING = os.getenv(
    "IOT_HUB_CONNECTION_STRING",
    ""
)

DEVICE_ID = os.getenv(
    "DEVICE_ID",
    "ev-fleet-gateway"
)