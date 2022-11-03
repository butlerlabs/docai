from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="ExampleFormFieldKeysAndValues")


@attr.s(auto_attribs=True)
class ExampleFormFieldKeysAndValues:
    """
    Attributes:
        values (List[str]): Previous example values for a specified Form Field
        keys (List[str]): Previous example keys for a specified Form Field
    """

    values: List[str]
    keys: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        values = self.values

        keys = self.keys

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "values": values,
                "keys": keys,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        values = cast(List[str], d.pop("values"))

        keys = cast(List[str], d.pop("keys"))

        example_form_field_keys_and_values = cls(
            values=values,
            keys=keys,
        )

        example_form_field_keys_and_values.additional_properties = d
        return example_form_field_keys_and_values

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
