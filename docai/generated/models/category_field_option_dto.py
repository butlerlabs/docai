from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CategoryFieldOptionDto")


@attr.s(auto_attribs=True)
class CategoryFieldOptionDto:
    """
    Attributes:
        display_value (str): The display value for this category field
        value (str): The selected value for this category field
    """

    display_value: str
    value: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_value = self.display_value
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "displayValue": display_value,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        display_value = d.pop("displayValue")

        value = d.pop("value")

        category_field_option_dto = cls(
            display_value=display_value,
            value=value,
        )

        category_field_option_dto.additional_properties = d
        return category_field_option_dto

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
