# Grafana Dashboard

This directory contains the exported dashboard configuration used by the
EV Fleet Monitoring Platform.

The dashboard presents fleet information using data exposed by the
platforms Dashboard REST API, including vehicle views, fleet status,
summary metrics, and telemetry trends.

## Dashboard Data Sources

The dashboard consumes the backend HTTP endpoints:

- `/api/dashboard/summary`
- `/api/dashboard/status`
- `/api/dashboard/vehicles`
- `/api/dashboard/trends`

The API route prefix depends on the Azure Functions host configuration.

## Import

To import the dashboard into Grafana:

1.  Open Grafana.
2.  Navigate to **Dashboards**.
3.  Select **New** or **Import**.
4.  Upload or paste the contents of `dashboard.json`.
5.  Configure the required data source and verify the endpoint settings.

The dashboard requires a data source configuration that can retrieve and
interpret the JSON responses returned by the Dashboard API.

## Related Documentation

- [Main project README](../README.md)
- [Dashboard API documentation](../docs/api/dashboard-api.md)
