from enum import Enum


class ModelStatus(str, Enum):
    NEEDSTRAINING = "NeedsTraining"
    TRAINING = "Training"
    ACTIVE = "Active"

    def __str__(self) -> str:
        return str(self.value)
