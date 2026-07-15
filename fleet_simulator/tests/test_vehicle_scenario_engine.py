from fleet_simulator.scenarios.fleet_scenario_engine import (
    FleetScenarioEngine,
)
from fleet_simulator.vehicles.vehicle import Vehicle


def test_profile_assignment():

    vehicles = [Vehicle(f"EV-{i:03}") for i in range(1, 6)]

    FleetScenarioEngine.assign_profiles(vehicles)

    for vehicle in vehicles:

        assert vehicle.profile is not None

        assert vehicle.profile_cycles_remaining > 0


def test_vehicle_count():

    vehicles = [Vehicle(f"EV-{i:03}") for i in range(1, 6)]

    assert len(vehicles) == 5
