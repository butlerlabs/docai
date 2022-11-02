from enum import Enum


class DocExConfidence(str, Enum):
    HIGH = "High"
    LOW = "Low"
    USERREVIEWED = "UserReviewed"

    def __str__(self) -> str:
        return str(self.value)
