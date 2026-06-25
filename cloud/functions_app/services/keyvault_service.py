import os
import logging

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient


class KeyVaultService:

    _client = None
    _cache = {}

    def __init__(self):

        if KeyVaultService._client is None:

            vault_url = os.getenv("KEYVAULT_URL")
            logging.info(f"Vault URL: {vault_url}")

            if not vault_url:
                raise ValueError(
                    "KEY_VAULT_URL is not configured."
                )

            credential = DefaultAzureCredential()

            KeyVaultService._client = SecretClient(
                vault_url=vault_url,
                credential=credential
            )

    def get_secret(self, secret_name):

        if secret_name in KeyVaultService._cache:
            return KeyVaultService._cache[secret_name]

        value = (
            KeyVaultService._client
            .get_secret(secret_name)
            .value
        )

        KeyVaultService._cache[secret_name] = value

        return value