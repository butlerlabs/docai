from enum import Enum


class SubmitTrainingDocumentsDisabledReason(str, Enum):
    MAXIMUMTRAININGDOCUMENTSREACHED = "MaximumTrainingDocumentsReached"
    NOTSUPPORTED = "NotSupported"
    PENDINGSCHEMACHANGES = "PendingSchemaChanges"

    def __str__(self) -> str:
        return str(self.value)
