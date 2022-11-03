from enum import Enum


class QueueUploadSortBy(str, Enum):
    CREATEDAT = "CreatedAt"

    def __str__(self) -> str:
        return str(self.value)
