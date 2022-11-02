from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.field_dto import FieldDto
from ..models.table_dto import TableDto
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateModelDto")


@attr.s(auto_attribs=True)
class CreateModelDto:
    """
    Attributes:
        name (str): The name of the model
        fields (Union[Unset, List[FieldDto]]): The text and checkbox fields for this document
        tables (Union[Unset, List[TableDto]]): The tables for this document
    """

    name: str
    fields: Union[Unset, List[FieldDto]] = UNSET
    tables: Union[Unset, List[TableDto]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        fields: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()

                fields.append(fields_item)

        tables: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tables, Unset):
            tables = []
            for tables_item_data in self.tables:
                tables_item = tables_item_data.to_dict()

                tables.append(tables_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if fields is not UNSET:
            field_dict["fields"] = fields
        if tables is not UNSET:
            field_dict["tables"] = tables

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = FieldDto.from_dict(fields_item_data)

            fields.append(fields_item)

        tables = []
        _tables = d.pop("tables", UNSET)
        for tables_item_data in _tables or []:
            tables_item = TableDto.from_dict(tables_item_data)

            tables.append(tables_item)

        create_model_dto = cls(
            name=name,
            fields=fields,
            tables=tables,
        )

        create_model_dto.additional_properties = d
        return create_model_dto

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
