resource "azurerm_function_app_flex_consumption" "evfleet_func_app" {

  name                = var.function_app_name
  resource_group_name = var.resource_group_name
  location            = var.location

  storage_container_type      = "blobContainer"
  storage_container_endpoint  = "https://${var.storage_account_name}.blob.core.windows.net/function-releases"
  storage_authentication_type = "StorageAccountConnectionString"

  storage_access_key = var.storage_account_access_key

  runtime_name    = "python"
  runtime_version = "3.12"

  maximum_instance_count = 50
  instance_memory_in_mb  = 2048

  site_config {}

  app_settings = {
    APPLICATIONINSIGHTS_CONNECTION_STRING = var.application_insights_connection_string
  }
}