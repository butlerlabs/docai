from enum import Enum


class DocumentStatus(str, Enum):
    INPROGRESS = "InProgress"
    WAITINGFORUSERREVIEW = "WaitingForUserReview"
    COMPLETED = "Completed"
    FAILED = "Failed"

    def __str__(self) -> str:
        return str(self.value)
