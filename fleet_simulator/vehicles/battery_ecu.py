import random
from datetime import UTC, datetime


class BatteryECU:
    """
    Simulates an EV Battery ECU.

    Responsibilities
    ----------------
    - Simulate realistic battery behaviour
    - Handle charging/discharging cycles
    - Manage thermal behaviour
    - Detect and recover from overheating

    The BatteryECU does NOT decide vehicle behaviour.
    It only applies the operating profile assigned by the
    FleetScenarioEngine.
    """

    def __init__(self, device_id: str):

        self.device_id = device_id

        # Battery parameters
        self.soc = random.uniform(60, 90)
        self.temperature = random.uniform(25, 35)
        self.voltage = 3.7
        self.current = 0

        # ECU state
        self.state = "PARKED"
        self.fault_code = None

    # ---------------------------------------------------------
    # Physics Engine
    # ---------------------------------------------------------

    def update(self, profile):
        """
        Execute one physical simulation cycle.
        """
        # Apply operating profile
        self.state = profile.vehicle_state

        if profile.max_soc is not None:
            self.soc = min(self.soc, profile.max_soc)

        if profile.min_temperature is not None:
            self.temperature = max(
                self.temperature,
                profile.min_temperature,
            )

        self.fault_code = profile.fault_code

        # Small voltage variation
        self.voltage += random.uniform(-0.02, 0.02)

        # ==================================================
        # FAULT MODE
        # ==================================================

        if self.state == "FAULT":

            self.current = 0

            # Active cooling
            self.temperature -= random.uniform(1.0, 3.0)

            if self.temperature <= 55:

                self.state = "PARKED"
                self.fault_code = None

        # ==================================================
        # NORMAL OPERATION
        # ==================================================

        else:

            # Automatic charging
            if self.soc <= 15:

                self.state = "CHARGING"

            elif random.random() < 0.05:

                self.state = random.choice(
                    [
                        "DRIVING",
                        "PARKED",
                    ]
                )

            # ---------------------------------------------
            # Driving
            # ---------------------------------------------

            if self.state == "DRIVING":

                self.soc -= random.uniform(0.5, 2.0)

                self.temperature += random.uniform(
                    0.3,
                    1.0,
                )

                self.current = random.uniform(
                    20,
                    80,
                )

                if self.temperature >= 55:

                    self.state = "PARKED"

            # ---------------------------------------------
            # Charging
            # ---------------------------------------------

            elif self.state == "CHARGING":

                self.soc += random.uniform(
                    2.0,
                    5.0,
                )

                self.temperature += random.uniform(
                    -0.5,
                    0.3,
                )

                self.current = random.uniform(
                    -40,
                    -10,
                )

                if self.soc >= 90:

                    self.state = "PARKED"

            # ---------------------------------------------
            # Parked
            # ---------------------------------------------

            elif self.state == "PARKED":

                self.current = random.uniform(-1, 1)

                if self.temperature > 35:

                    self.temperature -= random.uniform(
                        0.3,
                        1.0,
                    )

                else:

                    self.temperature += random.uniform(
                        -0.2,
                        0.2,
                    )

                if self.temperature < 45 and random.random() < 0.05:

                    self.state = "DRIVING"

            # ---------------------------------------------
            # Thermal protection
            # ---------------------------------------------

            if self.temperature > 70:

                self.state = "FAULT"
                self.fault_code = "OVERHEAT"

        # ==================================================
        # Physical limits
        # ==================================================

        self.soc = max(0, min(100, self.soc))
        self.temperature = max(-20, min(80, self.temperature))
        self.voltage = max(3.0, min(4.2, self.voltage))

        # ==================================================
        # Telemetry payload
        # ==================================================

        return {
            "deviceId": self.device_id,
            "temperature": round(self.temperature, 2),
            "current": round(self.current, 2),
            "voltage": round(self.voltage, 2),
            "soc": round(self.soc, 2),
            "state": self.state,
            "faultCode": self.fault_code,
            "timestamp": datetime.now(UTC).isoformat(),
        }
