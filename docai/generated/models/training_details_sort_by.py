from enum import Enum


class TrainingDetailsSortBy(str, Enum):
    CREATEDAT = "CreatedAt"

    def __str__(self) -> str:
        return str(self.value)
