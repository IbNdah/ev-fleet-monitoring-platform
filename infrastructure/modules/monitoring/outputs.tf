output "application_insights_id" {

  value = azurerm_application_insights.app_insig.id

}

output "instrumentation_key" {

  value     = azurerm_application_insights.app_insig.instrumentation_key

  sensitive = true

}

output "connection_string" {

  value     = azurerm_application_insights.app_insig.connection_string

  sensitive = true

}