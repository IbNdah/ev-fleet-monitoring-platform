from fleet_simulator.telemetry.vehicle_profiles import (
    VehicleProfiles,
)


def test_driving_profile():

    assert VehicleProfiles.DRIVING.name == "DRIVING"
    assert VehicleProfiles.DRIVING.vehicle_state == "DRIVING"


def test_charging_profile():

    assert VehicleProfiles.CHARGING.name == "CHARGING"
    assert VehicleProfiles.CHARGING.vehicle_state == "CHARGING"


def test_low_battery_profile():

    assert VehicleProfiles.LOW_BATTERY.max_soc == 15
    assert VehicleProfiles.LOW_BATTERY.vehicle_state == "DRIVING"


def test_overheating_profile():

    assert VehicleProfiles.OVERHEATING.vehicle_state == "FAULT"
    assert VehicleProfiles.OVERHEATING.fault_code == "OVERHEAT"
