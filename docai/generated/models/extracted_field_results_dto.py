from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.block_result_dto import BlockResultDto
from ..models.doc_ex_confidence import DocExConfidence
from ..models.doc_ex_field_type import DocExFieldType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExtractedFieldResultsDto")


@attr.s(auto_attribs=True)
class ExtractedFieldResultsDto:
    """
    Attributes:
        id (str): Id of the extracted field
        type (DocExFieldType):
        value (str): Extracted value associated with the field
        associated_blocks (List[BlockResultDto]): Blocks associated with the extracted field
        confidence_score (DocExConfidence):
        config_id (Union[Unset, str]): Id of the extracted field's config (form field config or column config)
    """

    id: str
    type: DocExFieldType
    value: str
    associated_blocks: List[BlockResultDto]
    confidence_score: DocExConfidence
    config_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type = self.type.value

        value = self.value
        associated_blocks = []
        for associated_blocks_item_data in self.associated_blocks:
            associated_blocks_item = associated_blocks_item_data.to_dict()

            associated_blocks.append(associated_blocks_item)

        confidence_score = self.confidence_score.value

        config_id = self.config_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type,
                "value": value,
                "associatedBlocks": associated_blocks,
                "confidenceScore": confidence_score,
            }
        )
        if config_id is not UNSET:
            field_dict["configId"] = config_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        type = DocExFieldType(d.pop("type"))

        value = d.pop("value")

        associated_blocks = []
        _associated_blocks = d.pop("associatedBlocks")
        for associated_blocks_item_data in _associated_blocks:
            associated_blocks_item = BlockResultDto.from_dict(associated_blocks_item_data)

            associated_blocks.append(associated_blocks_item)

        confidence_score = DocExConfidence(d.pop("confidenceScore"))

        config_id = d.pop("configId", UNSET)

        extracted_field_results_dto = cls(
            id=id,
            type=type,
            value=value,
            associated_blocks=associated_blocks,
            confidence_score=confidence_score,
            config_id=config_id,
        )

        extracted_field_results_dto.additional_properties = d
        return extracted_field_results_dto

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
