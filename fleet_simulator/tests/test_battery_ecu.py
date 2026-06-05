from fleet_simulator.vehicles.vehicle import Vehicle

def test_simulate_cycle():
    """
    Verify that a telemetry payload is generated and contains
    the expected fields.
    """

    vehicle = Vehicle("EV-001")

    vehicle.change_state("DRIVING")

    telemetry = vehicle.simulate_cycle()

    expected_keys = [
        "deviceId",
        "temperature",
        "current",
        "voltage",
        "soc",
        "state",
        "faultCode",
        "timestamp",
        "vehicleId",
        "vehicleState",
    ]

    for key in expected_keys:
        assert key in telemetry

    assert telemetry["vehicleId"] == "EV-001"
    assert telemetry["vehicleState"] == "DRIVING"