> **Back to the main project:** [README.md](../README.md)

# 📚 Documentation

Welcome to the documentation of the **EV Fleet Monitoring Platform**.

This section complements the main project README by providing additional architectural references, API documentation, and supporting assets used throughout the project.

---

# Documentation Structure

```
docs/
│
├── architecture/
│   └── README.md
│
├── api/
│   └── dashboard-api.md
│
├── diagrams/
│
└── screenshots/
```

---

# 🏗️ Architecture

The architecture documentation explains how the platform is designed and why key architectural decisions were made.

It includes:

- Architecture Overview
- Layered Architecture
- Technology Stack
- Key Architectural Decisions
- Related Architecture Diagrams

📂 Location

```
docs/architecture/
```

---

# 🌐 API Documentation

The Dashboard API exposes REST endpoints consumed by Azure Managed Grafana.

Available documentation includes:

- Dashboard Summary
- Dashboard Status
- Dashboard Trends
- Dashboard Vehicles

📂 Location

```
docs/api/
```

---

# 📐 Architecture Diagrams

The project contains several diagrams illustrating the platform from different perspectives.

| Diagram | Description |
|----------|-------------|
| Executive Architecture | High-level view of the platform |
| End-to-End Telemetry Flow | Telemetry lifecycle from simulator to dashboard |
| Software Component Architecture | Internal application organization |
| Azure Infrastructure | Azure resources deployed with Terraform |
| Azure Solution Topology | Connectivity between Azure services |

📂 Location

```
docs/diagrams/
```

---

# 📷 Screenshots

Screenshots illustrate the operational platform and Azure resources.

Included images:

- Grafana Dashboard
- Azure Portal
- Application Insights
- Cosmos DB Explorer
- Azure Infrastructure

📂 Location

```
docs/screenshots/
```

---

# 🎯 Documentation Philosophy

The documentation is intentionally concise and focuses on the architectural concepts required to understand the platform.

It is designed to help readers quickly understand:

- the overall architecture;
- the telemetry processing flow;
- the interaction between Azure services;
- the dashboard APIs;
- the technologies used throughout the project.

For a complete overview of the project, please refer to the main **README.md**.
