from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.block_type import BlockType
from ..models.bounding_box_dto import BoundingBoxDto

T = TypeVar("T", bound="BlockDto")


@attr.s(auto_attribs=True)
class BlockDto:
    """
    Attributes:
        id (str): ID of this block
        block_type (BlockType):
        text (str): Text within this block
        bounding_box (BoundingBoxDto):
    """

    id: str
    block_type: BlockType
    text: str
    bounding_box: BoundingBoxDto
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        block_type = self.block_type.value

        text = self.text
        bounding_box = self.bounding_box.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "blockType": block_type,
                "text": text,
                "boundingBox": bounding_box,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        block_type = BlockType(d.pop("blockType"))

        text = d.pop("text")

        bounding_box = BoundingBoxDto.from_dict(d.pop("boundingBox"))

        block_dto = cls(
            id=id,
            block_type=block_type,
            text=text,
            bounding_box=bounding_box,
        )

        block_dto.additional_properties = d
        return block_dto

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
