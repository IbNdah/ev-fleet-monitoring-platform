# region Imports

from dataclasses import dataclass
from typing import Optional

# endregion


# region Data Transfer Objects (DTO)


@dataclass(frozen=True)
class VehicleProfile:
    """
    Immutable operating profile assigned to a simulated vehicle.

    Responsibilities
    ----------------
    - Describe the current operating mode.
    - Define optional physical constraints.
    - Inject optional fault conditions.

    Notes
    -----
    VehicleProfile is a pure data object.

    The FleetScenarioEngine selects the active profile.
    The BatteryECU interprets the profile and generates
    realistic battery telemetry.
    """

    name: str
    vehicle_state: str

    # Optional operating constraints
    max_soc: Optional[float] = None
    min_temperature: Optional[float] = None

    # Optional injected fault
    fault_code: Optional[str] = None


# endregion


# region Vehicle Profile Catalog


class VehicleProfiles:
    """
    Catalog of predefined vehicle operating profiles.

    These immutable profiles represent the business scenarios
    available to the FleetScenarioEngine.
    """

    # ---------------------------------------------------------
    # Normal Operation
    # ---------------------------------------------------------

    DRIVING = VehicleProfile(
        name="DRIVING",
        vehicle_state="DRIVING",
    )

    PARKED = VehicleProfile(
        name="PARKED",
        vehicle_state="PARKED",
    )

    CHARGING = VehicleProfile(
        name="CHARGING",
        vehicle_state="CHARGING",
    )

    # ---------------------------------------------------------
    # Special Operating Conditions
    # ---------------------------------------------------------

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


# endregion
