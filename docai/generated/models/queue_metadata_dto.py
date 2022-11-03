from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.queue_metadata_day_summary import QueueMetadataDaySummary

T = TypeVar("T", bound="QueueMetadataDto")


@attr.s(auto_attribs=True)
class QueueMetadataDto:
    """
    Attributes:
        total_docs_processed (float): The total number of documents processed in the last 30 days.
        total_low_confidence_docs (float): The total number of low confidence documents in the last 30 days.
        total_high_confidence_docs (float): The total number of high confidence documents in the last 30 days.
        total_user_reviewed_docs (float): The total number of documents reviewed by you or teammates in the last 30
            days.
        daily_statistics (List[QueueMetadataDaySummary]): A sparse array of daily summaries. Contains statistics from up
            to 30 days ago.
    """

    total_docs_processed: float
    total_low_confidence_docs: float
    total_high_confidence_docs: float
    total_user_reviewed_docs: float
    daily_statistics: List[QueueMetadataDaySummary]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_docs_processed = self.total_docs_processed
        total_low_confidence_docs = self.total_low_confidence_docs
        total_high_confidence_docs = self.total_high_confidence_docs
        total_user_reviewed_docs = self.total_user_reviewed_docs
        daily_statistics = []
        for daily_statistics_item_data in self.daily_statistics:
            daily_statistics_item = daily_statistics_item_data.to_dict()

            daily_statistics.append(daily_statistics_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalDocsProcessed": total_docs_processed,
                "totalLowConfidenceDocs": total_low_confidence_docs,
                "totalHighConfidenceDocs": total_high_confidence_docs,
                "totalUserReviewedDocs": total_user_reviewed_docs,
                "dailyStatistics": daily_statistics,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_docs_processed = d.pop("totalDocsProcessed")

        total_low_confidence_docs = d.pop("totalLowConfidenceDocs")

        total_high_confidence_docs = d.pop("totalHighConfidenceDocs")

        total_user_reviewed_docs = d.pop("totalUserReviewedDocs")

        daily_statistics = []
        _daily_statistics = d.pop("dailyStatistics")
        for daily_statistics_item_data in _daily_statistics:
            daily_statistics_item = QueueMetadataDaySummary.from_dict(daily_statistics_item_data)

            daily_statistics.append(daily_statistics_item)

        queue_metadata_dto = cls(
            total_docs_processed=total_docs_processed,
            total_low_confidence_docs=total_low_confidence_docs,
            total_high_confidence_docs=total_high_confidence_docs,
            total_user_reviewed_docs=total_user_reviewed_docs,
            daily_statistics=daily_statistics,
        )

        queue_metadata_dto.additional_properties = d
        return queue_metadata_dto

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
