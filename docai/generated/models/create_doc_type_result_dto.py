from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CreateDocTypeResultDto")


@attr.s(auto_attribs=True)
class CreateDocTypeResultDto:
    """
    Attributes:
        doc_type_id (str): The ID of the newly created doc type.
        queue_id (str): The ID of the newly created queue.
    """

    doc_type_id: str
    queue_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        doc_type_id = self.doc_type_id
        queue_id = self.queue_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "docTypeId": doc_type_id,
                "queueId": queue_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        doc_type_id = d.pop("docTypeId")

        queue_id = d.pop("queueId")

        create_doc_type_result_dto = cls(
            doc_type_id=doc_type_id,
            queue_id=queue_id,
        )

        create_doc_type_result_dto.additional_properties = d
        return create_doc_type_result_dto

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
