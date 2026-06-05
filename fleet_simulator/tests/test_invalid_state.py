import pytest

from fleet_simulator.vehicles.vehicle import Vehicle


def test_invalid_state():
    """
    Verify that an invalid vehicle state raises a ValueError.
    """

    vehicle = Vehicle("EV-001")

    with pytest.raises(ValueError):
        vehicle.change_state("SINKING")