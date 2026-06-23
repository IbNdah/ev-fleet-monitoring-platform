import os

from azure.identity import (DefaultAzureCredential, AzureCliCredential)
from azure.keyvault.secrets import SecretClient

if os.getenv("AZURE_FUNCTIONS_ENVIRONMENT") == "Development":
    credential = AzureCliCredential()
else:
    credential = DefaultAzureCredential()
    

class KeyVaultService:

    def __init__(self):

        vault_url = os.environ["KEYVAULT_URL"]

        credential = DefaultAzureCredential(exclude_managed_identity_credential=True)

        self.client = SecretClient(
            vault_url=vault_url,
            credential=credential
        )

    def get_secret(self, secret_name: str):

        return self.client.get_secret(
            secret_name
        ).value