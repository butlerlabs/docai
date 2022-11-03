from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.training_document_status_dto import TrainingDocumentStatusDto

T = TypeVar("T", bound="TrainingDocumentStatusListDto")


@attr.s(auto_attribs=True)
class TrainingDocumentStatusListDto:
    """
    Attributes:
        items (List[TrainingDocumentStatusDto]): List of Training Document statuses
    """

    items: List[TrainingDocumentStatusDto]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()

            items.append(items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "items": items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = TrainingDocumentStatusDto.from_dict(items_item_data)

            items.append(items_item)

        training_document_status_list_dto = cls(
            items=items,
        )

        training_document_status_list_dto.additional_properties = d
        return training_document_status_list_dto

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
