# region Imports

import random

from fleet_simulator.telemetry.vehicle_profiles import (
    VehicleProfiles,
)

# endregion


# region Fleet Scenario Engine


class FleetScenarioEngine:
    """
    EV Fleet Monitoring Platform

    Fleet Scenario Engine

    Responsibilities
    ----------------
    Central decision layer of the simulator.

    The FleetScenarioEngine decides which operating
    profile is assigned to each simulated vehicle.

    It never generates telemetry.

    Telemetry generation remains exclusively the
    responsibility of the BatteryECU.

    Architecture
    ------------
    FleetScenarioEngine
            │
            ▼
      VehicleProfile
            │
            ▼
         BatteryECU
            │
            ▼
      Telemetry Payload
    """

    # endregion

    # region Fleet Configuration

    # Weighted distribution of normal operating profiles

    NORMAL_PROFILES = [
        VehicleProfiles.DRIVING,
        VehicleProfiles.DRIVING,
        VehicleProfiles.DRIVING,
        VehicleProfiles.DRIVING,
        VehicleProfiles.DRIVING,
        VehicleProfiles.DRIVING,
        VehicleProfiles.PARKED,
        VehicleProfiles.PARKED,
        VehicleProfiles.CHARGING,
        VehicleProfiles.CHARGING,
    ]

    # Number of simulation cycles
    # each profile remains active

    PROFILE_DURATION = {
        "DRIVING": (5, 10),
        "PARKED": (2, 5),
        "CHARGING": (3, 6),
        "OVERHEATING": (1, 2),
    }

    # Probability of injecting a fault

    FAULT_PROBABILITY = 0.03

    # endregion

    # region Scenario Assignment

    @classmethod
    def assign_profiles(cls, vehicles):
        """
        Assign operating profiles to every vehicle.

        The same profile is kept for several
        simulation cycles to avoid unrealistic
        state oscillations.
        """

        for vehicle in vehicles:

            # -----------------------------------------
            # Keep current operating profile
            # -----------------------------------------

            if vehicle.profile_cycles_remaining > 0:

                vehicle.profile_cycles_remaining -= 1
                continue

            # -----------------------------------------
            # Low battery
            # -----------------------------------------

            if vehicle.battery_ecu.soc <= 15:

                profile = VehicleProfiles.CHARGING

            # -----------------------------------------
            # Rare overheating event
            # -----------------------------------------

            elif random.random() < cls.FAULT_PROBABILITY:

                profile = VehicleProfiles.OVERHEATING

            # -----------------------------------------
            # Normal fleet operation
            # -----------------------------------------

            else:

                profile = random.choice(
                    cls.NORMAL_PROFILES,
                )

            duration = random.randint(*cls.PROFILE_DURATION[profile.name])

            vehicle.set_profile(
                profile,
                duration,
            )

    # endregion
