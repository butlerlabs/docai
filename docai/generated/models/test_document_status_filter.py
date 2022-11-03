from enum import Enum


class TestDocumentStatusFilter(str, Enum):
    INPROGRESS = "InProgress"
    COMPLETED = "Completed"

    def __str__(self) -> str:
        return str(self.value)
