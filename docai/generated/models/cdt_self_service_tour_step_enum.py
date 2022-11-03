from enum import Enum


class CdtSelfServiceTourStepEnum(str, Enum):
    NOTYETSTARTED = "NotYetStarted"
    LEARNABOUTMODELS = "LearnAboutModels"
    CREATEAMODEL = "CreateAModel"
    LEARNABOUTFIELDS = "LearnAboutFields"
    LEARNABOUTFIELDNAMES = "LearnAboutFieldNames"
    UPLOADDOCSTOTRAINING = "UploadDocsToTraining"
    SELECTAVALUE = "SelectAValue"
    SELECTAKEY = "SelectAKey"
    SAVELABELS = "SaveLabels"
    TRAINADOCTYPE = "TrainADocType"
    GOTOLIVETEST = "GoToLiveTest"
    UPLOADDOCSTOLIVETEST = "UploadDocsToLiveTest"
    LEARNABOUTEXTRACTIONRESULTS = "LearnAboutExtractionResults"
    GIVEEXTRACTIONFEEDBACK = "GiveExtractionFeedback"
    INTEGRATEWITHAPIS = "IntegrateWithApis"
    GOTOQUEUES = "GoToQueues"
    LEARNABOUTQUEUES = "LearnAboutQueues"
    INTEGRATEWITHQUEUES = "IntegrateWithQueues"
    NEEDHELP = "NeedHelp"
    COMPLETED = "Completed"

    def __str__(self) -> str:
        return str(self.value)
