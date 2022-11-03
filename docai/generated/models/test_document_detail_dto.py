from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.test_document_status import TestDocumentStatus

T = TypeVar("T", bound="TestDocumentDetailDto")


@attr.s(auto_attribs=True)
class TestDocumentDetailDto:
    """
    Attributes:
        id (str): The id of the Test Document
        file_name (str): The file name of the Test Document
        upload_time (float): The unix timestamp for when the Test Document was uploaded
        status (TestDocumentStatus):
    """

    id: str
    file_name: str
    upload_time: float
    status: TestDocumentStatus
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        file_name = self.file_name
        upload_time = self.upload_time
        status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "fileName": file_name,
                "uploadTime": upload_time,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        file_name = d.pop("fileName")

        upload_time = d.pop("uploadTime")

        status = TestDocumentStatus(d.pop("status"))

        test_document_detail_dto = cls(
            id=id,
            file_name=file_name,
            upload_time=upload_time,
            status=status,
        )

        test_document_detail_dto.additional_properties = d
        return test_document_detail_dto

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
