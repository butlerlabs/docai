from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.column_field_update_dto import ColumnFieldUpdateDto

T = TypeVar("T", bound="TableUpdateDto")


@attr.s(auto_attribs=True)
class TableUpdateDto:
    """
    Attributes:
        name (str): Document table display name
        columns (List[ColumnFieldUpdateDto]):
    """

    name: str
    columns: List[ColumnFieldUpdateDto]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        columns = []
        for columns_item_data in self.columns:
            columns_item = columns_item_data.to_dict()

            columns.append(columns_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "columns": columns,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        columns = []
        _columns = d.pop("columns")
        for columns_item_data in _columns:
            columns_item = ColumnFieldUpdateDto.from_dict(columns_item_data)

            columns.append(columns_item)

        table_update_dto = cls(
            name=name,
            columns=columns,
        )

        table_update_dto.additional_properties = d
        return table_update_dto

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
