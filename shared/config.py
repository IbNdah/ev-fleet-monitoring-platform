"""
Shared configuration for EV Fleet Monitoring Platform.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# ==========================================
# MQTT
# ==========================================

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

# ==========================================
# Topics
# ==========================================

RAW_TOPIC = os.getenv(
    "RAW_TOPIC",
    "evfleet/telemetry/raw"
)

PROCESSED_TOPIC = os.getenv(
    "PROCESSED_TOPIC",
    "evfleet/telemetry/processed"
)

REJECTED_TOPIC = os.getenv(
    "REJECTED_TOPIC",
    "evfleet/telemetry/rejected"
)


LOG_LEVEL = os.getenv(
    "LOG_LEVEL",
    "INFO"
)


# ==========================================
# AZURE IOT HUB
# ==========================================

IOT_HUB_CONNECTION_STRING = os.getenv(
    "IOT_HUB_CONNECTION_STRING")

DEVICE_ID = os.getenv(
    "DEVICE_ID",
    "ev-fleet-gateway"
)