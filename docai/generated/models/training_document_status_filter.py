from enum import Enum


class TrainingDocumentStatusFilter(str, Enum):
    INPROGRESS = "InProgress"
    WAITINGFORREVIEW = "WaitingForReview"
    COMPLETED = "Completed"

    def __str__(self) -> str:
        return str(self.value)
