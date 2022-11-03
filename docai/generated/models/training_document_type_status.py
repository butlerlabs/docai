from enum import Enum


class TrainingDocumentTypeStatus(str, Enum):
    ENABLED = "Enabled"
    NOTENOUGHDOCSLABELED = "NotEnoughDocsLabeled"
    DOCUMENTSNEEDREVIEW = "DocumentsNeedReview"
    NOADDITIONALTRAINING = "NoAdditionalTraining"
    TESTDOCUMENTSINPROGRESS = "TestDocumentsInProgress"

    def __str__(self) -> str:
        return str(self.value)
