from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.entity_type import EntityType
from ..models.extracted_field_results_dto import ExtractedFieldResultsDto

T = TypeVar("T", bound="ExtractedColumnHeaderWithBlocksDto")


@attr.s(auto_attribs=True)
class ExtractedColumnHeaderWithBlocksDto:
    """
    Attributes:
        id (str): Id of the extracted column header
        column_type (EntityType):
        column_name (str): Name of the column
        label_field (ExtractedFieldResultsDto):
    """

    id: str
    column_type: EntityType
    column_name: str
    label_field: ExtractedFieldResultsDto
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        column_type = self.column_type.value

        column_name = self.column_name
        label_field = self.label_field.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "columnType": column_type,
                "columnName": column_name,
                "labelField": label_field,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        column_type = EntityType(d.pop("columnType"))

        column_name = d.pop("columnName")

        label_field = ExtractedFieldResultsDto.from_dict(d.pop("labelField"))

        extracted_column_header_with_blocks_dto = cls(
            id=id,
            column_type=column_type,
            column_name=column_name,
            label_field=label_field,
        )

        extracted_column_header_with_blocks_dto.additional_properties = d
        return extracted_column_header_with_blocks_dto

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
