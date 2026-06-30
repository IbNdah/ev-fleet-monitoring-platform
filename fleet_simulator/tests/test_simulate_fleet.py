from fleet_simulator.fleet_manager import FleetSimulator
from fleet_simulator.vehicles.vehicle import Vehicle


def test_simulate_fleet():
    """
    Verify that telemetry is generated for all vehicles.
    """

    fleet = FleetSimulator()

    fleet.add_vehicle(Vehicle("EV-001"))
    fleet.add_vehicle(Vehicle("EV-002"))
    fleet.add_vehicle(Vehicle("EV-003"))

    telemetry = fleet.simulate_cycle()

    assert len(telemetry) == 3

    assert telemetry[0]["vehicleId"] == "EV-001"
    assert telemetry[1]["vehicleId"] == "EV-002"
    assert telemetry[2]["vehicleId"] == "EV-003"
