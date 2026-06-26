"""
EV Fleet Monitoring Platform
Main entry point for the fleet simulator.

This module:
1. Creates a fleet of simulated EVs.
2. Runs telemetry simulation cycles.
3. Publishes telemetry data to MQTT.
4. Repeats continuously until interrupted.

Data flow:

Vehicle
    ↓
BatteryECU
    ↓
FleetSimulator
    ↓
MQTT Publisher
    ↓
Mosquitto Broker
"""

from time import sleep

from fleet_simulator.fleet_manager import FleetSimulator
from fleet_simulator.vehicles.vehicle import Vehicle
from edge_gateway.mqtt_publisher import MQTTPublisher


TOPIC = "evfleet/telemetry/raw"                     # MQTT topic(raw) used for telemetry messages
SIMULATION_INTERVAL = 5                             # Delay between simulation cycles (seconds)


def main():
    """
    Start the EV fleet simulation.
    Creates simulated vehicles, publishes telemetry
    to MQTT, and continuously runs simulation cycles.
    """
    
    fleet = FleetSimulator()                        # Create fleet simulator

    fleet.add_vehicle(Vehicle("EV-001"))            # Add simulated vehicles
    fleet.add_vehicle(Vehicle("EV-002"))
    fleet.add_vehicle(Vehicle("EV-003"))
    fleet.add_vehicle(Vehicle("EV-004"))
    fleet.add_vehicle(Vehicle("EV-005"))


    publisher = MQTTPublisher()                     # Create MQTT publisher
    publisher.connect()                             # Connect to MQTT broker

    print("🚀...Fleet simulator started...🚀")
    print(f"📡...Publishing telemetry to topic...📡: {TOPIC}")

    try:

        while True:
            
            telemetry_batch = (fleet.simulate_cycle())     # Generate telemetry for all vehicles
            
            for telemetry in telemetry_batch:              # Publish telemetry of each vehicle

                publisher.publish(TOPIC,telemetry)
                print(f"📡...Published telemetry: {telemetry}")
                            
            print("⏱️... New publishing in 5s ...📦")

            sleep(SIMULATION_INTERVAL)                     # Wait until next simulation cycle
             

    except KeyboardInterrupt:
        print("\n... Stopping fleet simulator.⚠️")

    finally:
        publisher.disconnect()
        print("... MQTT connection closed!  ✅")
        print("                                   ")


if __name__ == "__main__":
    main()