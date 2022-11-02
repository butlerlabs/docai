from enum import Enum


class UploadDocumentsToQueueExtraResultsItem(str, Enum):
    LINEBLOCKS = "LineBlocks"
    FORMFIELDS = "FormFields"
    TABLES = "Tables"

    def __str__(self) -> str:
        return str(self.value)
