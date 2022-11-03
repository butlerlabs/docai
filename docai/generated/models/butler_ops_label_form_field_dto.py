from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.extracted_field_labeling_results_dto import ExtractedFieldLabelingResultsDto
from ..types import UNSET, Unset

T = TypeVar("T", bound="ButlerOpsLabelFormFieldDto")


@attr.s(auto_attribs=True)
class ButlerOpsLabelFormFieldDto:
    """
    Attributes:
        key (ExtractedFieldLabelingResultsDto):
        value (ExtractedFieldLabelingResultsDto):
        is_unsure (Union[Unset, bool]): If the Butler Ops agent was unsure about this form field
        unsure_details (Union[Unset, str]): Details on why the Butler Ops agent was unsure about this form field
    """

    key: ExtractedFieldLabelingResultsDto
    value: ExtractedFieldLabelingResultsDto
    is_unsure: Union[Unset, bool] = UNSET
    unsure_details: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key.to_dict()

        value = self.value.to_dict()

        is_unsure = self.is_unsure
        unsure_details = self.unsure_details

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "value": value,
            }
        )
        if is_unsure is not UNSET:
            field_dict["isUnsure"] = is_unsure
        if unsure_details is not UNSET:
            field_dict["unsureDetails"] = unsure_details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key = ExtractedFieldLabelingResultsDto.from_dict(d.pop("key"))

        value = ExtractedFieldLabelingResultsDto.from_dict(d.pop("value"))

        is_unsure = d.pop("isUnsure", UNSET)

        unsure_details = d.pop("unsureDetails", UNSET)

        butler_ops_label_form_field_dto = cls(
            key=key,
            value=value,
            is_unsure=is_unsure,
            unsure_details=unsure_details,
        )

        butler_ops_label_form_field_dto.additional_properties = d
        return butler_ops_label_form_field_dto

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
