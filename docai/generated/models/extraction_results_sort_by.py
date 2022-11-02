from enum import Enum


class ExtractionResultsSortBy(str, Enum):
    DOCUMENTID = "DocumentId"

    def __str__(self) -> str:
        return str(self.value)
