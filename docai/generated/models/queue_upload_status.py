from enum import Enum


class QueueUploadStatus(str, Enum):
    INPROGRESS = "InProgress"
    WAITINGFORUSERREVIEW = "WaitingForUserReview"
    GENERATINGRESULTS = "GeneratingResults"
    COMPLETED = "Completed"
    FAILED = "Failed"

    def __str__(self) -> str:
        return str(self.value)
