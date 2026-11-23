# Architecture Guide

This document describes the architecture of the **EV Fleet Monitoring
Platform**, including its main layers, data flow, and key technology
choices.

## Architecture Overview

The platform is an event-driven Azure IoT solution built around
simulated electric vehicles. Vehicle and battery telemetry is generated
by the simulator, transferred through an MQTT-based edge layer, ingested
by Azure IoT Hub, processed by Azure Functions, and stored in Azure
Cosmos DB.

Dashboard-oriented data is exposed through HTTP endpoints and visualized
in Azure Managed Grafana.

## Architecture Diagrams

| Diagram                                                                    | Purpose                                       |
|----------------------------------------------------------------------------|-----------------------------------------------|
| [01-executive-architecture.png](../diagrams/01-executive-architecture.png) | Overall platform architecture.                |
| [02-telemetry-flow.png](../diagrams/02-telemetry-flow.png)                 | End-to-end telemetry processing path.         |
| [03-software-components.png](../diagrams/03-software-components.png)       | Application components and responsibilities.  |
| [04-azure-infrastructure.png](../diagrams/04-azure-infrastructure.png)     | Azure resources provisioned for the platform. |

## Logical Architecture Layers

| Layer              | Responsibility                                                                                                 |
|--------------------|----------------------------------------------------------------------------------------------------------------|
| Vehicle simulation | Generates vehicle and battery telemetry.                                                                       |
| Messaging and edge | Transfers, validates, and prepares telemetry for cloud ingestion.                                              |
| Cloud ingestion    | Receives telemetry through Azure IoT Hub.                                                                      |
| Event processing   | Azure Functions consume events through the IoT Hub Event Hubs-compatible endpoint.                             |
| Data               | Cosmos DB persists telemetry for subsequent access.                                                            |
| Service            | HTTP-triggered Functions expose dashboard data, with FleetService providing dashboard-oriented business logic. |
| Visualization      | Azure Managed Grafana presents fleet information and trends.                                                   |

## Key Design Decisions

### Event-Driven Processing

The cloud processing path is event-driven. Azure IoT Hub receives device
telemetry, and an Azure Functions Event Hub trigger consumes messages
from the IoT Hub built-in Event Hubs-compatible endpoint.

This separates device ingestion from backend processing and avoids
coupling the telemetry producer directly to the persistence logic.

### Serverless Backend

Azure Functions hosts both the event-triggered telemetry processing
function and the HTTP-triggered dashboard endpoints. This keeps event
processing and API delivery within a managed compute service.

### Separation of Responsibilities

The backend separates the application entry points, business logic, and
data access:

- **Function App:** receives telemetry events and handles HTTP requests.
- **FleetService:** prepares fleet summaries, vehicle views, status
  information, and trends for the dashboard.
- **CosmosService:** handles persistence and data access for Cosmos DB.
- **Cosmos DB:** stores telemetry data.

### Telemetry Storage

Azure Cosmos DB stores the telemetry used by the backend and dashboard.
The data model supports access to vehicle information and telemetry
history required by the platforms views.

## Technology Stack

| Area                   | Technology                                         |
|------------------------|----------------------------------------------------|
| Cloud platform         | Microsoft Azure                                    |
| Language               | Python 3.11                                        |
| Device messaging       | MQTT, Mosquitto                                    |
| Cloud ingestion        | Azure IoT Hub                                      |
| Event processing       | Azure Functions, Event Hub trigger                 |
| Data storage           | Azure Cosmos DB                                    |
| Backend interface      | HTTP, REST, JSON                                   |
| Security               | Managed Identity, Azure Key Vault                  |
| Monitoring             | Azure Monitor, Application Insights, Log Analytics |
| Visualization          | Azure Managed Grafana                              |
| Infrastructure as Code | Terraform                                          |

## Related Documentation

- [Main project README](../../README.md)
- [Dashboard API](../api/dashboard-api.md)
- [Architecture diagrams](../diagrams/)
- [Platform screenshots](../screenshots/)
