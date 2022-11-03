from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.doc_ex_confidence import DocExConfidence
from ..models.example_column_values import ExampleColumnValues
from ..models.extracted_column_header_row_with_blocks_dto import ExtractedColumnHeaderRowWithBlocksDto
from ..models.extracted_table_row_with_blocks_dto import ExtractedTableRowWithBlocksDto

T = TypeVar("T", bound="EnhancedTableResultWithBlocksDto")


@attr.s(auto_attribs=True)
class EnhancedTableResultWithBlocksDto:
    """
    Attributes:
        id (str): Id of the extracted table
        name (str): Name of the extracted table
        column_headers (ExtractedColumnHeaderRowWithBlocksDto):
        rows (List[ExtractedTableRowWithBlocksDto]): List of extracted table rows with associated blocks
        confidence_score (DocExConfidence):
        examples (List[ExampleColumnValues]): Examples of previous values for each column for this Table
        notes (str): Free text notes associated with this Table
    """

    id: str
    name: str
    column_headers: ExtractedColumnHeaderRowWithBlocksDto
    rows: List[ExtractedTableRowWithBlocksDto]
    confidence_score: DocExConfidence
    examples: List[ExampleColumnValues]
    notes: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        column_headers = self.column_headers.to_dict()

        rows = []
        for rows_item_data in self.rows:
            rows_item = rows_item_data.to_dict()

            rows.append(rows_item)

        confidence_score = self.confidence_score.value

        examples = []
        for examples_item_data in self.examples:
            examples_item = examples_item_data.to_dict()

            examples.append(examples_item)

        notes = self.notes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "columnHeaders": column_headers,
                "rows": rows,
                "confidenceScore": confidence_score,
                "examples": examples,
                "notes": notes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        column_headers = ExtractedColumnHeaderRowWithBlocksDto.from_dict(d.pop("columnHeaders"))

        rows = []
        _rows = d.pop("rows")
        for rows_item_data in _rows:
            rows_item = ExtractedTableRowWithBlocksDto.from_dict(rows_item_data)

            rows.append(rows_item)

        confidence_score = DocExConfidence(d.pop("confidenceScore"))

        examples = []
        _examples = d.pop("examples")
        for examples_item_data in _examples:
            examples_item = ExampleColumnValues.from_dict(examples_item_data)

            examples.append(examples_item)

        notes = d.pop("notes")

        enhanced_table_result_with_blocks_dto = cls(
            id=id,
            name=name,
            column_headers=column_headers,
            rows=rows,
            confidence_score=confidence_score,
            examples=examples,
            notes=notes,
        )

        enhanced_table_result_with_blocks_dto.additional_properties = d
        return enhanced_table_result_with_blocks_dto

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
