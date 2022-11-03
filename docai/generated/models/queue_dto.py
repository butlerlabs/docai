from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.base_model_type import BaseModelType

T = TypeVar("T", bound="QueueDto")


@attr.s(auto_attribs=True)
class QueueDto:
    """
    Attributes:
        queue_id (str): The ID of the Queue.
        queue_name (str): The name of the Queue.
        doc_type_id (str): The ID of the document type associated with this Queue.
        doc_type_name (str): The name of the document type associated with this Queue.
        docs_processed (float): Total number of documents processed by this Queue.
        model_type (BaseModelType):
    """

    queue_id: str
    queue_name: str
    doc_type_id: str
    doc_type_name: str
    docs_processed: float
    model_type: BaseModelType
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        queue_id = self.queue_id
        queue_name = self.queue_name
        doc_type_id = self.doc_type_id
        doc_type_name = self.doc_type_name
        docs_processed = self.docs_processed
        model_type = self.model_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "queueId": queue_id,
                "queueName": queue_name,
                "docTypeId": doc_type_id,
                "docTypeName": doc_type_name,
                "docsProcessed": docs_processed,
                "modelType": model_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        queue_id = d.pop("queueId")

        queue_name = d.pop("queueName")

        doc_type_id = d.pop("docTypeId")

        doc_type_name = d.pop("docTypeName")

        docs_processed = d.pop("docsProcessed")

        model_type = BaseModelType(d.pop("modelType"))

        queue_dto = cls(
            queue_id=queue_id,
            queue_name=queue_name,
            doc_type_id=doc_type_id,
            doc_type_name=doc_type_name,
            docs_processed=docs_processed,
            model_type=model_type,
        )

        queue_dto.additional_properties = d
        return queue_dto

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
