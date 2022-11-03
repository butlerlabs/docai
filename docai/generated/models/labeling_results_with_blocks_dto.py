from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.deprecated_extracted_table_with_blocks_dto import DeprecatedExtractedTableWithBlocksDto
from ..models.extracted_form_fields_with_blocks_dto import ExtractedFormFieldsWithBlocksDto
from ..types import UNSET, Unset

T = TypeVar("T", bound="LabelingResultsWithBlocksDto")


@attr.s(auto_attribs=True)
class LabelingResultsWithBlocksDto:
    """
    Attributes:
        id (str): Id of the extracted document
        form_fields (List[ExtractedFormFieldsWithBlocksDto]): Form Fields extracted from the document, with associated
            blocks
        tables (List[DeprecatedExtractedTableWithBlocksDto]): Tables extracted from the document, with associated blocks
        labeling_start_time (Union[Unset, float]): Millisecond timestamp of when the labeling UI was opened
    """

    id: str
    form_fields: List[ExtractedFormFieldsWithBlocksDto]
    tables: List[DeprecatedExtractedTableWithBlocksDto]
    labeling_start_time: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        form_fields = []
        for form_fields_item_data in self.form_fields:
            form_fields_item = form_fields_item_data.to_dict()

            form_fields.append(form_fields_item)

        tables = []
        for tables_item_data in self.tables:
            tables_item = tables_item_data.to_dict()

            tables.append(tables_item)

        labeling_start_time = self.labeling_start_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "formFields": form_fields,
                "tables": tables,
            }
        )
        if labeling_start_time is not UNSET:
            field_dict["labelingStartTime"] = labeling_start_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        form_fields = []
        _form_fields = d.pop("formFields")
        for form_fields_item_data in _form_fields:
            form_fields_item = ExtractedFormFieldsWithBlocksDto.from_dict(form_fields_item_data)

            form_fields.append(form_fields_item)

        tables = []
        _tables = d.pop("tables")
        for tables_item_data in _tables:
            tables_item = DeprecatedExtractedTableWithBlocksDto.from_dict(tables_item_data)

            tables.append(tables_item)

        labeling_start_time = d.pop("labelingStartTime", UNSET)

        labeling_results_with_blocks_dto = cls(
            id=id,
            form_fields=form_fields,
            tables=tables,
            labeling_start_time=labeling_start_time,
        )

        labeling_results_with_blocks_dto.additional_properties = d
        return labeling_results_with_blocks_dto

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
