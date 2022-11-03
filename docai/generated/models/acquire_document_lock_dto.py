from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="AcquireDocumentLockDto")


@attr.s(auto_attribs=True)
class AcquireDocumentLockDto:
    """
    Attributes:
        document_id (str): The documentId of the document that has been locked. Undefined if there is not document to
            label.
    """

    document_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        document_id = self.document_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "documentId": document_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        document_id = d.pop("documentId")

        acquire_document_lock_dto = cls(
            document_id=document_id,
        )

        acquire_document_lock_dto.additional_properties = d
        return acquire_document_lock_dto

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
