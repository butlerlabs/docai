from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.bounding_box_dto import BoundingBoxDto
from ..models.doc_ex_confidence import DocExConfidence
from ..models.model_field_type import ModelFieldType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SignatureFieldWithConfidenceLabeledResultDto")


@attr.s(auto_attribs=True)
class SignatureFieldWithConfidenceLabeledResultDto:
    """
    Attributes:
        id (str): The unique id of the signature field.
        name (str): The name of the signature field.
        type (ModelFieldType):
        confidence_score (DocExConfidence):
        region (Union[Unset, BoundingBoxDto]):
        value (Union[Unset, str]): The text value for this field.
    """

    id: str
    name: str
    type: ModelFieldType
    confidence_score: DocExConfidence
    region: Union[Unset, BoundingBoxDto] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        type = self.type.value

        confidence_score = self.confidence_score.value

        region: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.to_dict()

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "type": type,
                "confidenceScore": confidence_score,
            }
        )
        if region is not UNSET:
            field_dict["region"] = region
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        type = ModelFieldType(d.pop("type"))

        confidence_score = DocExConfidence(d.pop("confidenceScore"))

        _region = d.pop("region", UNSET)
        region: Union[Unset, BoundingBoxDto]
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = BoundingBoxDto.from_dict(_region)

        value = d.pop("value", UNSET)

        signature_field_with_confidence_labeled_result_dto = cls(
            id=id,
            name=name,
            type=type,
            confidence_score=confidence_score,
            region=region,
            value=value,
        )

        signature_field_with_confidence_labeled_result_dto.additional_properties = d
        return signature_field_with_confidence_labeled_result_dto

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
