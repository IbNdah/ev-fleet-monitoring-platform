import json
import logging

import azure.functions as func

app = func.FunctionApp()


@app.event_hub_message_trigger(
    arg_name="event",
    event_hub_name="messages/events",
    connection="EventHubConnection"
)
def process_telemetry(event: func.EventHubEvent):

    try:
        raw_payload = event.get_body().decode("utf-8")

        payload = json.loads(raw_payload)

        vehicle_id = payload.get("vehicleId", "unknown")

        logging.info("========== TELEMETRY RECEIVED ==========")
        logging.info(payload)
        logging.info(
            f"Telemetry received from vehicle: {vehicle_id}"
        )
        logging.info("========================================")

    except Exception as ex:
        logging.error(
            f"Processing failed: {str(ex)}"
        )