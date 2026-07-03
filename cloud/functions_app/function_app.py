import json
import logging
import os
import time
import uuid

import azure.functions as func
from azure.monitor.opentelemetry import configure_azure_monitor
from services.cosmos_service import CosmosService
from services.fleet_service import FleetService

# -----------------------------------------------------------------------------
# Configure Azure Monitor / Application Insights
# -----------------------------------------------------------------------------

connection_string = os.getenv("APPLICATIONINSIGHTS_CONNECTION_STRING")

if connection_string:
    configure_azure_monitor(
        connection_string=connection_string
    )

# -----------------------------------------------------------------------------
# Logging
# -----------------------------------------------------------------------------

logger = logging.getLogger("evfleet")
logger.setLevel(logging.INFO)

app = func.FunctionApp()


# -----------------------------------------------------------------------------
# Event Hub Trigger
# -----------------------------------------------------------------------------

@app.event_hub_message_trigger(
    arg_name="event",
    event_hub_name="messages/events",
    connection="EventHubConnection",
)
def process_telemetry(event: func.EventHubEvent):

    logger.info("######## VERSION 7.4 ########")

    correlation_id = str(uuid.uuid4())
    function_start = time.perf_counter()

    cosmos = CosmosService()
    payload = {}

    try:

        raw_payload = event.get_body().decode("utf-8")
        payload = json.loads(raw_payload)

        vehicle_id = payload.get("vehicleId", "UNKNOWN")

        logger.info(
            "Telemetry received",
            extra={
                "custom_dimensions": {
                    "vehicleId": vehicle_id,
                    "deviceId": payload.get("deviceId"),
                    "correlationId": correlation_id,
                }
            },
        )

        cosmos_duration = cosmos.save_telemetry(payload)

        function_duration = round(
            (time.perf_counter() - function_start) * 1000,
            2,
        )

        logger.info(
            "Telemetry processed",
            extra={
                "custom_dimensions": {
                    "vehicleId": vehicle_id,
                    "deviceId": payload.get("deviceId"),
                    "batteryState": payload.get("batteryState"),
                    "batterySoc": payload.get("batterySoc"),
                    "batteryTemperature": payload.get("batteryTemperature"),
                    "batteryVoltage": payload.get("batteryVoltage"),
                    "batteryCurrent": payload.get("batteryCurrent"),
                    "cosmosDurationMs": cosmos_duration,
                    "functionDurationMs": function_duration,
                    "correlationId": correlation_id,
                    "status": "SUCCESS",
                }
            },
        )

        logger.info(
            "Telemetry persisted",
            extra={
                "custom_dimensions": {
                    "vehicleId": vehicle_id,
                    "cosmosDurationMs": cosmos_duration,
                    "correlationId": correlation_id,
                }
            },
        )

    except Exception:

        logger.exception(
            "Telemetry processing failed",
            extra={
                "custom_dimensions": {
                    "vehicleId": payload.get("vehicleId", "UNKNOWN"),
                    "correlationId": correlation_id,
                    "status": "FAILED",
                }
            },
        )

        raise
    

# -----------------------------------------------------------------------------
# Fleet Summary API
# -----------------------------------------------------------------------------

@app.route(
    route="fleet/summary",
    methods=["GET"],
    auth_level=func.AuthLevel.FUNCTION,
)
def fleet_summary(req: func.HttpRequest) -> func.HttpResponse:

    logger.info("Fleet Summary API called")

    try:

        fleet = FleetService()

        data = fleet.get_summary()

        return func.HttpResponse(
            json.dumps(data, indent=4),
            mimetype="application/json",
            status_code=200,
        )

    except Exception:

        logger.exception("Fleet Summary API failed")

        return func.HttpResponse(
            "Internal Server Error",
            status_code=500,
        )