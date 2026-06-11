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