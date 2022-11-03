from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.block_result_dto import BlockResultDto

T = TypeVar("T", bound="FieldResultDto")


@attr.s(auto_attribs=True)
class FieldResultDto:
    """
    Attributes:
        associated_blocks (List[BlockResultDto]): Blocks associated with this field
        value (str): Text override value of this field. If non-empty, takes precedence over blocks
        deleted (bool): Is field deleted by user/reviewer
    """

    associated_blocks: List[BlockResultDto]
    value: str
    deleted: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        associated_blocks = []
        for associated_blocks_item_data in self.associated_blocks:
            associated_blocks_item = associated_blocks_item_data.to_dict()

            associated_blocks.append(associated_blocks_item)

        value = self.value
        deleted = self.deleted

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "associatedBlocks": associated_blocks,
                "value": value,
                "deleted": deleted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        associated_blocks = []
        _associated_blocks = d.pop("associatedBlocks")
        for associated_blocks_item_data in _associated_blocks:
            associated_blocks_item = BlockResultDto.from_dict(associated_blocks_item_data)

            associated_blocks.append(associated_blocks_item)

        value = d.pop("value")

        deleted = d.pop("deleted")

        field_result_dto = cls(
            associated_blocks=associated_blocks,
            value=value,
            deleted=deleted,
        )

        field_result_dto.additional_properties = d
        return field_result_dto

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
