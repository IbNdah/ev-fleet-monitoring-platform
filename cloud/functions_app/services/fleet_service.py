from dataclasses import asdict, dataclass
import json
import logging

from services.cosmos_service import CosmosService

logger = logging.getLogger("evfleet")


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


class FleetService:

    def __init__(self):
        self.cosmos = CosmosService()

    def get_summary(self):

        telemetry = self.cosmos.get_fleet_summary()
        logger.info(json.dumps(telemetry, indent=4))

        if not telemetry:
            return {}

        # ------------------------------------------------------------------
        # Keep only the latest telemetry for each vehicle
        # ------------------------------------------------------------------

        latest = {}

        for item in telemetry:

            vehicle_id = item.get("vehicleId")
            if not vehicle_id:
                logger.warning("Ignoring document without vehicleId (id=%s)", item.get("id"))
                continue

            if not latest.get(vehicle_id):
                latest[vehicle_id] = item
                continue

            if (
                item["processedTimestamp"]
                > latest[vehicle_id]["processedTimestamp"]
            ):
                latest[vehicle_id] = item

        fleet = list(latest.values())

        total = len(fleet)
        
        if total == 0:
            logger.warning("No valid telemetry data found for any vehicle")
            return {}

        driving = sum(
            1
            for v in fleet
            if v["vehicleState"] == "DRIVING"
        )

        charging = sum(
            1
            for v in fleet
            if v["batteryState"] == "CHARGING"
        )

        parked = sum(
            1
            for v in fleet
            if v["vehicleState"] == "PARKED"
        )

        fault = sum(
            1
            for v in fleet
            if v["faultCode"] is not None
        )

        average_soc = round(
            sum(v["batterySoc"] for v in fleet) / total,
            2,
        )

        average_temperature = round(
            sum(v["batteryTemperature"] for v in fleet) / total,
            2,
        )

        average_voltage = round(
            sum(v["batteryVoltage"] for v in fleet) / total,
            2,
        )

        average_current = round(
            sum(v["batteryCurrent"] for v in fleet) / total,
            2,
        )

        # ------------------------------------------------------------------
        # Fleet Health Score
        # ------------------------------------------------------------------

        health = 100.0

        health -= fault * 20

        if average_temperature > 60:
            health -= 10

        if average_soc < 20:
            health -= 10

        health = max(0, round(health, 1))

        summary = FleetSummary(
            fleet_health=health,
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

        return asdict(summary)