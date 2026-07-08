import json
import logging
from collections import defaultdict
from dataclasses import asdict, dataclass
from datetime import datetime

from services.cosmos_service import CosmosService

logger = logging.getLogger("evfleet")


# ------------------------------------------------------------------
# Dashboard configuration
# ------------------------------------------------------------------

TREND_BUCKET_SECONDS = 5


# ------------------------------------------------------------------
# DTOs
# ------------------------------------------------------------------


@dataclass
class FleetSummary:
    fleet_health: float
    vehicles_online: int
    driving: int
    charging: int
    parked: int
    fault: int
    average_soc: float
    average_temperature: float
    average_voltage: float
    average_current: float


@dataclass
class FleetStatistics:
    """
    Fleet statistics calculated from the latest telemetry.
    """

    vehicles_online: int
    driving: int
    charging: int
    parked: int
    fault: int
    average_soc: float
    average_temperature: float
    average_voltage: float
    average_current: float


# ------------------------------------------------------------------
# Fleet Service
# ------------------------------------------------------------------


class FleetService:

    def __init__(self):
        self.cosmos = CosmosService()

    # ------------------------------------------------------------------
    # Fleet retrieval
    # ------------------------------------------------------------------

    def _get_latest_fleet(self) -> list[dict]:
        """
        Retrieve the latest telemetry document for each vehicle.

        Returns:
            list[dict]: Latest telemetry documents, one per vehicle.
        """

        telemetry = self.cosmos.get_fleet_summary()
        logger.info(json.dumps(telemetry, indent=4))

        if not telemetry:
            return []

        latest = {}

        # ------------------------------------------------------------------
        # Keep only the latest telemetry for each vehicle
        # ------------------------------------------------------------------

        for item in telemetry:

            vehicle_id = item.get("vehicleId")

            if not vehicle_id:
                logger.warning(
                    "Ignoring document without vehicleId (id=%s)",
                    item.get("id"),
                )
                continue

            if (
                vehicle_id not in latest
                or item["processedTimestamp"] > latest[vehicle_id]["processedTimestamp"]
            ):
                latest[vehicle_id] = item

        fleet = list(latest.values())

        if not fleet:
            logger.warning("No valid telemetry data found for any vehicle")

        return fleet

    # ------------------------------------------------------------------
    # Fleet statistics
    # ------------------------------------------------------------------

    def _calculate_statistics(
        self,
        fleet: list[dict],
    ) -> FleetStatistics:
        """
        Calculate fleet statistics.

        Args:
            fleet: Latest telemetry for each vehicle.

        Returns:
            FleetStatistics
        """

        total = len(fleet)

        driving = sum(1 for vehicle in fleet if vehicle["vehicleState"] == "DRIVING")

        charging = sum(1 for vehicle in fleet if vehicle["batteryState"] == "CHARGING")

        parked = sum(1 for vehicle in fleet if vehicle["vehicleState"] == "PARKED")

        fault = sum(1 for vehicle in fleet if vehicle["faultCode"] is not None)

        average_soc = round(
            sum(vehicle["batterySoc"] for vehicle in fleet) / total,
            2,
        )

        average_temperature = round(
            sum(vehicle["batteryTemperature"] for vehicle in fleet) / total,
            2,
        )

        average_voltage = round(
            sum(vehicle["batteryVoltage"] for vehicle in fleet) / total,
            2,
        )

        average_current = round(
            sum(vehicle["batteryCurrent"] for vehicle in fleet) / total,
            2,
        )

        return FleetStatistics(
            vehicles_online=total,
            driving=driving,
            charging=charging,
            parked=parked,
            fault=fault,
            average_soc=average_soc,
            average_temperature=average_temperature,
            average_voltage=average_voltage,
            average_current=average_current,
        )

    # ------------------------------------------------------------------
    # Fleet Summary
    # ------------------------------------------------------------------

    def get_summary(self):

        fleet = self._get_latest_fleet()

        if not fleet:
            return {}

        stats = self._calculate_statistics(fleet)

        # ------------------------------------------------------------------
        # Fleet Health Score
        # ------------------------------------------------------------------

        health = 100.0

        health -= stats.fault * 20

        if stats.average_temperature > 60:
            health -= 10

        if stats.average_soc < 20:
            health -= 10

        health = max(0, round(health, 1))

        summary = FleetSummary(
            fleet_health=health,
            vehicles_online=stats.vehicles_online,
            driving=stats.driving,
            charging=stats.charging,
            parked=stats.parked,
            fault=stats.fault,
            average_soc=stats.average_soc,
            average_temperature=stats.average_temperature,
            average_voltage=stats.average_voltage,
            average_current=stats.average_current,
        )

        return asdict(summary)

    # ------------------------------------------------------------------
    # Dashboard Overview
    # ------------------------------------------------------------------

    def get_overview(self):
        """
        Return the fleet overview for dashboard consumers.

        Returns:
            dict: Fleet overview.
        """

        return self.get_summary()

    # ------------------------------------------------------------------
    # Dashboard Vehicles
    # ------------------------------------------------------------------

    def get_vehicles(self):
        """
        Return dashboard-friendly vehicle information.
        """
        fleet = self._get_latest_fleet()
        return [
            {
                "vehicle": vehicle["vehicleId"],
                "soc": vehicle["batterySoc"],
                "temperature": vehicle["batteryTemperature"],
                "voltage": vehicle["batteryVoltage"],
                "current": vehicle["batteryCurrent"],
                "state": vehicle["vehicleState"],
                "fault": vehicle["faultCode"] or "-",
            }
            for vehicle in fleet
        ]

    # ------------------------------------------------------------------
    # Dashboard Trends
    # ------------------------------------------------------------------

    def get_trends(self):
        """
        Calculate fleet trends using configurable time buckets.

        The telemetry is grouped into 5-second buckets in order to
        calculate fleet-level averages instead of individual vehicle
        measurements.

        Returns:
            list[dict]: Fleet trend data ready for Grafana.
        """

        # --------------------------------------------------------------
        # Retrieve telemetry history
        # --------------------------------------------------------------

        telemetry = self.cosmos.get_telemetry_history()

        if not telemetry:
            logger.warning("No telemetry history found.")
            return []

        # --------------------------------------------------------------
        # Group telemetry into time buckets
        # --------------------------------------------------------------

        buckets = defaultdict(
            lambda: {
                "soc": [],
                "temperature": [],
            }
        )

        for item in telemetry:

            timestamp = datetime.fromisoformat(item["processedTimestamp"])

            bucket = timestamp.replace(
                second=(timestamp.second // TREND_BUCKET_SECONDS)
                * TREND_BUCKET_SECONDS,
                microsecond=0,
            )

            buckets[bucket]["soc"].append(item["batterySoc"])

            buckets[bucket]["temperature"].append(item["batteryTemperature"])

        # --------------------------------------------------------------
        # Calculate fleet averages
        # --------------------------------------------------------------

        trends = []

        for bucket in sorted(buckets.keys()):

            soc = buckets[bucket]["soc"]
            temperature = buckets[bucket]["temperature"]

            trends.append(
                {
                    "timestamp": bucket.strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "vehicle_count": len(soc),
                    "average_soc": round(
                        sum(soc) / len(soc),
                        2,
                    ),
                    "average_temperature": round(
                        sum(temperature) / len(temperature),
                        2,
                    ),
                }
            )

        logger.info(
            "Calculated %s fleet trend points.",
            len(trends),
        )

        return trends
