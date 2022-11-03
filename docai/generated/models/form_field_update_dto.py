from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.entity_type import EntityType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FormFieldUpdateDto")


@attr.s(auto_attribs=True)
class FormFieldUpdateDto:
    """
    Attributes:
        name (str): Document field display name, e.g., "Purchase Order Number"
        type (Union[Unset, EntityType]):
    """

    name: str
    type: Union[Unset, EntityType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        _type = d.pop("type", UNSET)
        type: Union[Unset, EntityType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = EntityType(_type)

        form_field_update_dto = cls(
            name=name,
            type=type,
        )

        form_field_update_dto.additional_properties = d
        return form_field_update_dto

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
