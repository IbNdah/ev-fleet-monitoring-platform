import json
import logging
import os
import time
import uuid

import azure.functions as func
from azure.monitor.opentelemetry import configure_azure_monitor
from services.cosmos_service import CosmosService

# -----------------------------------------------------------------------------
# Configure Azure Monitor / Application Insights
# -----------------------------------------------------------------------------

if os.getenv("APPLICATIONINSIGHTS_CONNECTION_STRING"):
    configure_azure_monitor()


app = func.FunctionApp()

logger = logging.getLogger(__name__)


# -----------------------------------------------------------------------------
# Event Hub Trigger
# -----------------------------------------------------------------------------


@app.event_hub_message_trigger(
    arg_name="event", event_hub_name="messages/events", connection="EventHubConnection"
)
def process_telemetry(event: func.EventHubEvent):
    """
    Processes incoming telemetry from Azure IoT Hub.

    Responsibilities
    ----------------
    1. Decode incoming Event Hub message
    2. Parse JSON payload
    3. Persist telemetry into Cosmos DB
    4. Publish structured logs to Application Insights
    """

    logger.info("########* VERSION 7.0 *########")

    correlation_id = str(uuid.uuid4())
    function_start = time.perf_counter()

    cosmos = CosmosService()

    payload = {}

    try:

        # ---------------------------------------------------------------------
        # Decode Event Hub message
        # ---------------------------------------------------------------------

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

        # ---------------------------------------------------------------------
        # Persist telemetry
        # ---------------------------------------------------------------------

        cosmos_duration = cosmos.save_telemetry(payload)

        # ---------------------------------------------------------------------
        # Compute execution time
        # ---------------------------------------------------------------------

        function_duration = round((time.perf_counter() - function_start) * 1000, 2)

        # ---------------------------------------------------------------------
        # Structured telemetry log
        # ---------------------------------------------------------------------

        logger.info(
            "Telemetry processed",
            extra={
                "custom_dimensions": json.dumps(
                    {
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
                )
            },
        )

        logger.info(
            "Telemetry persisted",
            extra={
                "custom_dimensions": json.dumps(
                    {
                        "vehicleId": vehicle_id,
                        "cosmosDurationMs": cosmos_duration,
                        "correlationId": correlation_id,
                    }
                )
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
