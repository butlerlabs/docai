from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.library_model_dto import LibraryModelDto

T = TypeVar("T", bound="PaginatedLibraryModelDto")


@attr.s(auto_attribs=True)
class PaginatedLibraryModelDto:
    """
    Attributes:
        has_next (bool): Whether there are more pages to fetch after this page.
        has_previous (bool): Whether there are more pages to fetch before this page.
        total_count (float): Total number of items across all pages.
        items (List[LibraryModelDto]): List of library models.
    """

    has_next: bool
    has_previous: bool
    total_count: float
    items: List[LibraryModelDto]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        has_next = self.has_next
        has_previous = self.has_previous
        total_count = self.total_count
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()

            items.append(items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hasNext": has_next,
                "hasPrevious": has_previous,
                "totalCount": total_count,
                "items": items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        has_next = d.pop("hasNext")

        has_previous = d.pop("hasPrevious")

        total_count = d.pop("totalCount")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = LibraryModelDto.from_dict(items_item_data)

            items.append(items_item)

        paginated_library_model_dto = cls(
            has_next=has_next,
            has_previous=has_previous,
            total_count=total_count,
            items=items,
        )

        paginated_library_model_dto.additional_properties = d
        return paginated_library_model_dto

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
