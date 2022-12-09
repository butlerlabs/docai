from enum import Enum


class PredictionDocumentsSortBy(str, Enum):
    CREATEDAT = "CreatedAt"

    def __str__(self) -> str:
        return str(self.value)
