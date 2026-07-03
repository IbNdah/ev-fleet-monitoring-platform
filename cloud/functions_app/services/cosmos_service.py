import logging
import time
import uuid
from datetime import datetime, timezone

from azure.cosmos import CosmosClient, PartitionKey
from services.keyvault_service import KeyVaultService


class CosmosService:

    _client = None
    _database = None
    _container = None

    def __init__(self):

        if CosmosService._client is None:

            kv = KeyVaultService()

            endpoint = kv.get_secret("cosmos-endpoint")
            key = kv.get_secret("cosmos-key")

            CosmosService._client = CosmosClient(
                endpoint,
                credential=key,
            )

            CosmosService._database = (
                CosmosService._client.create_database_if_not_exists(
                    id="fleetdb"
                )
            )

            CosmosService._container = (
                CosmosService._database.create_container_if_not_exists(
                    id="telemetry",
                    partition_key=PartitionKey(path="/vehicleId"),
                )
            )

    def save_telemetry(self, telemetry):

        if "id" not in telemetry:
            telemetry["id"] = str(uuid.uuid4())

        if "processedTimestamp" not in telemetry:
            telemetry["processedTimestamp"] = (
                datetime.now(timezone.utc).isoformat()
            )

        start = time.time()

        CosmosService._container.upsert_item(telemetry)

        cosmos_duration = round((time.time() - start) * 1000, 2)

        logging.info("========== COSMOS WRITE ==========")

        return cosmos_duration

    def get_fleet_summary(self):
        """
        Returns telemetry documents from Cosmos DB.
        """

        query = """
        SELECT
            c.vehicleId,
            c.deviceId,
            c.vehicleState,
            c.batteryState,
            c.batterySoc,
            c.batteryTemperature,
            c.batteryVoltage,
            c.batteryCurrent,
            c.faultCode,
            c.processedTimestamp
        FROM c
        """

        items = list(
            CosmosService._container.query_items(
                query=query,
                enable_cross_partition_query=True,
            )
        )

        return items