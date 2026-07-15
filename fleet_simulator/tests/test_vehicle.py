from fleet_simulator.telemetry.vehicle_profiles import (
    VehicleProfiles,
)
from fleet_simulator.vehicles.vehicle import Vehicle


def test_vehicle_generates_complete_telemetry():

    vehicle = Vehicle("EV-001")

    vehicle.set_profile(
        VehicleProfiles.DRIVING,
        duration=5,
    )

    telemetry = vehicle.simulate_cycle()

    assert telemetry["vehicleId"] == "EV-001"

    assert "soc" in telemetry
    assert "temperature" in telemetry
    assert "voltage" in telemetry
    assert "current" in telemetry

    assert "vehicleProfile" in telemetry
    assert "vehicleState" in telemetry
