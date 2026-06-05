import json
import paho.mqtt.client as mqtt

broker = "localhost"
topic = "evfleet/telemetry"

telemetry = {
    "vehicle_id": "EV-001",
    "state": "DRIVING",
    "speed": 78,
    "battery_soc": 84,
    "temperature": 31.2
}

client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2,
    client_id="test-publisher"
)

client.connect(broker, 1883, 60)

payload = json.dumps(telemetry)

client.publish(topic, payload)

print(f"Sent: {payload}")

client.disconnect()