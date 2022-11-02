from enum import Enum


class UploadDocumentsExtraResultsItem(str, Enum):
    LINEBLOCKS = "LineBlocks"
    FORMFIELDS = "FormFields"
    TABLES = "Tables"

    def __str__(self) -> str:
        return str(self.value)
