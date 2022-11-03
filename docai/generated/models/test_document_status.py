from enum import Enum


class TestDocumentStatus(str, Enum):
    UPLOADINGFILE = "UploadingFile"
    DETECTINGTEXT = "DetectingText"
    EXTRACTINGDATA = "ExtractingData"
    REEXTRACTINGDATA = "ReExtractingData"
    WAITINGFORBUTLEROPSREVIEW = "WaitingForButlerOpsReview"
    COMPLETED = "Completed"
    FAILED = "Failed"

    def __str__(self) -> str:
        return str(self.value)
