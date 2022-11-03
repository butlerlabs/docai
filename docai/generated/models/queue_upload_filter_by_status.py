from enum import Enum


class QueueUploadFilterByStatus(str, Enum):
    INPROGRESS = "InProgress"
    WAITING = "Waiting"
    COMPLETED = "Completed"
    FAILED = "Failed"

    def __str__(self) -> str:
        return str(self.value)
