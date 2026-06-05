from enum import Enum


class Scenario(Enum):
    """Supported fleet simulation scenarios."""

    NORMAL_DRIVING = "NORMAL_DRIVING"
    FAST_CHARGING = "FAST_CHARGING"
    LOW_BATTERY = "LOW_BATTERY"
    OVERHEATING = "OVERHEATING"