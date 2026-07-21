# Dashboard API

The Dashboard API provides aggregated telemetry data consumed by the Grafana dashboards.

Rather than exposing raw telemetry events, the API returns processed and summarized information optimized for visualization and operational monitoring.

---

# API Overview

| Property | Value |
|----------|-------|
| Base URL | `/api` |
| Format | JSON |
| Authentication | Anonymous *(Demo Project)* |
| Response Type | REST / JSON |

---

# Available Endpoints

| Endpoint | Purpose |
|----------|---------|
| `/dashboard/summary` | Fleet KPIs and aggregated metrics |
| `/dashboard/status` | Platform health and service status |
| `/dashboard/trends` | Historical telemetry trends |
| `/dashboard/vehicles` | Real-time vehicle information |

---

# Dashboard Summary

Provides high-level operational KPIs used by the Grafana overview dashboard.

### Example Response

```json
[
  {
    "vehicles_online": 5,
    "average_soc": 81.4,
    "average_temperature": 28.1,
    "average_voltage": 397.2,
    "average_current": 42.8,
    "fleet_health": "Healthy"
  }
]
```

---

# Dashboard Status

Returns the operational status of the platform components.

### Example Response

```json
[
  {
    "simulator_status": "Running",
    "edge_gateway_status": "Connected",
    "iot_hub_status": "Connected",
    "function_status": "Healthy",
    "cosmosdb_status": "Available",
    "last_update": "2026-07-16T10:15:00Z"
  }
]
```

---

# Dashboard Trends

Returns historical fleet metrics used for trend visualization.

### Example Response

```json
[
  {
    "timestamp": "2026-07-16T10:00:00Z",
    "average_soc": 82.1,
    "average_temperature": 27.8
  }
]
```

---

# Dashboard Vehicles

Returns the latest telemetry for each simulated vehicle.

### Example Response

```json
[
  {
    "vehicle_id": "EV-001",
    "state": "Driving",
    "soc": 84,
    "temperature": 29.2,
    "voltage": 398.4,
    "current": 41.7
  }
]
```

---

# Grafana Integration

The API is consumed by Azure Managed Grafana using the Infinity data source.

Each endpoint is optimized for dashboard consumption, minimizing client-side transformations while keeping the API simple and lightweight.

---

# Design Principles

The Dashboard API follows a Backend-for-Dashboard approach.

Instead of exposing raw telemetry, each endpoint returns aggregated information tailored for visualization.

This approach provides:

- Simplified dashboard configuration
- Reduced network traffic
- Faster dashboard rendering
- Stable JSON contracts
- Clear separation between telemetry processing and presentation
