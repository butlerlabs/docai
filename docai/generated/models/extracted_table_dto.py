from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.doc_ex_confidence import DocExConfidence
from ..models.extracted_table_row_dto import ExtractedTableRowDto

T = TypeVar("T", bound="ExtractedTableDto")


@attr.s(auto_attribs=True)
class ExtractedTableDto:
    """
    Attributes:
        table_name (str):
        rows (List[ExtractedTableRowDto]):
        confidence_score (DocExConfidence):
    """

    table_name: str
    rows: List[ExtractedTableRowDto]
    confidence_score: DocExConfidence
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        table_name = self.table_name
        rows = []
        for rows_item_data in self.rows:
            rows_item = rows_item_data.to_dict()

            rows.append(rows_item)

        confidence_score = self.confidence_score.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tableName": table_name,
                "rows": rows,
                "confidenceScore": confidence_score,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        table_name = d.pop("tableName")

        rows = []
        _rows = d.pop("rows")
        for rows_item_data in _rows:
            rows_item = ExtractedTableRowDto.from_dict(rows_item_data)

            rows.append(rows_item)

        confidence_score = DocExConfidence(d.pop("confidenceScore"))

        extracted_table_dto = cls(
            table_name=table_name,
            rows=rows,
            confidence_score=confidence_score,
        )

        extracted_table_dto.additional_properties = d
        return extracted_table_dto

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
