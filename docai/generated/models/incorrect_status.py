from enum import Enum


class IncorrectStatus(str, Enum):
    DISPUTED = "Disputed"
    CRITICAL = "Critical"
    MINOR = "Minor"

    def __str__(self) -> str:
        return str(self.value)
