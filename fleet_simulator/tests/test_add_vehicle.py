from fleet_simulator.fleet_manager import FleetSimulator
from fleet_simulator.vehicles.vehicle import Vehicle


def test_add_vehicle():
    """
    Verify that a vehicle can be added to the fleet.
    """

    fleet = FleetSimulator()
    vehicle = Vehicle("EV-001")

    fleet.add_vehicle(vehicle)

    assert len(fleet.vehicles) == 1
    assert fleet.vehicles[0] == vehicle
