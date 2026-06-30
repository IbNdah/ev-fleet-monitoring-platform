from fleet_simulator.telemetry.scenarios import Scenario


class TelemetryGenerator:
    """Applies simulation scenarios to vehicles."""

    @staticmethod
    def apply_scenario(vehicle):
        """Apply the vehicle's current scenario."""

        if vehicle.scenario == Scenario.NORMAL_DRIVING:

            vehicle.change_state("DRIVING")

        elif vehicle.scenario == Scenario.FAST_CHARGING:

            vehicle.change_state("CHARGING")

        elif vehicle.scenario == Scenario.LOW_BATTERY:

            vehicle.battery_ecu.soc = 10

        elif vehicle.scenario == Scenario.OVERHEATING:

            vehicle.battery_ecu.temperature = 70

        else:

            raise ValueError(f"Unsupported scenario: {vehicle.scenario}")
