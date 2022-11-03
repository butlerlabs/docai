from enum import Enum


class QueueUploadStatus(str, Enum):
    UPLOADINGFILES = "UploadingFiles"
    DETECTINGTEXT = "DetectingText"
    EXTRACTINGDATA = "ExtractingData"
    WAITINGFORBUTLEROPSREVIEW = "WaitingForButlerOpsReview"
    WAITINGFORUSERREVIEW = "WaitingForUserReview"
    GENERATINGRESULTS = "GeneratingResults"
    COMPLETED = "Completed"
    FAILED = "Failed"

    def __str__(self) -> str:
        return str(self.value)
