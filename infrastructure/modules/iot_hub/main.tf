resource "azurerm_iothub" "iot_hub" {
  name                = var.iot_hub_name
  location            = var.location
  resource_group_name = var.resource_group_name

  event_hub_partition_count = 2

  sku {
    name     = "F1"
    capacity = 1
  }
}