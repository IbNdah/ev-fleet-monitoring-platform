# region Imports

from fleet_simulator.scenarios.fleet_scenario_engine import (
    FleetScenarioEngine,
)

# endregion


# region Fleet Simulator


class FleetSimulator:
    """
    EV Fleet Monitoring Platform

    Fleet Simulator

    Responsibilities
    ----------------
    Coordinate the complete fleet simulation.

    The FleetSimulator orchestrates the different
    simulator components but never generates telemetry
    itself.

    Architecture
    ------------
    FleetSimulator
            │
            ▼
    FleetScenarioEngine
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

    def __init__(self):
        """
        Create an empty simulated fleet.
        """

        self.vehicles = []

    # endregion

    # region Fleet Management

    def add_vehicle(self, vehicle):
        """
        Register a vehicle in the simulated fleet.

        Parameters
        ----------
        vehicle : Vehicle
            Vehicle instance to register.
        """

        self.vehicles.append(vehicle)

    # endregion

    # region Fleet Simulation

    def simulate_cycle(self):
        """
        Execute one complete fleet simulation cycle.

        Workflow
        --------
        1. Assign operating profiles.
        2. Simulate every vehicle.
        3. Return the telemetry batch.

        Returns
        -------
        list[dict]
            Fleet telemetry batch.
        """

        # -----------------------------------------
        # Assign operating profiles
        # -----------------------------------------

        FleetScenarioEngine.assign_profiles(
            self.vehicles,
        )

        # -----------------------------------------
        # Simulate fleet
        # -----------------------------------------

        telemetry_batch = []

        for vehicle in self.vehicles:

            telemetry_batch.append(
                vehicle.simulate_cycle(),
            )

        return telemetry_batch

    # endregion
