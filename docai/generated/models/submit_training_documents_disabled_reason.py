from enum import Enum


class SubmitTrainingDocumentsDisabledReason(str, Enum):
    MAXIMUMTRAININGDOCUMENTSREACHED = "MaximumTrainingDocumentsReached"

    def __str__(self) -> str:
        return str(self.value)
