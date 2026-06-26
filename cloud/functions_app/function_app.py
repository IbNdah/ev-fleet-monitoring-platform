import json
import logging
import os
import time
import uuid

import azure.functions as func
from azure.monitor.opentelemetry import configure_azure_monitor
from services.cosmos_service import CosmosService

if os.getenv("APPLICATIONINSIGHTS_CONNECTION_STRING"):
    configure_azure_monitor()

app = func.FunctionApp()
logger = logging.getLogger(__name__)


@app.event_hub_message_trigger(
    arg_name="event",
    event_hub_name="messages/events",
    connection="EventHubConnection"
)
def process_telemetry(event: func.EventHubEvent):

    logger.info("######## VERSION 6.3.6 ########")

    cosmos = CosmosService()
    correlation_id = str(uuid.uuid4())
    start = time.time()

    try:

        raw_payload = event.get_body().decode("utf-8")
        payload = json.loads(raw_payload)
        
        logger.warning(f"RAW VEHICLE = {payload.get('vehicleId')} | DEVICE = {payload.get('deviceId')}")        
        logger.warning(f"WRITING TO COSMOS = {payload.get('vehicleId')}")

        vehicle_id = payload.get("vehicleId", "unknown")        
        cosmos_ms = cosmos.save_telemetry(payload)
        duration_ms = round((time.time() - start) * 1000, 2)

        logger.info(
            f"Vehicle={vehicle_id} "
            f"State={payload.get('batteryState')} "
            f"Battery={payload.get('batterySoc')}% "
            f"Temperature={payload.get('batteryTemperature')}°C "
            f"Cosmos={cosmos_ms:.2f}ms "
            f"Duration={duration_ms:.2f}ms "
            f"Correlation={correlation_id} "
            f"Status=SUCCESS "
        )

    except Exception as ex:

        logger.exception(ex)