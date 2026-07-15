"""
EV Fleet Monitoring Platform

Vehicle Model

Represents a simulated electric vehicle.

Responsibilities
----------------
- Own a BatteryECU.
- Store the current operating profile.
- Produce one telemetry cycle.

The FleetScenarioEngine decides the operating profile.
The BatteryECU generates realistic telemetry.
"""

from fleet_simulator.telemetry.vehicle_profiles import VehicleProfiles
from fleet_simulator.vehicles.battery_ecu import BatteryECU


class Vehicle:
    """Represents a simulated electric vehicle."""

    def __init__(self, vehicle_id: str):

        self.vehicle_id = vehicle_id

        self.battery_ecu = BatteryECU(device_id=f"BATT-{vehicle_id}")

        # Default profile
        self.profile = VehicleProfiles.PARKED

        # Number of remaining cycles before assigning a new profile
        self.profile_cycles_remaining = 0

    @property
    def state(self):
        """Current operating state."""

        return self.profile.vehicle_state

    def set_profile(self, profile, duration):
        """
        Assign a new operating profile.

        Parameters
        ----------
        profile : VehicleProfile
            Operating profile assigned by the FleetScenarioEngine.

        duration : int
            Number of simulation cycles the profile remains active.
        """

        self.profile = profile
        self.profile_cycles_remaining = duration

    def simulate_cycle(self):
        """
        Execute one simulation cycle.

        Returns
        -------
        dict
            Vehicle telemetry payload.
        """

        telemetry = self.battery_ecu.update(self.profile)

        telemetry["vehicleId"] = self.vehicle_id
        telemetry["vehicleProfile"] = self.profile.name
        telemetry["vehicleState"] = telemetry["state"]
        return telemetry
