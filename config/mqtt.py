import os

MQTT_BROKER = os.getenv(
    "MQTT_BROKER",
    "localhost"
)

MQTT_PORT = int(
    os.getenv(
        "MQTT_PORT",
        "1883"
    )
)

MQTT_KEEPALIVE = int(
    os.getenv(
        "MQTT_KEEPALIVE",
        "60"
    )
)