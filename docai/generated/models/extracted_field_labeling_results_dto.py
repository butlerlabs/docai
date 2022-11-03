from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.block_result_dto import BlockResultDto
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExtractedFieldLabelingResultsDto")


@attr.s(auto_attribs=True)
class ExtractedFieldLabelingResultsDto:
    """
    Attributes:
        id (str): Id of the extracted field to label
        value (str): Value to label for the field
        associated_blocks (List[BlockResultDto]): Blocks to label for the field
        config_id (Union[Unset, str]): Id of the extracted field's config (form field config or column config)
    """

    id: str
    value: str
    associated_blocks: List[BlockResultDto]
    config_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        value = self.value
        associated_blocks = []
        for associated_blocks_item_data in self.associated_blocks:
            associated_blocks_item = associated_blocks_item_data.to_dict()

            associated_blocks.append(associated_blocks_item)

        config_id = self.config_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "value": value,
                "associatedBlocks": associated_blocks,
            }
        )
        if config_id is not UNSET:
            field_dict["configId"] = config_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        value = d.pop("value")

        associated_blocks = []
        _associated_blocks = d.pop("associatedBlocks")
        for associated_blocks_item_data in _associated_blocks:
            associated_blocks_item = BlockResultDto.from_dict(associated_blocks_item_data)

            associated_blocks.append(associated_blocks_item)

        config_id = d.pop("configId", UNSET)

        extracted_field_labeling_results_dto = cls(
            id=id,
            value=value,
            associated_blocks=associated_blocks,
            config_id=config_id,
        )

        extracted_field_labeling_results_dto.additional_properties = d
        return extracted_field_labeling_results_dto

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
