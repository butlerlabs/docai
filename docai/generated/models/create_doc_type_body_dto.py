from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.form_field_update_dto import FormFieldUpdateDto
from ..models.table_update_dto import TableUpdateDto

T = TypeVar("T", bound="CreateDocTypeBodyDto")


@attr.s(auto_attribs=True)
class CreateDocTypeBodyDto:
    """
    Attributes:
        doc_type_name (str): A short name for this new doc type.
        description (str): A short blurb describing what kind of document this new doc type is for.
        form_fields (List[FormFieldUpdateDto]): The form fields section of the extraction config.
        tables (List[TableUpdateDto]): The tables section of the extraction config.
    """

    doc_type_name: str
    description: str
    form_fields: List[FormFieldUpdateDto]
    tables: List[TableUpdateDto]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        doc_type_name = self.doc_type_name
        description = self.description
        form_fields = []
        for form_fields_item_data in self.form_fields:
            form_fields_item = form_fields_item_data.to_dict()

            form_fields.append(form_fields_item)

        tables = []
        for tables_item_data in self.tables:
            tables_item = tables_item_data.to_dict()

            tables.append(tables_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "docTypeName": doc_type_name,
                "description": description,
                "formFields": form_fields,
                "tables": tables,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        doc_type_name = d.pop("docTypeName")

        description = d.pop("description")

        form_fields = []
        _form_fields = d.pop("formFields")
        for form_fields_item_data in _form_fields:
            form_fields_item = FormFieldUpdateDto.from_dict(form_fields_item_data)

            form_fields.append(form_fields_item)

        tables = []
        _tables = d.pop("tables")
        for tables_item_data in _tables:
            tables_item = TableUpdateDto.from_dict(tables_item_data)

            tables.append(tables_item)

        create_doc_type_body_dto = cls(
            doc_type_name=doc_type_name,
            description=description,
            form_fields=form_fields,
            tables=tables,
        )

        create_doc_type_body_dto.additional_properties = d
        return create_doc_type_body_dto

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
