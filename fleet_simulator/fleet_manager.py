"""
EV Fleet Monitoring Platform

Fleet Manager

Coordinates the complete fleet simulation.

Responsibilities
----------------
- Maintain the vehicle fleet.
- Ask the FleetScenarioEngine to assign profiles.
- Execute one simulation cycle.
- Return telemetry for the complete fleet.
"""

from fleet_simulator.scenarios.fleet_scenario_engine import (
    FleetScenarioEngine,
)


class FleetSimulator:
    """Coordinates the complete fleet simulation."""

    def __init__(self):

        self.vehicles = []

    def add_vehicle(self, vehicle):
        """
        Register a vehicle in the fleet.
        """

        self.vehicles.append(vehicle)

    def simulate_cycle(self):
        """
        Execute one simulation cycle for the complete fleet.
        """

        FleetScenarioEngine.assign_profiles(self.vehicles)

        telemetry_batch = []

        for vehicle in self.vehicles:

            telemetry_batch.append(vehicle.simulate_cycle())

        return telemetry_batch
