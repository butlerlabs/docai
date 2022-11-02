from enum import Enum


class ModelTrainingDocumentStatus(str, Enum):
    OCRINPROGRESS = "OcrInProgress"
    NEEDSLABELS = "NeedsLabels"
    LABELED = "Labeled"
    OCRFAILED = "OcrFailed"

    def __str__(self) -> str:
        return str(self.value)
