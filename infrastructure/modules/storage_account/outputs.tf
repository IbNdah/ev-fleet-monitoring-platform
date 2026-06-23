output "storage_account_id" {

  value = azurerm_storage_account.storage-account.id

}

output "storage_account_name" {

  value = azurerm_storage_account.storage-account.name

}

output "primary_access_key" {

  value     = azurerm_storage_account.storage-account.primary_access_key
  sensitive = true

}

output "function_container_name" {

  value = azurerm_storage_container.function_releases.name

}