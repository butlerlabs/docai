from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.enhanced_form_field_result_with_blocks_dto import EnhancedFormFieldResultWithBlocksDto
from ..models.enhanced_table_result_with_blocks_dto import EnhancedTableResultWithBlocksDto

T = TypeVar("T", bound="EnhancedExtractionResultsDto")


@attr.s(auto_attribs=True)
class EnhancedExtractionResultsDto:
    """
    Attributes:
        form_fields (List[EnhancedFormFieldResultWithBlocksDto]): Form fields extracted as a part of these extraction
            results
        tables (List[EnhancedTableResultWithBlocksDto]): Tables extracted as a part of these extraction results
    """

    form_fields: List[EnhancedFormFieldResultWithBlocksDto]
    tables: List[EnhancedTableResultWithBlocksDto]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        form_fields = []
        for form_fields_item_data in self.form_fields:
            form_fields_item = form_fields_item_data.to_dict()

            form_fields.append(form_fields_item)

        tables = []
        for tables_item_data in self.tables:
            tables_item = tables_item_data.to_dict()

            tables.append(tables_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "formFields": form_fields,
                "tables": tables,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        form_fields = []
        _form_fields = d.pop("formFields")
        for form_fields_item_data in _form_fields:
            form_fields_item = EnhancedFormFieldResultWithBlocksDto.from_dict(form_fields_item_data)

            form_fields.append(form_fields_item)

        tables = []
        _tables = d.pop("tables")
        for tables_item_data in _tables:
            tables_item = EnhancedTableResultWithBlocksDto.from_dict(tables_item_data)

            tables.append(tables_item)

        enhanced_extraction_results_dto = cls(
            form_fields=form_fields,
            tables=tables,
        )

        enhanced_extraction_results_dto.additional_properties = d
        return enhanced_extraction_results_dto

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
