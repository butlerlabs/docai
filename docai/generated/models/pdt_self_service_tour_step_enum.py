from enum import Enum


class PdtSelfServiceTourStepEnum(str, Enum):
    NOTYETSTARTED = "NotYetStarted"
    LEARNABOUTMODELS = "LearnAboutModels"
    PICKAMODEL = "PickAModel"
    UPLOADDOCSTOLIVETEST = "UploadDocsToLiveTest"
    LEARNABOUTEXTRACTIONRESULTS = "LearnAboutExtractionResults"
    GIVEEXTRACTIONFEEDBACK = "GiveExtractionFeedback"
    INTEGRATEWITHAPIS = "IntegrateWithApis"
    GOTOQUEUES = "GoToQueues"
    LEARNABOUTQUEUES = "LearnAboutQueues"
    INTEGRATEWITHQUEUES = "IntegrateWithQueues"
    NEEDHELP = "NeedHelp"
    CUSTOMIZEDOCTYPE = "CustomizeDocType"
    COMPLETED = "Completed"

    def __str__(self) -> str:
        return str(self.value)
