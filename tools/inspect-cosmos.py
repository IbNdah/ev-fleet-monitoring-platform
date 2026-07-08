import json
from collections import Counter

from azure.cosmos import CosmosClient
from dotenv import load_dotenv
import os

load_dotenv()

COSMOS_ENDPOINT = os.getenv("COSMOS_ENDPOINT")
COSMOS_KEY = os.getenv("COSMOS_KEY")

DATABASE_NAME = "fleetdb"
CONTAINER_NAME = "telemetry"

client = CosmosClient(COSMOS_ENDPOINT, credential=COSMOS_KEY)

container = client.get_database_client(DATABASE_NAME).get_container_client(
    CONTAINER_NAME
)

print("\n==============================")
print(" COSMOS DATA INSPECTOR")
print("==============================\n")

query = """
SELECT TOP 20 *
FROM c
ORDER BY c._ts DESC
"""

items = list(container.query_items(query=query, enable_cross_partition_query=True))

print(f"Documents loaded : {len(items)}")

print("\n------------------------------")
print("Document Structure")
print("------------------------------")

all_keys = Counter()

for doc in items:

    all_keys.update(doc.keys())

for key, count in sorted(all_keys.items()):

    print(f"{key:25} {count}")

print("\n------------------------------")
print("Documents")
print("------------------------------\n")

for i, doc in enumerate(items):

    print("=" * 70)
    print(f"DOCUMENT {i+1}")
    print("=" * 70)

    print(json.dumps(doc, indent=4))

print("\nInspection finished.")
