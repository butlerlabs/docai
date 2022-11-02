from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.model_field_type import ModelFieldType

T = TypeVar("T", bound="ModelFieldDto")


@attr.s(auto_attribs=True)
class ModelFieldDto:
    """
    Attributes:
        type (ModelFieldType):
        name (str): The name for the new field
        id (str): The unique id of this field.
    """

    type: ModelFieldType
    name: str
    id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        name = self.name
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "name": name,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = ModelFieldType(d.pop("type"))

        name = d.pop("name")

        id = d.pop("id")

        model_field_dto = cls(
            type=type,
            name=name,
            id=id,
        )

        model_field_dto.additional_properties = d
        return model_field_dto

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
