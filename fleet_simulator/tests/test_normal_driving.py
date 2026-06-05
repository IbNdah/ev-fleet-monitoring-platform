from fleet_simulator.telemetry.telemetry_generator import TelemetryGenerator
from fleet_simulator.telemetry.scenarios import Scenario
from fleet_simulator.vehicles.vehicle import Vehicle


def test_normal_driving_scenario():
    """
    Verify that NORMAL_DRIVING puts the vehicle in DRIVING state.
    """

    vehicle = Vehicle("EV-001")

    vehicle.set_scenario(
        Scenario.NORMAL_DRIVING
    )

    TelemetryGenerator.apply_scenario(vehicle)

    assert vehicle.state == "DRIVING"