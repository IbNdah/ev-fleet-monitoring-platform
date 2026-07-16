import json
import logging
import os
import time
import uuid
from typing import Any

import azure.functions as func
from azure.monitor.opentelemetry import configure_azure_monitor
from services.cosmos_service import CosmosService
from services.fleet_service import FleetService

# -----------------------------------------------------------------------------
# Configure Azure Monitor / Application Insights
# -----------------------------------------------------------------------------

connection_string = os.getenv("APPLICATIONINSIGHTS_CONNECTION_STRING")

if connection_string:
    configure_azure_monitor(connection_string=connection_string)

# -----------------------------------------------------------------------------
# Logging
# -----------------------------------------------------------------------------

logger = logging.getLogger("evfleet")
logger.setLevel(logging.INFO)

app = func.FunctionApp()

# -----------------------------------------------------------------------------
# HTTP Response Helpers
# -----------------------------------------------------------------------------


def json_response(data: Any, status_code: int = 200) -> func.HttpResponse:
    """
    Return a standardized JSON HTTP response.

    Architectural rationale
    -----------------------
    Centralizes JSON serialization and guarantees that every REST endpoint
    exposes a consistent response contract.
    """

    return func.HttpResponse(
        json.dumps(data, indent=4),
        mimetype="application/json",
        status_code=status_code,
    )


def error_response(ex: Exception, status_code: int = 500) -> func.HttpResponse:
    """
    Return a standardized JSON error response.

    Keeping error payloads consistent simplifies debugging and enables
    future REST consumers to process failures programmatically.
    """

    return json_response(
        {
            "error": str(ex),
            "status": status_code,
        },
        status_code=status_code,
    )


# -----------------------------------------------------------------------------
# Event Hub Trigger
# -----------------------------------------------------------------------------
@app.event_hub_message_trigger(
    arg_name="event",
    event_hub_name="messages/events",
    connection="EventHubConnection",
)
def process_telemetry(event: func.EventHubEvent):

    logger.info("########_ VERSION 7.6.1 _########")

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
                "custom_dimensions": json.dumps(
                    {
                        "vehicleId": vehicle_id,
                        "deviceId": payload.get("deviceId"),
                        "correlationId": correlation_id,
                    },
                    ensure_ascii=False,
                )
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
                    },
                    ensure_ascii=False,
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
                    },
                    ensure_ascii=False,
                )
            },
        )

    except Exception:

        logger.exception(
            "Telemetry processing failed",
            extra={
                "custom_dimensions": json.dumps(
                    {
                        "vehicleId": payload.get("vehicleId", "UNKNOWN"),
                        "correlationId": correlation_id,
                        "status": "FAILED",
                    },
                    ensure_ascii=False,
                )
            },
        )

        raise


# -----------------------------------------------------------------------------
# Dashboard Summary API
# -----------------------------------------------------------------------------
@app.route(
    route="dashboard/summary",
    methods=["GET"],
    auth_level=func.AuthLevel.ANONYMOUS,
)
def dashboard_summary(req: func.HttpRequest) -> func.HttpResponse:

    logger.info("Dashboard Summary API called")

    try:
        fleet = FleetService()
        data = fleet.get_dashboard_summary()

        return json_response([data])

    except Exception as ex:
        logger.exception("Dashboard Summary API failed")

        return error_response(ex)


# -----------------------------------------------------------------------------
# Dashboard Vehicles API
# -----------------------------------------------------------------------------
@app.route(
    route="dashboard/vehicles",
    methods=["GET"],
    auth_level=func.AuthLevel.ANONYMOUS,
)
def dashboard_vehicles(req: func.HttpRequest) -> func.HttpResponse:

    logger.info("Dashboard Vehicles API called")

    try:
        fleet = FleetService()
        data = fleet.get_dashboard_vehicles()

        return json_response(data)

    except Exception as ex:
        logger.exception("Dashboard Vehicles API failed")

        return error_response(ex)


# -----------------------------------------------------------------------------
# Dashboard Trends API
# -----------------------------------------------------------------------------
@app.route(
    route="dashboard/trends",
    methods=["GET"],
    auth_level=func.AuthLevel.ANONYMOUS,
)
def dashboard_trends(req: func.HttpRequest) -> func.HttpResponse:

    logger.info("Dashboard Trends API called")

    try:
        fleet = FleetService()
        data = fleet.get_dashboard_trends()

        return json_response(data)

    except Exception as ex:
        logger.exception("Dashboard Trends API failed")

        return error_response(ex)


# -----------------------------------------------------------------------------
# Dashboard Status API
# -----------------------------------------------------------------------------
@app.route(
    route="dashboard/status",
    methods=["GET"],
    auth_level=func.AuthLevel.ANONYMOUS,
)
def dashboard_status(req: func.HttpRequest) -> func.HttpResponse:

    logger.info("Dashboard Status API called")

    try:
        fleet = FleetService()
        data = fleet.get_dashboard_status()

        return json_response([data])

    except Exception as ex:
        logger.exception("Dashboard Status API failed")

        return error_response(ex)
