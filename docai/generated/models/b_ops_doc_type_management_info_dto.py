from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.field_notes import FieldNotes

T = TypeVar("T", bound="BOpsDocTypeManagementInfoDto")


@attr.s(auto_attribs=True)
class BOpsDocTypeManagementInfoDto:
    """
    Attributes:
        sla (float): The SLA (in minutes) for this document type
        doc_type_notes_url (str): The URL to the detailed notes for this doc type
        form_field_notes (List[FieldNotes]): The notes for this document types form fields
        table_notes (List[FieldNotes]): The notes for this document types tables
    """

    sla: float
    doc_type_notes_url: str
    form_field_notes: List[FieldNotes]
    table_notes: List[FieldNotes]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sla = self.sla
        doc_type_notes_url = self.doc_type_notes_url
        form_field_notes = []
        for form_field_notes_item_data in self.form_field_notes:
            form_field_notes_item = form_field_notes_item_data.to_dict()

            form_field_notes.append(form_field_notes_item)

        table_notes = []
        for table_notes_item_data in self.table_notes:
            table_notes_item = table_notes_item_data.to_dict()

            table_notes.append(table_notes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sla": sla,
                "docTypeNotesUrl": doc_type_notes_url,
                "formFieldNotes": form_field_notes,
                "tableNotes": table_notes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sla = d.pop("sla")

        doc_type_notes_url = d.pop("docTypeNotesUrl")

        form_field_notes = []
        _form_field_notes = d.pop("formFieldNotes")
        for form_field_notes_item_data in _form_field_notes:
            form_field_notes_item = FieldNotes.from_dict(form_field_notes_item_data)

            form_field_notes.append(form_field_notes_item)

        table_notes = []
        _table_notes = d.pop("tableNotes")
        for table_notes_item_data in _table_notes:
            table_notes_item = FieldNotes.from_dict(table_notes_item_data)

            table_notes.append(table_notes_item)

        b_ops_doc_type_management_info_dto = cls(
            sla=sla,
            doc_type_notes_url=doc_type_notes_url,
            form_field_notes=form_field_notes,
            table_notes=table_notes,
        )

        b_ops_doc_type_management_info_dto.additional_properties = d
        return b_ops_doc_type_management_info_dto

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
