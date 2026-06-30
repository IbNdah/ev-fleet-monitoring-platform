from fleet_simulator.vehicles.vehicle import Vehicle


def test_change_state():
    """
    Verify that changing the vehicle state updates both
    Vehicle and BatteryECU states.
    """

    vehicle = Vehicle("EV-001")

    vehicle.change_state("DRIVING")

    assert vehicle.state == "DRIVING"
    assert vehicle.battery_ecu.state == "DRIVING"
