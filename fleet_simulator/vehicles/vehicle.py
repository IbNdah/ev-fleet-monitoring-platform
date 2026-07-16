# region Imports

from fleet_simulator.telemetry.vehicle_profiles import VehicleProfiles
from fleet_simulator.vehicles.battery_ecu import BatteryECU

# endregion


# region Vehicle Model


class Vehicle:
    """
    EV Fleet Monitoring Platform

    Vehicle Model

    Responsibilities
    ----------------
    Represent a simulated electric vehicle.

    The Vehicle acts as an orchestrator between the
    FleetScenarioEngine and the BatteryECU.

    Architecture
    ------------
    FleetScenarioEngine
            │
            ▼
      Vehicle Profile
            │
            ▼
          Vehicle
            │
            ▼
        BatteryECU
            │
            ▼
      Telemetry Payload
    """

    # endregion

    # region Constructor

    def __init__(self, vehicle_id: str):
        """
        Create a simulated electric vehicle.
        """

        self.vehicle_id = vehicle_id
        self.battery_ecu = BatteryECU(device_id=f"BATT-{vehicle_id}")

        # Default operating profile

        self.profile = VehicleProfiles.PARKED

        # Remaining simulation cycles before
        # requesting a new operating profile.

        self.profile_cycles_remaining = 0

    # endregion

    # region Properties

    @property
    def state(self):
        """
        Return the current vehicle operating state.
        """

        return self.profile.vehicle_state

    # endregion

    # region Vehicle Profile Management

    def set_profile(
        self,
        profile,
        duration,
    ):
        """
        Assign a new operating profile.

        Parameters
        ----------
        profile : VehicleProfile

            Operating profile selected by the
            FleetScenarioEngine.

        duration : int

            Number of simulation cycles during
            which the profile remains active.
        """

        self.profile = profile
        self.profile_cycles_remaining = duration

    # endregion

    # region Simulation

    def simulate_cycle(self):
        """
        Execute one complete simulation cycle.

        Returns
        -------
        dict

            Vehicle telemetry payload.
        """

        telemetry = self.battery_ecu.update(
            self.profile,
        )

        # Vehicle metadata
        telemetry["vehicleId"] = self.vehicle_id
        telemetry["vehicleProfile"] = self.profile.name
        telemetry["vehicleState"] = telemetry["state"]

        return telemetry

    # endregion
