from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.confidence_doc_count_dto import ConfidenceDocCountDto
from ..types import UNSET, Unset

T = TypeVar("T", bound="QueueUploadDocInfoDto")


@attr.s(auto_attribs=True)
class QueueUploadDocInfoDto:
    """
    Attributes:
        confidence_doc_count (ConfidenceDocCountDto):
        next_doc_to_review (Union[Unset, str]): ID of next document that needs user review, if one exists
    """

    confidence_doc_count: ConfidenceDocCountDto
    next_doc_to_review: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        confidence_doc_count = self.confidence_doc_count.to_dict()

        next_doc_to_review = self.next_doc_to_review

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "confidenceDocCount": confidence_doc_count,
            }
        )
        if next_doc_to_review is not UNSET:
            field_dict["nextDocToReview"] = next_doc_to_review

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        confidence_doc_count = ConfidenceDocCountDto.from_dict(d.pop("confidenceDocCount"))

        next_doc_to_review = d.pop("nextDocToReview", UNSET)

        queue_upload_doc_info_dto = cls(
            confidence_doc_count=confidence_doc_count,
            next_doc_to_review=next_doc_to_review,
        )

        queue_upload_doc_info_dto.additional_properties = d
        return queue_upload_doc_info_dto

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
