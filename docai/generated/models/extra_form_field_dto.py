from typing import Any, Dict, List, Optional, Type, TypeVar

import attr

from ..models.extra_form_field_dto_key import ExtraFormFieldDtoKey
from ..models.extra_form_field_dto_value import ExtraFormFieldDtoValue

T = TypeVar("T", bound="ExtraFormFieldDto")


@attr.s(auto_attribs=True)
class ExtraFormFieldDto:
    """
    Attributes:
        key (Optional[ExtraFormFieldDtoKey]): This form-field's key. `null` if not found
        value (Optional[ExtraFormFieldDtoValue]): This form-field's value. `null` if not found
    """

    key: Optional[ExtraFormFieldDtoKey]
    value: Optional[ExtraFormFieldDtoValue]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key.to_dict() if self.key else None

        value = self.value.to_dict() if self.value else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _key = d.pop("key")
        key: Optional[ExtraFormFieldDtoKey]
        if _key is None:
            key = None
        else:
            key = ExtraFormFieldDtoKey.from_dict(_key)

        _value = d.pop("value")
        value: Optional[ExtraFormFieldDtoValue]
        if _value is None:
            value = None
        else:
            value = ExtraFormFieldDtoValue.from_dict(_value)

        extra_form_field_dto = cls(
            key=key,
            value=value,
        )

        extra_form_field_dto.additional_properties = d
        return extra_form_field_dto

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
