from datetime import datetime, UTC
from fleet_simulator.vehicles.battery_ecu import BatteryECU


class Vehicle:
    """Simulates an EV vehicle and manages its components."""

    def __init__(self, vehicle_id):
        self.vehicle_id = vehicle_id                          # Unique identifier for the vehicle
        self.battery_ecu = BatteryECU(f"BATT-{vehicle_id}")   # Initialize the battery ECU with a unique device ID
        self.state = "PARKED"                                 # Current state of the vehicle


    def change_state(self, new_state):
        """Change the vehicle's state and update the battery ECU accordingly."""

        valid_states = ["PARKED", "DRIVING", "CHARGING"]
        
        if new_state in valid_states:
            self.state = new_state
            self.battery_ecu.state = new_state
        else:
            raise ValueError(f"Invalid state: {new_state}. Valid states are: {valid_states}")
        
        
        
    def simulate_cycle(self):
        
        """Simulate one telemetry cycle and return the battery ECU data."""
        telemetry = self.battery_ecu.update()
        
        # Add vehicle-level data to the telemetry
        telemetry["vehicleId"] = self.vehicle_id
        telemetry["vehicleState"] = self.state
               
        return telemetry
     
# Quick test
if __name__ == "__main__":
    vehicle = Vehicle("EV-001")
    vehicle.change_state("DRIVING")

    for _ in range(10):
        print(vehicle.simulate_cycle())