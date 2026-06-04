# EV Fleet Monitoring Platform

## Overview

EV Fleet Monitoring Platform is a cloud-native Azure IoT solution designed to monitor the health and operational status of electric vehicle battery systems at scale.

The platform simulates a fleet of electric vehicles equipped with Battery ECUs that generate telemetry data. An Edge Gateway aggregates and normalizes telemetry before securely transmitting it to Azure IoT Hub using MQTT.

Telemetry is processed through an event-driven architecture using Azure Functions and stored in Azure Cosmos DB for analytics, monitoring, and future predictive maintenance scenarios.

---

## Business Scenario

Fleet operators need real-time visibility into the health and performance of electric vehicle batteries.

The platform continuously monitors:

- State of Charge (SOC)
- Battery Temperature
- Cell Voltage
- Current Consumption
- Battery Health Indicators

The solution enables:

- Fleet-wide battery monitoring
- Early anomaly detection
- Historical telemetry analysis
- Scalable cloud ingestion
- Future predictive maintenance capabilities

---

## High-Level Architecture

```text
┌─────────────────┐
│ EV Fleet        │
│ (Simulated)     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Battery ECU     │
│ Simulation      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Edge Gateway    │
│ Python          │
└────────┬────────┘
         │ MQTT
         ▼
┌─────────────────┐
│ Azure IoT Hub   │
└────────┬────────┘
         ▼
┌─────────────────┐
│ Azure Functions │
└────────┬────────┘
         ▼
┌─────────────────┐
│ Cosmos DB       │
└─────────────────┘
```

---

## Solution Architecture

```text
Fleet Simulator
      │
      ▼
Battery ECUs
      │
      ▼
Edge Gateway
      │
      ▼
MQTT Messaging
      │
      ▼
Azure IoT Hub
      │
      ▼
Telemetry Processing Function
      │
      ▼
Cosmos DB
      │
      ▼
Analytics & Monitoring
```

---

## Technology Stack

### Edge Layer

- Python
- MQTT

### Cloud Platform

- Azure IoT Hub
- Azure Functions
- Azure Cosmos DB

### Infrastructure

- Terraform

### Monitoring

- Azure Monitor
- Application Insights
- Log Analytics

### CI/CD

- GitHub Actions

---

## Repository Structure

```text
ev-fleet-monitoring-platform/

├── docs/
├── fleet_simulator/
├── edge_gateway/
├── cloud/
├── infrastructure/
└── .github/
```

---

## Data Model Example

```json
{
  "vehicleId": "EV-001",
  "soc": 82,
  "batteryTemperature": 36,
  "cellVoltage": 3.72,
  "current": 45,
  "timestamp": "2026-06-04T12:00:00Z"
}
```

---

## Data Flow

### 1. Telemetry Generation

Battery ECUs simulate vehicle battery behavior and generate telemetry.

### 2. Edge Processing

The Edge Gateway:

- Collects telemetry
- Validates payloads
- Normalizes data
- Publishes MQTT messages

### 3. Cloud Ingestion

Azure IoT Hub receives and authenticates incoming telemetry.

### 4. Event Processing

Azure Functions process telemetry events and apply business rules.

### 5. Persistence

Telemetry is stored in Azure Cosmos DB.

---

## Design Decisions

### Why an Edge Gateway?

Legacy ECUs typically do not communicate directly with cloud platforms.

The gateway provides:

- Protocol translation
- Data normalization
- Validation
- Future edge analytics capabilities

---

### Why MQTT?

MQTT is lightweight and optimized for constrained environments.

Benefits:

- Low bandwidth usage
- Reliable message delivery
- Widely adopted in IoT ecosystems

---

### Why Azure IoT Hub?

Azure IoT Hub provides:

- Device identity management
- Secure communication
- Cloud-to-device messaging
- Device provisioning capabilities

---

### Why Azure Functions?

Telemetry processing is event-driven and highly scalable.

Azure Functions eliminate the need to manage infrastructure while providing automatic scaling.

---

### Why Cosmos DB?

Telemetry data is naturally document-oriented and schema-flexible.

Cosmos DB offers:

- Global scalability
- Low latency
- Flexible JSON storage
- Efficient partitioning strategies

---

## Security Principles

The solution follows cloud security best practices:

- Managed Identity
- Azure RBAC
- Key Vault integration
- Principle of Least Privilege
- No secrets stored in source code

---

## Infrastructure as Code

Infrastructure is provisioned using Terraform.

Planned Azure resources:

- Resource Group
- Azure IoT Hub
- Cosmos DB
- Function App
- Key Vault
- Log Analytics Workspace
- Application Insights

---

## Future Enhancements

Planned future capabilities:

- Service Bus integration
- Real-time alerting
- Grafana dashboards
- Device Twins
- Digital Twin integration
- Predictive maintenance models
- Fleet-wide analytics

---

## Lessons Learned

This project focuses on understanding:

- Azure IoT Architecture
- Event-Driven Design
- Edge Computing
- Cloud-Native Patterns
- Infrastructure as Code
- Scalable Telemetry Processing

---

## Author

Ibrahim Ndah

- Microsoft Certified: Azure Administrator Associate (AZ-104)
- Cloud Engineering & Azure Architecture
- Automotive Systems Engineering Background