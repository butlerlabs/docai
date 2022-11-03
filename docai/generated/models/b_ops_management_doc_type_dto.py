from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="BOpsManagementDocTypeDto")


@attr.s(auto_attribs=True)
class BOpsManagementDocTypeDto:
    """
    Attributes:
        id (str): The id of the document type
        name (str): The name of the document type
        org_name (str): The name of the organization this document type belongs to
        sla (float): The SLA (in minutes) for this document type
        has_notes (bool): Whether or not this doc type has notes saved
    """

    id: str
    name: str
    org_name: str
    sla: float
    has_notes: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        org_name = self.org_name
        sla = self.sla
        has_notes = self.has_notes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "orgName": org_name,
                "sla": sla,
                "hasNotes": has_notes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        org_name = d.pop("orgName")

        sla = d.pop("sla")

        has_notes = d.pop("hasNotes")

        b_ops_management_doc_type_dto = cls(
            id=id,
            name=name,
            org_name=org_name,
            sla=sla,
            has_notes=has_notes,
        )

        b_ops_management_doc_type_dto.additional_properties = d
        return b_ops_management_doc_type_dto

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
