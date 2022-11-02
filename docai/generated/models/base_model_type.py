from enum import Enum


class BaseModelType(str, Enum):
    INVOICEV2 = "InvoiceV2"
    INVOICE = "Invoice"
    PASSPORTV2 = "PassportV2"
    PASSPORT = "Passport"
    RECEIPTV2 = "ReceiptV2"
    RECEIPT = "Receipt"
    USDRIVERSLICENSEV2 = "USDriversLicenseV2"
    USDRIVERSLICENSE = "USDriversLicense"
    HEALTHINSURANCECARD = "HealthInsuranceCard"
    IDCARD = "IdCard"
    BANKSTATEMENT = "BankStatement"
    PAYSLIP = "PaySlip"
    W2 = "W2"
    W9 = "W9"
    IRS1040STANDARD = "IRS1040Standard"
    MORTGAGE = "Mortgage"
    UTILITY = "Utility"
    LEGACYCUSTOM = "LegacyCustom"
    CUSTOMFORM = "CustomForm"
    COMPOSED = "Composed"

    def __str__(self) -> str:
        return str(self.value)
