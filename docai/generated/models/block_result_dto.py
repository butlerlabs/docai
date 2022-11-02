from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.bounding_box_dto import BoundingBoxDto
from ..models.doc_ex_block_type import DocExBlockType

T = TypeVar("T", bound="BlockResultDto")


@attr.s(auto_attribs=True)
class BlockResultDto:
    """
    Attributes:
        id (str): ID of this block
        block_type (DocExBlockType):
        confidence (float): OCR confidence of this block
        text (str): Text within this block
        bounding_box (BoundingBoxDto):
    """

    id: str
    block_type: DocExBlockType
    confidence: float
    text: str
    bounding_box: BoundingBoxDto
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        block_type = self.block_type.value

        confidence = self.confidence
        text = self.text
        bounding_box = self.bounding_box.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "blockType": block_type,
                "confidence": confidence,
                "text": text,
                "boundingBox": bounding_box,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        block_type = DocExBlockType(d.pop("blockType"))

        confidence = d.pop("confidence")

        text = d.pop("text")

        bounding_box = BoundingBoxDto.from_dict(d.pop("boundingBox"))

        block_result_dto = cls(
            id=id,
            block_type=block_type,
            confidence=confidence,
            text=text,
            bounding_box=bounding_box,
        )

        block_result_dto.additional_properties = d
        return block_result_dto

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
