from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.doc_ex_confidence import DocExConfidence

T = TypeVar("T", bound="ExtractedTableCellDto")


@attr.s(auto_attribs=True)
class ExtractedTableCellDto:
    """
    Attributes:
        column_name (str):
        value (str):
        confidence_score (DocExConfidence):
    """

    column_name: str
    value: str
    confidence_score: DocExConfidence
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        column_name = self.column_name
        value = self.value
        confidence_score = self.confidence_score.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "columnName": column_name,
                "value": value,
                "confidenceScore": confidence_score,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        column_name = d.pop("columnName")

        value = d.pop("value")

        confidence_score = DocExConfidence(d.pop("confidenceScore"))

        extracted_table_cell_dto = cls(
            column_name=column_name,
            value=value,
            confidence_score=confidence_score,
        )

        extracted_table_cell_dto.additional_properties = d
        return extracted_table_cell_dto

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
