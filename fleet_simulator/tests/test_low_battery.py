from fleet_simulator.telemetry.telemetry_generator import TelemetryGenerator
from fleet_simulator.telemetry.scenarios import Scenario
from fleet_simulator.vehicles.vehicle import Vehicle


def test_low_battery_scenario():
    """
    Verify that LOW_BATTERY forces SOC to 10%.
    """

    vehicle = Vehicle("EV-001")

    vehicle.set_scenario(
        Scenario.LOW_BATTERY
    )

    TelemetryGenerator.apply_scenario(vehicle)

    assert vehicle.battery_ecu.soc == 10