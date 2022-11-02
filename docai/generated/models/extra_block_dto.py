from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.bounding_box_dto import BoundingBoxDto

T = TypeVar("T", bound="ExtraBlockDto")


@attr.s(auto_attribs=True)
class ExtraBlockDto:
    """
    Attributes:
        text (str): The text of this block
        bounding_box (BoundingBoxDto):
    """

    text: str
    bounding_box: BoundingBoxDto
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        text = self.text
        bounding_box = self.bounding_box.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
                "boundingBox": bounding_box,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        text = d.pop("text")

        bounding_box = BoundingBoxDto.from_dict(d.pop("boundingBox"))

        extra_block_dto = cls(
            text=text,
            bounding_box=bounding_box,
        )

        extra_block_dto.additional_properties = d
        return extra_block_dto

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
