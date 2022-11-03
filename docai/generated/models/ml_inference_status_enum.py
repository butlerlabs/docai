from enum import Enum


class MlInferenceStatusEnum(str, Enum):
    REQUESTED = "Requested"
    RUNNING = "Running"
    DONE = "Done"
    FAILED = "Failed"

    def __str__(self) -> str:
        return str(self.value)
