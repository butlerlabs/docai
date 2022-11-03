from enum import Enum


class ModelSummaryBaseModelType(str, Enum):
    CUSTOM = "Custom"
    COMPOSED = "Composed"
    PRETRAINED = "Pretrained"
    LEGACY = "Legacy"

    def __str__(self) -> str:
        return str(self.value)
