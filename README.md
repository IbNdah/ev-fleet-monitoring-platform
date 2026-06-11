# 🚗 EV Fleet Monitoring Platform

![Status](https://img.shields.io/badge/status-active-success)
![Python](https://img.shields.io/badge/python-3.14-blue)
![MQTT](https://img.shields.io/badge/MQTT-Mosquitto-green)
![Azure](https://img.shields.io/badge/Azure-IoT%20Hub-blue)
![Tests](https://img.shields.io/badge/tests-passing-success)

---

# 📖 Overview

EV Fleet Monitoring Platform is a cloud-native Azure IoT project that simulates a fleet of electric vehicles and battery systems, processes telemetry at the edge, and transports telemetry to Azure cloud services.

The project demonstrates real-world concepts used in modern IoT and cloud platforms:

* ☁️ Cloud Architecture
* 📡 IoT Communication
* 🖥️ Edge Computing
* 🔄 Event-Driven Systems
* 🏗️ Infrastructure as Code (Terraform)
* 🔐 Configuration & Secret Management
* 🧪 Automated Testing
* ⚡ Azure IoT Services

---

# 🚀 Current Status

| Component                 | Status |
| ------------------------- | ------ |
| Fleet Simulator           | ✅      |
| Battery ECU Simulation    | ✅      |
| Scenario Engine           | ✅      |
| MQTT Publisher            | ✅      |
| MQTT Subscriber           | ✅      |
| Telemetry Validator       | ✅      |
| Telemetry Translator      | ✅      |
| Edge Gateway              | ✅      |
| Configuration Management  | ✅      |
| Cloud Connector           | ✅      |
| Azure IoT Hub             | ✅      |
| End-to-End Telemetry Flow | ✅      |
| Automated Tests           | ✅      |
| Azure Functions           | ⏳      |
| Cosmos DB                 | ⏳      |
| Monitoring & Alerting     | ⏳      |

---

# 🏗️ Current Solution Architecture

```text
Vehicle
    │
    ▼
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
    └── Routing
    │
    ▼
MQTT Processed Topic
(evfleet/telemetry/processed)
    │
    ▼
Cloud Connector
    │
    ▼
Azure IoT Hub
```

---

# 🌐 Azure Integration

Implemented Azure Components:

* Azure IoT Hub
* Device Identity Registration
* MQTT over TLS Communication
* Cloud Connector
* End-to-End Telemetry Ingestion
* Terraform-based Azure Provisioning
* Environment-Based Configuration (.env)

Validated Flow:

```text
Fleet Simulator
      │
      ▼
Edge Gateway
      │
      ▼
Cloud Connector
      │
      ▼
Azure IoT Hub
```

---

# 🚀 Implemented Features

## 🚗 Fleet Simulation

* Multiple simulated EVs
* Fleet management engine
* Vehicle lifecycle simulation
* Scenario-driven behavior

## 🔋 Battery ECU Simulation

Each Battery ECU generates:

* State of Charge (SOC)
* Temperature
* Voltage
* Current
* Fault conditions
* UTC timestamps

## 🎭 Scenario Engine

Implemented scenarios:

* Normal Driving
* Fast Charging
* Low Battery
* Overheating

## 📡 MQTT Integration

Validated end-to-end:

* Mosquitto MQTT Broker
* MQTT Publisher
* MQTT Subscriber
* JSON Serialization
* Continuous Telemetry Publishing

## 🌐 Edge Gateway

Implemented:

* MQTT Subscriber
* Telemetry Validation
* Telemetry Translation
* Raw Topic Processing
* Processed Topic Publishing
* Rejected Topic Routing
* Structured Logging

Topics:

```text
evfleet/telemetry/raw
evfleet/telemetry/processed
evfleet/telemetry/rejected
```

## ☁️ Cloud Connector

Implemented:

* MQTT Subscription to Processed Topic
* Azure IoT Hub Connection
* Telemetry Forwarding
* Device Authentication
* Secure Cloud Communication

---

# ✅ Current Architecture

![Current Architecture](docs/screenshots/Current_Architecture.png)

---

# 🎯 Target Architecture

![Target Architecture](docs/screenshots/Target_Architecture.png)

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

## Edge Gateway

* Telemetry validation
* Telemetry translation
* Gateway processing pipeline
* Invalid telemetry handling

## Cloud Integration

* Azure IoT Hub connectivity
* Device authentication
* Telemetry forwarding
* End-to-End validation

Run all tests:

```bash
pytest
```

---

# ▶️ Running the Platform

## Start MQTT Broker

```bash
mosquitto
```

## Start Cloud Connector

```bash
python -m cloud.main
```

## Start Edge Gateway

```bash
python -m edge_gateway.gateway
```

## Start Fleet Simulator

```bash
python -m fleet_simulator.main
```

---

# 🔐 Configuration

Sensitive configuration is stored outside the source code using environment variables.

Example:

```env
IOT_HUB_CONNECTION_STRING=your_connection_string
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
│   ├── functions/
│   ├── iot_hub_connector.py
│   └── main.py
│
├── infrastructure/
│   ├── modules/
│   └── environments/
│
├── config/
│
├── shared/
│
└── docs/
```

---

# 🏆 Skills Demonstrated

* Python Development
* MQTT Messaging
* Azure IoT Hub
* Edge Computing
* Event-Driven Architecture
* Infrastructure as Code (Terraform)
* Cloud Integration
* Telemetry Processing
* Configuration Management
* Dependency Injection
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

## Phase 2 — Edge Processing ✅

* MQTT Subscriber
* Telemetry Validator
* Telemetry Translator
* Gateway Processing Pipeline
* Raw / Processed / Rejected Topics

## Phase 3 — Configuration Management ✅

* Centralized Configuration
* Environment-Based Configuration
* Secret Management

## Phase 4 — Azure IoT Hub Integration ✅

* Azure IoT Hub
* Device Identity
* Cloud Connector
* End-to-End Validation

## Phase 5 — Azure Functions ⏳

* IoT Hub Trigger
* Telemetry Processing
* Event Handling

## Phase 6 — Cosmos DB ⏳

* Telemetry Persistence
* Data Modeling
* Query Layer

## Phase 7 — Monitoring & Observability ⏳

* Application Insights
* Azure Monitor
* Metrics
* Alerting

## Phase 8 — Advanced IoT Features ⏳

* Device Twins
* Fleet Analytics
* Predictive Maintenance
* Real-Time Dashboards

---

# 🧠 Lessons Learned

This project provides hands-on experience with:

* Python Object-Oriented Design
* MQTT Messaging Patterns
* IoT Architecture Design
* Edge Computing Concepts
* Event-Driven Systems
* Azure Cloud Services
* Infrastructure as Code
* Secure Configuration Management
* Scalable Telemetry Processing
* Software Testing and Validation

---

# 👨‍💻 Author

**Ibrahim Ndah**

🎓 Microsoft Certified: Azure Solutions Architect Expert (AZ-305)
🎓 Microsoft Certified: Azure Administrator Associate (AZ-104)
☁️ Azure Cloud Engineering & Solution Architecture
🚗 Automotive Systems Engineering Background
⚡ Cloud, IoT & Platform Engineering
