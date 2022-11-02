from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.model_column_dto import ModelColumnDto
from ..models.model_field_type import ModelFieldType

T = TypeVar("T", bound="ModelTableDto")


@attr.s(auto_attribs=True)
class ModelTableDto:
    """
    Attributes:
        type (ModelFieldType):
        name (str): The name for the new field
        id (str): The unique id of this table.
        columns (List[ModelColumnDto]): The columns fields for this table
    """

    type: ModelFieldType
    name: str
    id: str
    columns: List[ModelColumnDto]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        name = self.name
        id = self.id
        columns = []
        for columns_item_data in self.columns:
            columns_item = columns_item_data.to_dict()

            columns.append(columns_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "name": name,
                "id": id,
                "columns": columns,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = ModelFieldType(d.pop("type"))

        name = d.pop("name")

        id = d.pop("id")

        columns = []
        _columns = d.pop("columns")
        for columns_item_data in _columns:
            columns_item = ModelColumnDto.from_dict(columns_item_data)

            columns.append(columns_item)

        model_table_dto = cls(
            type=type,
            name=name,
            id=id,
            columns=columns,
        )

        model_table_dto.additional_properties = d
        return model_table_dto

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
