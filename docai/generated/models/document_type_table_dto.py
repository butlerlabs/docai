from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.document_type_field_dto import DocumentTypeFieldDto

T = TypeVar("T", bound="DocumentTypeTableDto")


@attr.s(auto_attribs=True)
class DocumentTypeTableDto:
    """
    Attributes:
        id (str): Table ID
        name (str): Table display name
        columns (List[DocumentTypeFieldDto]): Table columns
    """

    id: str
    name: str
    columns: List[DocumentTypeFieldDto]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        columns = []
        for columns_item_data in self.columns:
            columns_item = columns_item_data.to_dict()

            columns.append(columns_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "columns": columns,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        columns = []
        _columns = d.pop("columns")
        for columns_item_data in _columns:
            columns_item = DocumentTypeFieldDto.from_dict(columns_item_data)

            columns.append(columns_item)

        document_type_table_dto = cls(
            id=id,
            name=name,
            columns=columns,
        )

        document_type_table_dto.additional_properties = d
        return document_type_table_dto

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
