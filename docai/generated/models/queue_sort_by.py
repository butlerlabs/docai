from enum import Enum


class QueueSortBy(str, Enum):
    QUEUENAME = "QueueName"

    def __str__(self) -> str:
        return str(self.value)
