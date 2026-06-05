from fleet_simulator.fleet_manager import FleetSimulator


def test_fleet_creation():
    """
    Verify that a FleetSimulator instance is created correctly.
    """

    fleet = FleetSimulator()

    assert fleet.vehicles == []