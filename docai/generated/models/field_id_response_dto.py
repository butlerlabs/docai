from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="FieldIdResponseDto")


@attr.s(auto_attribs=True)
class FieldIdResponseDto:
    """
    Attributes:
        field_id (str): The id of the field.
    """

    field_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_id = self.field_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fieldId": field_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field_id = d.pop("fieldId")

        field_id_response_dto = cls(
            field_id=field_id,
        )

        field_id_response_dto.additional_properties = d
        return field_id_response_dto

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
