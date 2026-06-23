output "cosmosdb_name" {
  value = azurerm_cosmosdb_account.cosmosdb.name
}

output "cosmosdb_endpoint" {
  value = azurerm_cosmosdb_account.cosmosdb.endpoint
}

output "cosmosdb_id" {
  value = azurerm_cosmosdb_account.cosmosdb.id
}

output "database_name" {
  value = azurerm_cosmosdb_sql_database.database.name
}

output "container_name" {
  value = azurerm_cosmosdb_sql_container.container.name
}