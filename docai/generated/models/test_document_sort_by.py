from enum import Enum


class TestDocumentSortBy(str, Enum):
    UPLOADTIME = "UploadTime"

    def __str__(self) -> str:
        return str(self.value)
