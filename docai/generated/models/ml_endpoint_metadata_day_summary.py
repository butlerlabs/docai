from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="MlEndpointMetadataDaySummary")


@attr.s(auto_attribs=True)
class MlEndpointMetadataDaySummary:
    """
    Attributes:
        num_docs_processed (float): How many documents were processed this day.
        days_ago (float): How many days ago this summary refers to. Times are calculated in UTC.
    """

    num_docs_processed: float
    days_ago: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        num_docs_processed = self.num_docs_processed
        days_ago = self.days_ago

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "numDocsProcessed": num_docs_processed,
                "daysAgo": days_ago,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        num_docs_processed = d.pop("numDocsProcessed")

        days_ago = d.pop("daysAgo")

        ml_endpoint_metadata_day_summary = cls(
            num_docs_processed=num_docs_processed,
            days_ago=days_ago,
        )

        ml_endpoint_metadata_day_summary.additional_properties = d
        return ml_endpoint_metadata_day_summary

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
