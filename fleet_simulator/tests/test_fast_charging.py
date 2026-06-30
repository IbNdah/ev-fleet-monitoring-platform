from fleet_simulator.telemetry.scenarios import Scenario
from fleet_simulator.telemetry.telemetry_generator import TelemetryGenerator
from fleet_simulator.vehicles.vehicle import Vehicle


def test_fast_charging_scenario():
    """
    Verify that FAST_CHARGING puts the vehicle in CHARGING state.
    """

    vehicle = Vehicle("EV-001")

    vehicle.set_scenario(Scenario.FAST_CHARGING)

    TelemetryGenerator.apply_scenario(vehicle)

    assert vehicle.state == "CHARGING"
