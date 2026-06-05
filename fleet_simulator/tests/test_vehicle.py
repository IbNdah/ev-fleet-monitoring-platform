from fleet_simulator.vehicles.vehicle import Vehicle


def test_vehicle_creation():
    """
    Verify that a Vehicle instance is created with the expected
    default values.
    """

    vehicle = Vehicle("EV-001")

    assert vehicle.vehicle_id == "EV-001"
    assert vehicle.state == "PARKED"
    assert vehicle.battery_ecu is not None





