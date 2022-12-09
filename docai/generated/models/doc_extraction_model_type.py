from enum import Enum


class DocExtractionModelType(str, Enum):
    CUSTOM = "Custom"
    PRETRAINED = "Pretrained"
    LEGACY = "Legacy"

    def __str__(self) -> str:
        return str(self.value)
