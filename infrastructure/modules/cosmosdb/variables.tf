variable "cosmosdb_name" {
  description = "Cosmos DB account name"
  type        = string
}

variable "resource_group_name" {
  description = "Resource Group name"
  type        = string
}

variable "location" {
  description = "Azure region"
  type        = string
}

variable "database_name" {
  description = "Cosmos database name"
  type        = string
}

variable "container_name" {
  description = "Container name"
  type        = string
}

variable "partition_key" {
  description = "Partition key"
  type        = string
}

variable "throughput" {
  description = "Cosmos container throughput in RU/s"
  type        = number
  default     = 400
}