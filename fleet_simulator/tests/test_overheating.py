from fleet_simulator.telemetry.telemetry_generator import TelemetryGenerator
from fleet_simulator.telemetry.scenarios import Scenario
from fleet_simulator.vehicles.vehicle import Vehicle


def test_overheating_scenario():
    """
    Verify that OVERHEATING forces temperature to 70°C.
    """

    vehicle = Vehicle("EV-001")

    vehicle.set_scenario(
        Scenario.OVERHEATING
    )

    TelemetryGenerator.apply_scenario(vehicle)

    assert vehicle.battery_ecu.temperature == 70