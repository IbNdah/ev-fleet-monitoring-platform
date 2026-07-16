from fleet_simulator.telemetry.vehicle_profiles import (
    VehicleProfiles,
)
from fleet_simulator.vehicles.battery_ecu import BatteryECU


def test_battery_limits():

    battery = BatteryECU("EV-001")

    telemetry = battery.update(VehicleProfiles.DRIVING)

    assert 0 <= telemetry["soc"] <= 100

    assert -20 <= telemetry["temperature"] <= 80

    assert 3.0 <= telemetry["voltage"] <= 4.2


def test_low_battery_profile():

    battery = BatteryECU("EV-001")
    battery.soc = 40

    telemetry = battery.update(VehicleProfiles.LOW_BATTERY)

    assert telemetry["state"] == "DRIVING"
    assert telemetry["soc"] <= 15


def test_overheating_profile():

    battery = BatteryECU("EV-001")

    telemetry = battery.update(VehicleProfiles.OVERHEATING)

    assert telemetry["faultCode"] == "OVERHEAT"
