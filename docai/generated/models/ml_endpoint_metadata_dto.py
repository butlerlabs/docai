from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.ml_endpoint_metadata_day_summary import MlEndpointMetadataDaySummary

T = TypeVar("T", bound="MlEndpointMetadataDto")


@attr.s(auto_attribs=True)
class MlEndpointMetadataDto:
    """
    Attributes:
        total_docs_processed (float): The total number of documents processed in the last 30 days.
        daily_statistics (List[MlEndpointMetadataDaySummary]): A sparse array of daily summaries. Contains statistics
            from up to 30 days ago.
    """

    total_docs_processed: float
    daily_statistics: List[MlEndpointMetadataDaySummary]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_docs_processed = self.total_docs_processed
        daily_statistics = []
        for daily_statistics_item_data in self.daily_statistics:
            daily_statistics_item = daily_statistics_item_data.to_dict()

            daily_statistics.append(daily_statistics_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalDocsProcessed": total_docs_processed,
                "dailyStatistics": daily_statistics,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_docs_processed = d.pop("totalDocsProcessed")

        daily_statistics = []
        _daily_statistics = d.pop("dailyStatistics")
        for daily_statistics_item_data in _daily_statistics:
            daily_statistics_item = MlEndpointMetadataDaySummary.from_dict(daily_statistics_item_data)

            daily_statistics.append(daily_statistics_item)

        ml_endpoint_metadata_dto = cls(
            total_docs_processed=total_docs_processed,
            daily_statistics=daily_statistics,
        )

        ml_endpoint_metadata_dto.additional_properties = d
        return ml_endpoint_metadata_dto

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
