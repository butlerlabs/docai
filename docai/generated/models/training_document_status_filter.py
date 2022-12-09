from enum import Enum


class TrainingDocumentStatusFilter(str, Enum):
    INPROGRESS = "InProgress"
    WAITINGFORUSERREVIEW = "WaitingForUserReview"
    COMPLETED = "Completed"

    def __str__(self) -> str:
        return str(self.value)
