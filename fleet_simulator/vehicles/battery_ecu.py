import random
from datetime import datetime


class BatteryECU:
    """Simulates an EV battery ECU and generates telemetry data."""

    def __init__(self, device_id):

        self.device_id = device_id

        # Battery parameters
        self.soc = 80
        self.temperature = 30
        self.voltage = 3.7
        self.current = 0

        # ECU status
        self.state = "PARKED"
        self.fault_code = None

    def update(self):
        """Simulate one telemetry cycle."""

        # Simulate sensor variations
        self.temperature += random.uniform(-1, 1)
        self.voltage += random.uniform(-0.02, 0.02)
        self.current += random.uniform(-0.2, 0.2)

        # Detect overheating fault
        if self.temperature > 60:
            self.state = "FAULT"
            self.fault_code = "OVERHEAT"
        else:
            # Clear fault when temperature returns to normal
            if self.state == "FAULT" and self.temperature <= 60:
                self.state = "PARKED"
                self.fault_code = None

        # Update SOC based on vehicle state
        if self.state == "DRIVING":
            self.soc -= random.uniform(0.05, 0.20)
        elif self.state == "CHARGING":
            self.soc += random.uniform(0.10, 0.30)

        # Keep SOC between 0% and 100%
        self.soc = max(0, min(100, self.soc))

        # Return telemetry payload
        return {
            "deviceId": self.device_id,
            "temperature": round(self.temperature, 2),
            "current": round(self.current, 2),
            "voltage": round(self.voltage, 2),
            "soc": round(self.soc, 2),
            "state": self.state,
            "faultCode": self.fault_code,
            "timestamp": datetime.utcnow().isoformat()
        }


# Quick test
battery = BatteryECU("EV-001")

for _ in range(10):
    print(battery.update())