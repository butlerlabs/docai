from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="BoundingBoxDto")


@attr.s(auto_attribs=True)
class BoundingBoxDto:
    """
    Attributes:
        width (float): Relative width of this bounding box to page width
        height (float): Relative height of this bounding box to page height
        left (float): Relative position of leftmost point of this bounding box on the page
        top (float): Relative position of uppermost point of this bounding box on the page
        page (float): Page number
    """

    width: float
    height: float
    left: float
    top: float
    page: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        width = self.width
        height = self.height
        left = self.left
        top = self.top
        page = self.page

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "width": width,
                "height": height,
                "left": left,
                "top": top,
                "page": page,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        width = d.pop("width")

        height = d.pop("height")

        left = d.pop("left")

        top = d.pop("top")

        page = d.pop("page")

        bounding_box_dto = cls(
            width=width,
            height=height,
            left=left,
            top=top,
            page=page,
        )

        bounding_box_dto.additional_properties = d
        return bounding_box_dto

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
