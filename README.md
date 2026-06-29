# 🚗 EV Fleet Monitoring Platform

<p align="center">

![Azure](https://img.shields.io/badge/Microsoft-Azure-0078D4?logo=microsoftazure&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-IaC-7B42BC?logo=terraform&logoColor=white)
![Azure Functions](https://img.shields.io/badge/Azure-Functions-0062AD)
![Azure IoT Hub](https://img.shields.io/badge/Azure-IoT_Hub-0078D4)
![Cosmos DB](https://img.shields.io/badge/CosmosDB-NoSQL-2E8B57)
![MIT License](https://img.shields.io/badge/License-MIT-success)

</p>

---

# Enterprise Azure IoT Monitoring Platform

> An end-to-end Azure-native IoT platform demonstrating **Event-Driven Architecture**, **Serverless Computing**, **Infrastructure as Code**, **Cloud Security** and **Enterprise Observability**.

---

# 📷 Solution Overview

<p align="center">

**Battery ECU → MQTT → Edge Gateway → Azure IoT Hub → Azure Functions → Cosmos DB → Azure Monitor → Workbooks**

</p>

---

# 🌍 Business Problem

Modern electric vehicle fleets continuously generate telemetry that must be securely collected, validated, processed and visualized in near real time.

This project demonstrates how Microsoft Azure services can be combined into a production-inspired cloud-native architecture.

---

# 🚀 Solution Highlights

- 🚗 Multi-Vehicle Fleet Simulator
- 🌐 MQTT Edge Communication
- ☁ Azure IoT Hub
- ⚡ Azure Functions
- 🌌 Azure Cosmos DB
- 🔑 Azure Key Vault
- 🔒 Managed Identity
- 📊 Azure Monitor
- 💡 Application Insights
- 📈 Azure Workbooks
- 🏗 Terraform Infrastructure as Code
- 📋 OpenTelemetry
- 📑 Structured Logging

---

# 🏗 High-Level Architecture

<p align="center">

<img src="docs/architecture/high-level-architecture.png" width="100%">

</p>

---

# 🔄 End-to-End Telemetry Flow

<p align="center">

<img src="docs/architecture/end-to-end-flow.png" width="100%">

</p>

---

# ☁ Azure Architecture

| Azure Service | Purpose |
|---------------|---------|
| Azure IoT Hub | Secure telemetry ingestion |
| Event Hub Compatible Endpoint | Event streaming |
| Azure Functions | Event-driven processing |
| Azure Cosmos DB | Telemetry persistence |
| Azure Key Vault | Secret management |
| Managed Identity | Passwordless authentication |
| Application Insights | Distributed tracing |
| Azure Monitor | Cloud monitoring |
| Azure Workbooks | Fleet dashboards |

---

# ⭐ Enterprise Capabilities

| Capability | Status |
|------------|:------:|
| Fleet Simulation | ✅ |
| MQTT Communication | ✅ |
| Edge Gateway | ✅ |
| Azure IoT Hub | ✅ |
| Azure Functions | ✅ |
| Cosmos DB | ✅ |
| Managed Identity | ✅ |
| Azure Key Vault | ✅ |
| Application Insights | ✅ |
| Azure Monitor | ✅ |
| Azure Workbook | ✅ |
| Terraform | ✅ |
| GitHub Actions | 🚧 |
| Grafana | 🚧 |
| Alerting | 🚧 |

---

# 📊 Observability

The platform has been designed with **observability by default**.

✔ Structured Logging

✔ Correlation IDs

✔ OpenTelemetry

✔ Azure Monitor

✔ Application Insights

✔ Azure Workbook

✔ KQL Analytics

---

<p align="center">

<img src="docs/screenshots/workbook.png" width="95%">

</p>

---

# ⚡ Performance

Measured during production testing.

| Metric | Typical Value |
|---------|--------------:|
| Azure Function Execution | **8–16 ms** |
| Cosmos DB Write | **8–12 ms** |
| End-to-End Processing | **<20 ms** |
| Cosmos Response | **HTTP 201** |

---

# 📂 Repository Structure

```text
ev-fleet-monitoring-platform

├── cloud
│   ├── functions_app
│   ├── services
│   └── iot_hub_connector.py
│
├── fleet_simulator
│
├── edge_gateway
│
├── infrastructure
│   ├── environments
│   └── modules
│
├── shared
│
├── docs
│
└── tests
```

---

# 🛠 Technology Stack

| Category | Technologies |
|-----------|--------------|
| Language | Python 3.11 |
| Cloud | Microsoft Azure |
| IoT | MQTT |
| Messaging | Azure IoT Hub |
| Serverless | Azure Functions |
| Database | Cosmos DB |
| Security | Key Vault + Managed Identity |
| Monitoring | Azure Monitor |
| Observability | Application Insights + OpenTelemetry |
| Dashboards | Azure Workbooks |
| Infrastructure | Terraform |
| Version Control | Git & GitHub |

--- 

# 🚀 Quick Start

Clone

```bash
git clone https://github.com/<your-account>/ev-fleet-monitoring-platform.git
```

Install

```bash
python -m venv .venv

pip install -r requirements.txt
```

Run Fleet Simulator

```bash
python fleet_simulator/main.py
```

Run Azure Functions

```bash
func start
```

Deploy

```bash
func azure functionapp publish evfleet-function-dev
```

---

# 📷 Gallery

## Azure Workbook

<p align="center">

<img src="docs/screenshots/workbook.png" width="95%">

</p>

---

## Application Insights

<p align="center">

<img src="docs/screenshots/applications-insights.png" width="95%">

</p>

---

## Azure Cosmos DB

<p align="center">

<img src="docs/screenshots/cosmos-db.png" width="95%">

</p>

---

## Azure Portal

<p align="center">

<img src="docs/screenshots/resource-group.png" width="95%">

</p>

---

# 🗺 Roadmap

## Completed

- ✅ Fleet Simulator
- ✅ Edge Gateway
- ✅ Azure IoT Hub
- ✅ Azure Functions
- ✅ Cosmos DB
- ✅ Azure Key Vault
- ✅ Managed Identity
- ✅ Azure Monitor
- ✅ Azure Workbook
- ✅ OpenTelemetry
- ✅ Terraform

---

## Planned

- ⬜ GitHub Actions CI/CD
- ⬜ Grafana Dashboard
- ⬜ Email Alerting
- ⬜ Microsoft Teams Notifications
- ⬜ Docker
- ⬜ Kubernetes
- ⬜ Predictive Analytics

---

# 🎯 Skills Demonstrated

| Cloud | Infrastructure | DevOps | Observability |
|--------|---------------|---------|----------------|
| Azure IoT Hub | Terraform | Git | Azure Monitor |
| Azure Functions | IaC | GitHub | Application Insights |
| Cosmos DB | Modular Design | CI/CD | Workbooks |
| Key Vault | Automation | Testing | OpenTelemetry |
| Managed Identity | Cloud Security | Deployment | KQL |

---

# 📚 Documentation

Additional technical documentation is available in the **docs/** folder.

- Architecture
- Deployment Guide
- Terraform
- Monitoring
- Troubleshooting
- Architecture Decision Records (ADR)

---

# 👨‍💻 Author

**Ibrahim Ndah**

Cloud Engineer • Azure Solutions Architect • IoT Enthusiast

---

<p align="center">

⭐ If you like this project, consider giving it a Star!

</p>