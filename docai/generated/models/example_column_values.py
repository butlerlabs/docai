from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="ExampleColumnValues")


@attr.s(auto_attribs=True)
class ExampleColumnValues:
    """
    Attributes:
        column_name (str): The name of the column these examples are for
        values (List[str]): The example values for this column
    """

    column_name: str
    values: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        column_name = self.column_name
        values = self.values

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "columnName": column_name,
                "values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        column_name = d.pop("columnName")

        values = cast(List[str], d.pop("values"))

        example_column_values = cls(
            column_name=column_name,
            values=values,
        )

        example_column_values.additional_properties = d
        return example_column_values

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
