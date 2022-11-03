from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PageRangeDto")


@attr.s(auto_attribs=True)
class PageRangeDto:
    """
    Attributes:
        start_page (float): Page number to start on, inclusive
        end_page (float): Page number to end on, inclusive
    """

    start_page: float
    end_page: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start_page = self.start_page
        end_page = self.end_page

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "startPage": start_page,
                "endPage": end_page,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        start_page = d.pop("startPage")

        end_page = d.pop("endPage")

        page_range_dto = cls(
            start_page=start_page,
            end_page=end_page,
        )

        page_range_dto.additional_properties = d
        return page_range_dto

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
