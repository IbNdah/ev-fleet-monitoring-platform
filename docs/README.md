# Documentation

This directory contains the supporting documentation for the **EV Fleet
Monitoring Platform**.

It provides the architecture guide, dashboard API reference,
architecture diagrams, and screenshots of the deployed platform.

## Documentation Structure

``` text
docs/
├── architecture/
│   └── README.md
├── api/
│   └── dashboard-api.md
├── diagrams/
│   ├── 01-executive-architecture.png
│   ├── 02-telemetry-flow.png
│   ├── 03-software-components.png
│   └── 04-azure-infrastructure.png
└── screenshots/
```

## Architecture Guide

The [Architecture Guide](architecture/README.md) describes the
platform’s logical layers, key design decisions, and technology choices.

## Dashboard API

The [Dashboard API documentation](api/dashboard-api.md) describes the
REST endpoints used to provide fleet information to Azure Managed
Grafana.

The dashboard endpoints cover:

- Fleet summary
- Fleet status
- Vehicle information
- Telemetry trends

## Architecture Diagrams

The diagrams present the solution from four complementary perspectives.

| Diagram                         | Description                                                 |
|---------------------------------|-------------------------------------------------------------|
| `01-executive-architecture.png` | High-level view of the complete platform.                   |
| `02-telemetry-flow.png`         | Telemetry path from the vehicle simulator to the dashboard. |
| `03-software-components.png`    | Main software components and their responsibilities.        |
| `04-azure-infrastructure.png`   | Azure resources and infrastructure relationships.           |

All diagrams are stored in `docs/diagrams/`.

## Screenshots

The screenshots provide visual evidence of the deployed platform and its
operational components, including Grafana, Azure resources, Application
Insights, and Cosmos DB.

They are stored in `docs/screenshots/`.

## Documentation Scope

The documentation focuses on the implemented architecture, the telemetry
processing path, the interaction between platform components, and the
dashboard interface.

For the project overview, start with the [main README](../README.md).
