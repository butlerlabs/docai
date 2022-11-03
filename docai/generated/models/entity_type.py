from enum import Enum


class EntityType(str, Enum):
    TEXT = "Text"
    DATE = "Date"
    EMAIL = "Email"
    PHONE = "Phone"
    CURRENCY = "Currency"
    PERSON = "Person"
    ORGANIZATION = "Organization"
    NUMBER = "Number"
    ADDRESS = "Address"
    SIGNATUREPRESENT = "SignaturePresent"
    CURRENCYTYPE = "CurrencyType"
    CHECKBOX = "Checkbox"
    ADDRESS1 = "Address1"
    ADDRESS2 = "Address2"
    CITY = "City"
    STATEPROVINCE = "StateProvince"
    ZIPPOSTALCODE = "ZipPostalCode"
    COUNTRY = "Country"

    def __str__(self) -> str:
        return str(self.value)
