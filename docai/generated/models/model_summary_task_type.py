from enum import Enum


class ModelSummaryTaskType(str, Enum):
    CUSTOMDOCUMENTEXTRACTION = "CustomDocumentExtraction"
    IMAGECLASSIFICATION = "ImageClassification"

    def __str__(self) -> str:
        return str(self.value)
