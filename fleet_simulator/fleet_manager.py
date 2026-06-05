from fleet_simulator.vehicles.vehicle import Vehicle


class FleetSimulator:
    """Manages a fleet of simulated EVs."""

    def __init__(self):

        # List of vehicles in the fleet
        self.vehicles = []

    def add_vehicle(self, vehicle):
        """Add a vehicle to the fleet."""

        self.vehicles.append(vehicle)

    def simulate_cycle(self):
        """Run one simulation cycle for all vehicles."""

        telemetry_data = []

        for vehicle in self.vehicles:
            telemetry_data.append(
                vehicle.simulate_cycle()
            )

        return telemetry_data


# Quick test
if __name__ == "__main__":

    fleet = FleetSimulator()

    fleet.add_vehicle(
        Vehicle("EV-001")
    )

    fleet.add_vehicle(
        Vehicle("EV-002")
    )

    telemetry = fleet.simulate_cycle()

    print(telemetry)