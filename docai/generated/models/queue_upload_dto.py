from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.queue_upload_status import QueueUploadStatus

T = TypeVar("T", bound="QueueUploadDto")


@attr.s(auto_attribs=True)
class QueueUploadDto:
    """
    Attributes:
        upload_id (str): ID of the upload
        status (QueueUploadStatus):
        uploaded_by (str): Email of the user who uploaded the upload
        num_documents (float): Number of documents in the upload
        created_at_time (float): Unix timestamp of when this upload was created
    """

    upload_id: str
    status: QueueUploadStatus
    uploaded_by: str
    num_documents: float
    created_at_time: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        upload_id = self.upload_id
        status = self.status.value

        uploaded_by = self.uploaded_by
        num_documents = self.num_documents
        created_at_time = self.created_at_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uploadId": upload_id,
                "status": status,
                "uploadedBy": uploaded_by,
                "numDocuments": num_documents,
                "createdAtTime": created_at_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        upload_id = d.pop("uploadId")

        status = QueueUploadStatus(d.pop("status"))

        uploaded_by = d.pop("uploadedBy")

        num_documents = d.pop("numDocuments")

        created_at_time = d.pop("createdAtTime")

        queue_upload_dto = cls(
            upload_id=upload_id,
            status=status,
            uploaded_by=uploaded_by,
            num_documents=num_documents,
            created_at_time=created_at_time,
        )

        queue_upload_dto.additional_properties = d
        return queue_upload_dto

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
