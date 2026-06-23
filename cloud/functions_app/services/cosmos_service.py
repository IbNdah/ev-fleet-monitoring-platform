import uuid

from azure.cosmos import CosmosClient, PartitionKey
from services.keyvault_service import KeyVaultService


class CosmosService:

    def __init__(self):

        kv = KeyVaultService()

        endpoint = kv.get_secret("cosmos-endpoint")
        key = kv.get_secret("cosmos-key")
        client = CosmosClient(endpoint, credential=key)

        self.database = client.create_database_if_not_exists(id="fleetdb")

        self.container = (
            self.database.create_container_if_not_exists(
                id="telemetry",
                partition_key=PartitionKey(
                    path="/vehicleId"
                )
            )
        )

    def save_telemetry(self, payload):

        payload["id"] = str(uuid.uuid4())
        self.container.upsert_item(payload)