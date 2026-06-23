# 🚗 EV Fleet Monitoring Platform

![Status](https://img.shields.io/badge/status-active-success)
![Python](https://img.shields.io/badge/python-3.11-blue)
![MQTT](https://img.shields.io/badge/MQTT-Mosquitto-green)
![Azure](https://img.shields.io/badge/Azure-IoT%20Hub-blue)
![Azure Functions](https://img.shields.io/badge/Azure-Functions-orange)
![Tests](https://img.shields.io/badge/tests-passing-success)

---

# 📖 Overview

EV Fleet Monitoring Platform is a cloud-native Azure IoT project that simulates a fleet of electric vehicles and battery systems, processes telemetry at the edge, and transports telemetry to Azure cloud services.

The project demonstrates real-world concepts used in modern IoT and cloud platforms:

* ☁️ Cloud Architecture
* 📡 IoT Communication
* 🖥️ Edge Computing
* ⚡ Serverless Computing
* 🔄 Event-Driven Systems
* 🏗️ Infrastructure as Code (Terraform)
* 🔐 Configuration & Secret Management
* 🧪 Automated Testing
* ⚡ Azure IoT Services

---

# 🚀 Current Status

| Component | Status |
|----------|---------|
| Fleet Simulator | ✅ |
| Battery ECU Simulation | ✅ |
| Scenario Engine | ✅ |
| MQTT Publisher | ✅ |
| MQTT Subscriber | ✅ |
| Telemetry Validator | ✅ |
| Telemetry Translator | ✅ |
| Edge Gateway | ✅ |
| Configuration Management | ✅ |
| Azure IoT Hub | ✅ |
| IoT Hub Device Connector | ✅ |
| Azure Functions | ✅ |
| Event Hub Trigger | ✅ |
| End-to-End Telemetry Pipeline | ✅ |
| Automated Tests | ✅ |
| Cosmos DB | ✅ |
| Monitoring & Alerting | ⏳ |
| Fleet Analytics | ⏳ |

---

# 🏗️ Current Solution Architecture

```text
Battery ECU
      │
      ▼
Fleet Simulator
      │
      ▼
MQTT Raw Topic
(evfleet/telemetry/raw)
      │
      ▼
Edge Gateway
      │
      ├── Validation
      ├── Translation
      │
      ├── MQTT Processed Topic
      │   (evfleet/telemetry/processed)
      │
      └── Azure IoT Hub
               │
               ▼
      Event Hub Compatible Endpoint
               │
               ▼
         Azure Functions
               │
               ▼
            Logging
```

---

# 🌐 Azure Integration

Implemented Azure Components:

* Azure IoT Hub
* Device Identity Registration
* MQTT over TLS Communication
* Azure Functions
* Event Hub Trigger
* Event-Driven Processing
* Environment-Based Configuration
* Python Azure SDK
* Terraform-based Azure Provisioning

Validated Cloud Flow:

```text
Fleet Simulator
      │
      ▼
Edge Gateway
      │
      ▼
Azure IoT Hub
      │
      ▼
Event Hub Endpoint
      │
      ▼
Azure Function
```

---

# 🚀 Implemented Features

## 🚗 Fleet Simulation

* Multiple simulated EVs
* Fleet management engine
* Vehicle lifecycle simulation
* Scenario-driven behavior

---

## 🔋 Battery ECU Simulation

Each Battery ECU generates:

* State of Charge (SOC)
* Temperature
* Voltage
* Current
* Fault conditions
* UTC timestamps

---

## 🎭 Scenario Engine

Implemented scenarios:

* Normal Driving
* Fast Charging
* Low Battery
* Overheating

---

## 📡 MQTT Integration

Validated end-to-end:

* Mosquitto MQTT Broker
* MQTT Publisher
* MQTT Subscriber
* JSON Serialization
* Continuous Telemetry Publishing

---

## 🌐 Edge Gateway

Implemented:

* MQTT Subscriber
* Telemetry Validation
* Telemetry Translation
* Raw Topic Processing
* Processed Topic Publishing
* Rejected Topic Routing
* Structured Logging
* Azure IoT Hub Integration

Topics:

```text
evfleet/telemetry/raw
evfleet/telemetry/processed
evfleet/telemetry/rejected
```

---

## ☁️ Azure IoT Hub

Implemented:

* Device Authentication
* Secure Communication
* IoT Device SDK
* Telemetry Forwarding
* MQTT over TLS
* Device Registration

---

## ⚡ Azure Functions

Implemented:

* Event Hub Trigger
* Event-Driven Processing
* JSON Deserialization
* Telemetry Parsing
* Structured Logging
* Error Handling

Current Function Flow:

```text
Azure IoT Hub
      │
      ▼
Event Hub Endpoint
      │
      ▼
Azure Function Trigger
      │
      ▼
Telemetry Processing
      │
      ▼
Logging
```

---

# ✅ End-to-End Telemetry Pipeline

```text
Battery ECU
      │
      ▼
Fleet Simulator
      │
      ▼
MQTT Raw Topic
      │
      ▼
Edge Gateway
      │
      ▼
Azure IoT Hub
      │
      ▼
Azure Function
      │
      ▼
Telemetry Processing
```

---

# 🎯 Target Architecture

```text
Battery ECU
      │
      ▼
Fleet Simulator
      │
      ▼
MQTT Raw Topic
      │
      ▼
Edge Gateway
      │
      ▼
Azure IoT Hub
      │
      ▼
Azure Functions
      │
      ▼
Cosmos DB
      │
      ▼
Azure Monitor
      │
      ▼
Dashboards & Analytics
```

---

# 📦 Example Telemetry

## Raw Telemetry

```json
{
  "deviceId": "BATT-EV-001",
  "temperature": 31.4,
  "current": -0.04,
  "voltage": 3.67,
  "soc": 79.77,
  "state": "DRIVING",
  "faultCode": null,
  "timestamp": "2026-06-05T16:08:20.227267+00:00",
  "vehicleId": "EV-001",
  "vehicleState": "DRIVING"
}
```

---

## Processed Telemetry

```json
{
  "schemaVersion": "1.0",
  "vehicleId": "EV-001",
  "deviceId": "BATT-EV-001",
  "vehicleState": "DRIVING",
  "batteryState": "DRIVING",
  "batterySoc": 79.77,
  "batteryTemperature": 31.4,
  "batteryVoltage": 3.67,
  "batteryCurrent": -0.04,
  "faultCode": null,
  "telemetryTimestamp": "2026-06-05T16:08:20.227267+00:00",
  "processedTimestamp": "2026-06-08T11:00:00+00:00"
}
```

---

# 🧪 Testing

Current automated test coverage includes:

## Fleet Simulator

* Vehicle creation
* Fleet creation
* Fleet simulation
* State changes
* Scenario handling
* Battery ECU behavior

---

## Edge Gateway

* Telemetry validation
* Telemetry translation
* Gateway processing pipeline
* Invalid telemetry handling

---

## Cloud Integration

* Azure IoT Hub connectivity
* Device authentication
* Event Hub Trigger
* Azure Functions processing
* Telemetry forwarding
* End-to-End validation

Run all tests:

```bash
pytest
```

---

# ▶️ Running the Platform

## 1. Start Mosquitto Broker

```bash
mosquitto
```

---

## 2. Start Azure Function

```bash
cd cloud/functions_app

func start
```

---

## 3. Start Edge Gateway

```bash
python -m edge_gateway.gateway
```

---

## 4. Start Fleet Simulator

```bash
python -m fleet_simulator.main
```

---

Complete telemetry flow:

```text
Fleet Simulator
      │
      ▼
MQTT Raw Topic
      │
      ▼
Edge Gateway
      │
      ▼
Azure IoT Hub
      │
      ▼
Azure Functions
```

---

# 🔐 Configuration

Sensitive configuration is stored outside the source code using environment variables.

Example:

```env
MQTT_BROKER=localhost

IOT_HUB_CONNECTION_STRING=your_connection_string

AzureWebJobsStorage=your_storage_connection

EventHubConnection=your_eventhub_connection
```

Environment variables are loaded automatically using:

```python
load_dotenv()
```

---

# 📂 Repository Structure

```text
ev-fleet-monitoring-platform/

├── .github/
│   └── workflows/
│
├── fleet_simulator/
│   ├── vehicles/
│   ├── telemetry/
│   └── tests/
│
├── edge_gateway/
│   ├── gateway.py
│   ├── mqtt_publisher.py
│   ├── mqtt_subscriber.py
│   ├── validator.py
│   ├── translator.py
│   └── tests/
│
├── cloud/
│   ├── functions_app/
│   │   ├── function_app.py
│   │   ├── host.json
│   │   └── local.settings.json
│   │
│   ├── iot_hub_connector.py
│   └── tests/
│
├── infrastructure/
│   ├── modules/
│   └── environments/
│
├── shared/
│   └── config.py
│
├── docs/
│
├── requirements.txt
│
└── README.md
```

---

# 🏆 Skills Demonstrated

* Python Development
* MQTT Messaging
* Azure IoT Hub
* Azure Functions
* Event Hub Triggers
* Serverless Computing
* Edge Computing
* Event-Driven Architecture
* Infrastructure as Code (Terraform)
* Cloud Integration
* Telemetry Processing
* Configuration Management
* Dependency Injection Concepts
* Automated Testing
* GitHub Actions CI/CD

---

# 🛣️ Roadmap

## Phase 1 — Simulation & MQTT ✅

* Fleet Simulator
* Battery ECU Simulation
* Scenario Engine
* MQTT Publisher
* MQTT Integration

---

## Phase 2 — Edge Processing ✅

* MQTT Subscriber
* Telemetry Validator
* Telemetry Translator
* Gateway Processing Pipeline
* Raw / Processed / Rejected Topics

---

## Phase 3 — Configuration Management ✅

* Centralized Configuration
* Environment-Based Configuration
* Secret Management

---

## Phase 4 — Azure IoT Hub Integration ✅

* Azure IoT Hub
* Device Identity
* Device Authentication
* Secure Communication
* End-to-End Validation

---

## Phase 5 — Azure Functions ✅

* Event Hub Trigger
* Event-Driven Processing
* JSON Deserialization
* Telemetry Processing
* Logging
* Error Handling
* End-to-End Validation

---

## Phase 6 — Cosmos DB ⏳

* Telemetry Persistence
* Data Modeling
* Historical Storage
* Query Layer

---

## Phase 7 — Monitoring & Observability ⏳

* Application Insights
* Azure Monitor
* Metrics
* Alerting

---

## Phase 8 — Advanced IoT Features ⏳

* Device Twins
* Fleet Analytics
* Predictive Maintenance
* Real-Time Dashboards

---

# 🧠 Key Learnings

This project provides hands-on experience with:

* Python Object-Oriented Design
* MQTT Messaging Patterns
* IoT Architecture Design
* Edge Computing Concepts
* Event-Driven Systems
* Azure IoT Hub
* Azure Functions
* Event Hub Triggers
* Serverless Processing
* Infrastructure as Code
* Secure Configuration Management
* Scalable Telemetry Processing
* Software Testing and Validation
* End-to-End Cloud Integration

---

# 👨‍💻 Author

**Ibrahim Ndah**

🎓 Microsoft Certified: Azure Solutions Architect Expert (AZ-305)

🎓 Microsoft Certified: Azure Administrator Associate (AZ-104)

☁️ Azure Cloud Engineering & Solution Architecture

🚗 Automotive Systems Engineering Background

⚡ Cloud, IoT & Platform Engineering