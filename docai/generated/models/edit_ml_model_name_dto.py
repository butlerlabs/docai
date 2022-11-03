from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="EditMlModelNameDto")


@attr.s(auto_attribs=True)
class EditMlModelNameDto:
    """
    Attributes:
        name (str): The new name for the ml model
    """

    name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        edit_ml_model_name_dto = cls(
            name=name,
        )

        edit_ml_model_name_dto.additional_properties = d
        return edit_ml_model_name_dto

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
