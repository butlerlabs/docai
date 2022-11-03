from enum import Enum


class TrainingACustomModelTourStepEnum(str, Enum):
    NOTYETSTARTED = "NotYetStarted"
    LEARNABOUTCUSTOMMODELS = "LearnAboutCustomModels"
    NAMEYOURMODEL = "NameYourModel"
    UPLOADSOMEDOCS = "UploadSomeDocs"
    ADDAFIELD = "AddAField"
    LABELAFIELD = "LabelAField"
    ADDMOREFIELDS = "AddMoreFields"
    LABELMOREDOCS = "LabelMoreDocs"
    LEARNABOUTDOCUMENTCARDS = "LearnAboutDocumentCards"
    STARTTRAINING = "StartTraining"
    COMPLETED = "Completed"

    def __str__(self) -> str:
        return str(self.value)
