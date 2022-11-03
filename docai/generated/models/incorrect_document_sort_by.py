from enum import Enum


class IncorrectDocumentSortBy(str, Enum):
    REVIEWTIME = "ReviewTime"

    def __str__(self) -> str:
        return str(self.value)
