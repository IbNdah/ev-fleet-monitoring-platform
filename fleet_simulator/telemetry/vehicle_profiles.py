"""
EV Fleet Monitoring Platform

Vehicle Operating Profiles

A VehicleProfile describes the operating condition assigned
to a simulated vehicle.

The FleetScenarioEngine decides which profile is active.

BatteryECU interprets the selected profile and generates
realistic battery telemetry.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class VehicleProfile:
    """
    Immutable description of a vehicle operating profile.
    """

    name: str
    vehicle_state: str

    # Optional constraints applied by BatteryECU
    max_soc: Optional[float] = None
    min_temperature: Optional[float] = None

    # Optional injected fault
    fault_code: Optional[str] = None


class VehicleProfiles:
    """
    Catalog of available operating profiles.
    """

    DRIVING = VehicleProfile(
        name="DRIVING",
        vehicle_state="DRIVING",
    )

    CHARGING = VehicleProfile(
        name="CHARGING",
        vehicle_state="CHARGING",
    )

    PARKED = VehicleProfile(
        name="PARKED",
        vehicle_state="PARKED",
    )

    LOW_BATTERY = VehicleProfile(
        name="LOW_BATTERY",
        vehicle_state="DRIVING",
        max_soc=15,
    )

    OVERHEATING = VehicleProfile(
        name="OVERHEATING",
        vehicle_state="FAULT",
        min_temperature=70,
        fault_code="OVERHEAT",
    )
