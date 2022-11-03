from enum import Enum


class FeatureName(str, Enum):
    ADDRESSCOMPONENTS = "AddressComponents"
    BILLING = "Billing"
    BDT = "Bdt"
    BUTLERREVIEWER = "ButlerReviewer"
    CHECKBOX = "Checkbox"
    CREATEDOCTYPE = "CreateDocType"
    CURRENCYTYPE = "CurrencyType"
    EMAILVERIFICATION = "EmailVerification"
    ENFORCEBILLING = "EnforceBilling"
    SELFSERVICEONBOARDING = "SelfServiceOnboarding"
    SIGNATURE = "Signature"
    ADVANCEDQUEUES = "AdvancedQueues"
    DOCUMENTRESULTSDISPLAYER = "DocumentResultsDisplayer"
    DASHBOARDUI = "DashboardUI"

    def __str__(self) -> str:
        return str(self.value)
