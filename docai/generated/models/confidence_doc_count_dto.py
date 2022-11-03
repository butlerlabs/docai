from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ConfidenceDocCountDto")


@attr.s(auto_attribs=True)
class ConfidenceDocCountDto:
    """
    Attributes:
        high (float): Number of documents with high confidence
        low (float): Number of documents with low confidence
        user_reviewed (float): Number of documents with user reviewed confidence
    """

    high: float
    low: float
    user_reviewed: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        high = self.high
        low = self.low
        user_reviewed = self.user_reviewed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "high": high,
                "low": low,
                "userReviewed": user_reviewed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        high = d.pop("high")

        low = d.pop("low")

        user_reviewed = d.pop("userReviewed")

        confidence_doc_count_dto = cls(
            high=high,
            low=low,
            user_reviewed=user_reviewed,
        )

        confidence_doc_count_dto.additional_properties = d
        return confidence_doc_count_dto

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
