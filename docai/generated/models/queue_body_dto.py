from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.queue_settings_create_dto import QueueSettingsCreateDto

T = TypeVar("T", bound="QueueBodyDto")


@attr.s(auto_attribs=True)
class QueueBodyDto:
    """
    Attributes:
        queue_name (str): Name of the queue to be created.
        doc_type_id (str): Id of the document type that the queue will process.
        settings (QueueSettingsCreateDto):
    """

    queue_name: str
    doc_type_id: str
    settings: QueueSettingsCreateDto
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        queue_name = self.queue_name
        doc_type_id = self.doc_type_id
        settings = self.settings.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "queueName": queue_name,
                "docTypeId": doc_type_id,
                "settings": settings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        queue_name = d.pop("queueName")

        doc_type_id = d.pop("docTypeId")

        settings = QueueSettingsCreateDto.from_dict(d.pop("settings"))

        queue_body_dto = cls(
            queue_name=queue_name,
            doc_type_id=doc_type_id,
            settings=settings,
        )

        queue_body_dto.additional_properties = d
        return queue_body_dto

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
