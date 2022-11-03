from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.reviewer_dto import ReviewerDto

T = TypeVar("T", bound="ReviewerListDto")


@attr.s(auto_attribs=True)
class ReviewerListDto:
    """
    Attributes:
        items (List[ReviewerDto]): List of reviewers
    """

    items: List[ReviewerDto]
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
            items_item = ReviewerDto.from_dict(items_item_data)

            items.append(items_item)

        reviewer_list_dto = cls(
            items=items,
        )

        reviewer_list_dto.additional_properties = d
        return reviewer_list_dto

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
