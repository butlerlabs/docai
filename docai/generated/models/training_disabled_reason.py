from enum import Enum


class TrainingDisabledReason(str, Enum):
    NOTENOUGHDOCUMENTSLABELED = "NotEnoughDocumentsLabeled"
    NOTSUPPORTED = "NotSupported"
    SUPPORTTRAININGONLY = "SupportTrainingOnly"

    def __str__(self) -> str:
        return str(self.value)
