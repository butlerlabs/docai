from enum import Enum


class EnhancedExtractionResultsFieldStatus(str, Enum):
    ALL = "All"
    NEEDSREVIEW = "NeedsReview"

    def __str__(self) -> str:
        return str(self.value)
