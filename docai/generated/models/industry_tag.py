from enum import Enum


class IndustryTag(str, Enum):
    FINANCIALSERVICES = "FinancialServices"
    INSURANCE = "Insurance"
    LOGISTICSANDSUPPLYCHAIN = "LogisticsAndSupplyChain"
    REALESTATE = "RealEstate"
    PROCUREMENT = "Procurement"
    OTHER = "Other"

    def __str__(self) -> str:
        return str(self.value)
