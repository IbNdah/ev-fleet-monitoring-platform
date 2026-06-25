output "workspace_id" {
  value = azurerm_log_analytics_workspace.workspace.id
}

output "workspace_name" {
  value = azurerm_log_analytics_workspace.workspace.name
}

output "app_insights_connection_string" {

  value     = azurerm_application_insights.app_insig.connection_string
  sensitive = true

}

output "application_insights_id" {

  value = azurerm_application_insights.app_insig.id

}

output "instrumentation_key" {

  value     = azurerm_application_insights.app_insig.instrumentation_key
  sensitive = true

}

