from enum import Enum


class TestDocumentStatus(str, Enum):
    INPROGRESS = "InProgress"
    COMPLETED = "Completed"
    FAILED = "Failed"

    def __str__(self) -> str:
        return str(self.value)
