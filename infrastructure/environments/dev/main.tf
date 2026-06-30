terraform {
  required_version = ">= 1.6"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.0"
    }
  }
}

provider "azurerm" {
  features {}
}

# Data of current User
data "azurerm_client_config" "current" {}


# Resource Group
module "resource_group" {
  source = "../../modules/resource_group"

  resource_group_name = var.resource_group_name
  location            = var.location
}

module "iot_hub" {
  source = "../../modules/iot_hub"

  iot_hub_name        = var.iot_hub_name
  resource_group_name = module.resource_group.resource_group_name
  location            = module.resource_group.resource_group_location
}

# Storage Account
module "storage_account" {
  source = "../../modules/storage_account"

  storage_account_name = var.storage_account_name
  resource_group_name  = module.resource_group.resource_group_name
  location             = module.resource_group.resource_group_location

}

# Application Insight
module "monitoring" {

  source = "../../modules/monitoring"

  application_insights_name    = var.application_insights_name
  log_analytics_workspace_name = var.log_analytics_workspace_name

  resource_group_name = module.resource_group.resource_group_name
  location            = module.resource_group.resource_group_location
}

# Function App
/* module "function_app" {

  source = "../../modules/function_app"

  function_app_name = var.function_app_name
  resource_group_name = module.resource_group.resource_group_name
  location = module.resource_group.resource_group_location
  storage_account_name = module.storage_account.storage_account_name
  storage_account_access_key = module.storage_account.primary_access_key
  application_insights_connection_string = module.monitoring.connection_string

}
*/

# Cosmos DB
module "cosmosdb" {
  source = "../../modules/cosmosdb"

  cosmosdb_name = "evfleetcosmosdev"

  resource_group_name = module.resource_group.resource_group_name
  location            = module.resource_group.resource_group_location

  database_name  = "fleetdb"
  container_name = "telemetry"

  partition_key = "/vehicleId"
  throughput    = 400
}

# Keyvault
module "keyvault" {
  source = "../../modules/keyvault"

  keyvault_name = "kv-evfleet-dev01"

  resource_group_name = module.resource_group.resource_group_name
  location            = module.resource_group.resource_group_location

  tenant_id = data.azurerm_client_config.current.tenant_id
  object_id = data.azurerm_client_config.current.object_id
}