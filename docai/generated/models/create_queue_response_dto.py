from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CreateQueueResponseDto")


@attr.s(auto_attribs=True)
class CreateQueueResponseDto:
    """
    Attributes:
        queue_id (str): Id of the generated queue.
    """

    queue_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        queue_id = self.queue_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "queueId": queue_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        queue_id = d.pop("queueId")

        create_queue_response_dto = cls(
            queue_id=queue_id,
        )

        create_queue_response_dto.additional_properties = d
        return create_queue_response_dto

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
