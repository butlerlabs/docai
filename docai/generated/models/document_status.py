from enum import Enum


class DocumentStatus(str, Enum):
    UPLOADINGFILE = "UploadingFile"
    DETECTINGTEXT = "DetectingText"
    EXTRACTINGDATA = "ExtractingData"
    WAITINGFORBUTLEROPSREVIEW = "WaitingForButlerOpsReview"
    WAITINGFORUSERREVIEW = "WaitingForUserReview"
    COMPLETED = "Completed"
    FAILED = "Failed"

    def __str__(self) -> str:
        return str(self.value)
