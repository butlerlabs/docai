from enum import Enum


class TrainingDocumentStatus(str, Enum):
    UPLOADINGFILE = "UploadingFile"
    DETECTINGTEXT = "DetectingText"
    EXTRACTINGDATA = "ExtractingData"
    REEXTRACTINGDATA = "ReExtractingData"
    WAITINGFORBUTLEROPSREVIEW = "WaitingForButlerOpsReview"
    WAITINGFORUSERREVIEW = "WaitingForUserReview"
    COMPLETED = "Completed"
    FAILED = "Failed"
    EVALUATINGDOCUMENT = "EvaluatingDocument"

    def __str__(self) -> str:
        return str(self.value)
