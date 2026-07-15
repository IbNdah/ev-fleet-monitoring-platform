"""
EV Fleet Monitoring Platform

Fleet Scenario Engine

Decision layer of the simulator.

Responsibilities
----------------
- Assign operating profiles.
- Keep profiles active for several cycles.
- Inject rare fault scenarios.
- Never generate telemetry.

Telemetry generation remains the responsibility
of the BatteryECU.
"""

import random

from fleet_simulator.telemetry.vehicle_profiles import (
    VehicleProfiles,
)


class FleetScenarioEngine:
    """Assign operating profiles to the simulated fleet."""

    # Fleet distribution
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
    PROFILE_DURATION = {
        "DRIVING": (5, 10),
        "PARKED": (2, 5),
        "CHARGING": (3, 6),
        "OVERHEATING": (1, 2),
    }

    FAULT_PROBABILITY = 0.03

    @classmethod
    def assign_profiles(cls, vehicles):
        """
        Assign operating profiles to every vehicle.
        """

        for vehicle in vehicles:

            # -----------------------------------------
            # Keep current profile
            # -----------------------------------------

            if vehicle.profile_cycles_remaining > 0:

                vehicle.profile_cycles_remaining -= 1
                continue

            # -----------------------------------------
            # Low battery always charges
            # -----------------------------------------

            if vehicle.battery_ecu.soc <= 15:

                profile = VehicleProfiles.CHARGING

            # -----------------------------------------
            # Rare overheating
            # -----------------------------------------

            elif random.random() < cls.FAULT_PROBABILITY:

                profile = VehicleProfiles.OVERHEATING

            # -----------------------------------------
            # Normal operation
            # -----------------------------------------

            else:

                profile = random.choice(cls.NORMAL_PROFILES)

            duration = random.randint(*cls.PROFILE_DURATION[profile.name])

            vehicle.set_profile(
                profile,
                duration,
            )
