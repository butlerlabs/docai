from enum import Enum


class AllowanceRefreshInterval(str, Enum):
    MONTHLY = "Monthly"
    NEVER = "Never"

    def __str__(self) -> str:
        return str(self.value)
