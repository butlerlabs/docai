from enum import Enum


class TrainingDisabledReason(str, Enum):
    NOTENOUGHDOCUMENTSLABELED = "NotEnoughDocumentsLabeled"

    def __str__(self) -> str:
        return str(self.value)
