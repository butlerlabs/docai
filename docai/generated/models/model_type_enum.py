from enum import Enum


class ModelTypeEnum(str, Enum):
    IMAGECLASSIFICATION = "ImageClassification"
    OBJECTDETECTION = "ObjectDetection"

    def __str__(self) -> str:
        return str(self.value)
