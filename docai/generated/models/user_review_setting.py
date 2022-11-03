from enum import Enum


class UserReviewSetting(str, Enum):
    ALLDOCS = "AllDocs"
    LOWCONFIDENCEDOCS = "LowConfidenceDocs"
    NODOCS = "NoDocs"

    def __str__(self) -> str:
        return str(self.value)
