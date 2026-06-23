output "resource_group_name" {
  value = module.resource_group.resource_group_name
}

# IoT Hub
output "iot_hub_name" {
  value = module.iot_hub.iot_hub_name
}

output "iot_hub_hostname" {
  value = module.iot_hub.iot_hub_hostname
}

# Keyvault
output "keyvault_id" {
  value = module.keyvault.keyvault_id
}

output "keyvault_uri" {
  value = module.keyvault.vault_uri
}