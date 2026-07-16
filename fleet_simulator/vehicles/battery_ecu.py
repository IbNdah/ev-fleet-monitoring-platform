# region Imports

import random
from datetime import UTC, datetime

from fleet_simulator.telemetry.vehicle_profiles import VehicleProfile

# endregion


# region Battery ECU


class BatteryECU:
    """
    EV Fleet Monitoring Platform

    Battery ECU

    Physics simulation engine responsible for generating
    realistic battery telemetry.

    Responsibilities
    ----------------
    - Simulate battery behaviour
    - Apply the operating profile selected by the
      FleetScenarioEngine
    - Produce telemetry payloads

    The BatteryECU never decides the vehicle state.
    """

    # region Constructor

    def __init__(self, device_id: str):

        self.device_id = device_id

        self.soc = random.uniform(60, 90)
        self.temperature = random.uniform(25, 35)
        self.voltage = 3.70
        self.current = 0.0

        self.state = "PARKED"
        self.fault_code = None

    # endregion

    # region Physics Engine

    def update(
        self,
        profile: VehicleProfile,
    ) -> dict:
        """Execute one battery simulation cycle."""

        self.state = profile.vehicle_state
        self.fault_code = profile.fault_code

        if profile.max_soc is not None:
            self.soc = min(self.soc, profile.max_soc)

        if profile.min_temperature is not None:
            self.temperature = max(
                self.temperature,
                profile.min_temperature,
            )

        self.voltage += random.uniform(-0.02, 0.02)

        # region Fault Simulation

        if self.state == "FAULT":

            self.current = 0.0

            self.temperature -= random.uniform(
                1.0,
                3.0,
            )

            if self.temperature <= 55:
                self.fault_code = None

        # endregion

        # region Driving Simulation

        elif self.state == "DRIVING":

            self.soc -= random.uniform(
                0.5,
                2.0,
            )

            self.temperature += random.uniform(
                0.3,
                1.0,
            )

            self.current = random.uniform(
                20,
                80,
            )

        # endregion

        # region Charging Simulation

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

        # endregion

        # region Parked Simulation

        elif self.state == "PARKED":

            self.current = random.uniform(
                -1.0,
                1.0,
            )

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

        # endregion

        else:
            self.current = 0.0

        self.soc = max(0, min(100, self.soc))
        self.temperature = max(-20, min(80, self.temperature))
        self.voltage = max(3.0, min(4.2, self.voltage))

        payload = {
            "deviceId": self.device_id,
            "temperature": round(self.temperature, 2),
            "current": round(self.current, 2),
            "voltage": round(self.voltage, 2),
            "soc": round(self.soc, 2),
            "state": self.state,
            "faultCode": self.fault_code,
            "timestamp": datetime.now(UTC).isoformat(),
        }

        return payload

    # endregion


# endregion
