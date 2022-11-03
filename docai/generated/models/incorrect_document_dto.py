from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.incorrect_status import IncorrectStatus

T = TypeVar("T", bound="IncorrectDocumentDto")


@attr.s(auto_attribs=True)
class IncorrectDocumentDto:
    """
    Attributes:
        id (str): ID of this incorrect document
        file_name (str): File name of this incorrect document
        doc_type_id (str): Document type ID of this incorrect document
        doc_type_name (str): Document type name of this incorrect document
        reviewer_user_id (str): User ID of the reviewer responsible for this incorrect document
        reviewer_email (str): Email of the reviewer responsible for this incorrect document
        status (IncorrectStatus):
        field_accuracy (float): Field accuracy of this incorrect document
        review_time (float): Unix timestamp of when this incorrect document was reviewed
    """

    id: str
    file_name: str
    doc_type_id: str
    doc_type_name: str
    reviewer_user_id: str
    reviewer_email: str
    status: IncorrectStatus
    field_accuracy: float
    review_time: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        file_name = self.file_name
        doc_type_id = self.doc_type_id
        doc_type_name = self.doc_type_name
        reviewer_user_id = self.reviewer_user_id
        reviewer_email = self.reviewer_email
        status = self.status.value

        field_accuracy = self.field_accuracy
        review_time = self.review_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "fileName": file_name,
                "docTypeId": doc_type_id,
                "docTypeName": doc_type_name,
                "reviewerUserId": reviewer_user_id,
                "reviewerEmail": reviewer_email,
                "status": status,
                "fieldAccuracy": field_accuracy,
                "reviewTime": review_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        file_name = d.pop("fileName")

        doc_type_id = d.pop("docTypeId")

        doc_type_name = d.pop("docTypeName")

        reviewer_user_id = d.pop("reviewerUserId")

        reviewer_email = d.pop("reviewerEmail")

        status = IncorrectStatus(d.pop("status"))

        field_accuracy = d.pop("fieldAccuracy")

        review_time = d.pop("reviewTime")

        incorrect_document_dto = cls(
            id=id,
            file_name=file_name,
            doc_type_id=doc_type_id,
            doc_type_name=doc_type_name,
            reviewer_user_id=reviewer_user_id,
            reviewer_email=reviewer_email,
            status=status,
            field_accuracy=field_accuracy,
            review_time=review_time,
        )

        incorrect_document_dto.additional_properties = d
        return incorrect_document_dto

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
