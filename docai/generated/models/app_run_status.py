from enum import Enum


class AppRunStatus(str, Enum):
    INPROGRESS = "InProgress"
    COMPLETED = "Completed"
    FAILED = "Failed"
    WAITING = "Waiting"

    def __str__(self) -> str:
        return str(self.value)
