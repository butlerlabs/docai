from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.block_result_dto import BlockResultDto
from ..models.bounding_box_dto import BoundingBoxDto
from ..models.model_field_type import ModelFieldType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SimpleFieldLabeledResultDto")


@attr.s(auto_attribs=True)
class SimpleFieldLabeledResultDto:
    """
    Attributes:
        id (str): The unique id of the field.
        name (str): The name of the field.
        type (ModelFieldType):
        blocks (List[BlockResultDto]): The blocks for this field.
        region (Union[Unset, BoundingBoxDto]):
    """

    id: str
    name: str
    type: ModelFieldType
    blocks: List[BlockResultDto]
    region: Union[Unset, BoundingBoxDto] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        type = self.type.value

        blocks = []
        for blocks_item_data in self.blocks:
            blocks_item = blocks_item_data.to_dict()

            blocks.append(blocks_item)

        region: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "type": type,
                "blocks": blocks,
            }
        )
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        type = ModelFieldType(d.pop("type"))

        blocks = []
        _blocks = d.pop("blocks")
        for blocks_item_data in _blocks:
            blocks_item = BlockResultDto.from_dict(blocks_item_data)

            blocks.append(blocks_item)

        _region = d.pop("region", UNSET)
        region: Union[Unset, BoundingBoxDto]
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = BoundingBoxDto.from_dict(_region)

        simple_field_labeled_result_dto = cls(
            id=id,
            name=name,
            type=type,
            blocks=blocks,
            region=region,
        )

        simple_field_labeled_result_dto.additional_properties = d
        return simple_field_labeled_result_dto

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
