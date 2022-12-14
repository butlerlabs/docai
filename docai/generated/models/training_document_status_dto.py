from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.document_status import DocumentStatus

T = TypeVar("T", bound="TrainingDocumentStatusDto")


@attr.s(auto_attribs=True)
class TrainingDocumentStatusDto:
    """
    Attributes:
        id (str): The ID of the training document.
        status (DocumentStatus):
    """

    id: str
    status: DocumentStatus
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        status = DocumentStatus(d.pop("status"))

        training_document_status_dto = cls(
            id=id,
            status=status,
        )

        training_document_status_dto.additional_properties = d
        return training_document_status_dto

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
