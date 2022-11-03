from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.queue_upload_status import QueueUploadStatus

T = TypeVar("T", bound="QueueUploadStatusDto")


@attr.s(auto_attribs=True)
class QueueUploadStatusDto:
    """
    Attributes:
        status (QueueUploadStatus):
    """

    status: QueueUploadStatus
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = QueueUploadStatus(d.pop("status"))

        queue_upload_status_dto = cls(
            status=status,
        )

        queue_upload_status_dto.additional_properties = d
        return queue_upload_status_dto

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
