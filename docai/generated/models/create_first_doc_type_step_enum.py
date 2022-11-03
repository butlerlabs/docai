from enum import Enum


class CreateFirstDocTypeStepEnum(str, Enum):
    NOTYETSTARTED = "NotYetStarted"
    CREATENEWDOCTYPE = "CreateNewDocType"
    LEARNABOUTQUEUES = "LearnAboutQueues"
    UPLOADDOCSTOQUEUE = "UploadDocsToQueue"
    LEARNABOUTBUTLEROPS = "LearnAboutButlerOps"
    CHECKOUTDOCUMENTATION = "CheckOutDocumentation"
    LINKTODOCTYPES = "LinkToDocTypes"
    LEARNABOUTDOCUMENTACCURACY = "LearnAboutDocumentAccuracy"
    TRAININGDOCTYPE = "TrainingDocType"
    COMPLETED = "Completed"

    def __str__(self) -> str:
        return str(self.value)
