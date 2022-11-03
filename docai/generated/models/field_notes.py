from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="FieldNotes")


@attr.s(auto_attribs=True)
class FieldNotes:
    """
    Attributes:
        field_id (str): The id of the field (table or form field) that these notes are for
        field_name (str): The name of the field (table or form field) that these notes are for
        notes (str): The notes for this field (table or form field)
    """

    field_id: str
    field_name: str
    notes: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_id = self.field_id
        field_name = self.field_name
        notes = self.notes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fieldId": field_id,
                "fieldName": field_name,
                "notes": notes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field_id = d.pop("fieldId")

        field_name = d.pop("fieldName")

        notes = d.pop("notes")

        field_notes = cls(
            field_id=field_id,
            field_name=field_name,
            notes=notes,
        )

        field_notes.additional_properties = d
        return field_notes

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
