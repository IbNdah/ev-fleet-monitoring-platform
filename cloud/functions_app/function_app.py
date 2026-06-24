import json
import logging
import time
import uuid

import azure.functions as func

from services.cosmos_service import CosmosService


app = func.FunctionApp()

cosmos = CosmosService()


@app.event_hub_message_trigger(
    arg_name="event",
    event_hub_name="messages/events",
    connection="EventHubConnection"
)
def process_telemetry(event: func.EventHubEvent):

    correlation_id = str(uuid.uuid4())

    start = time.time()

    try:

        raw_payload = event.get_body().decode(
            "utf-8"
        )

        payload = json.loads(raw_payload)

        vehicle_id = payload.get(
            "vehicleId",
            "unknown"
        )

        cosmos_ms = cosmos.save_telemetry(
            payload
        )

        duration_ms = round(
            (time.time() - start) * 1000,
            2
        )

        logging.info(
            "\n"
            "====================================\n"
            f"Vehicle      : {vehicle_id}\n"
            f"Battery      : {payload.get('batterySoc')} %\n"
            f"Temperature  : {payload.get('batteryTemperature')} °C\n"
            f"Cosmos Write : {cosmos_ms} ms\n"
            f"Duration     : {duration_ms} ms\n"
            f"Correlation  : {correlation_id}\n"
            "===================================="
        )

    except Exception as ex:

        logging.error(
            {
                "correlationId": correlation_id,
                "error": str(ex)
            },
            exc_info=True
        )