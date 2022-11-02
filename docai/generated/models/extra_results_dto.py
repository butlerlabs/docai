from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.extra_block_dto import ExtraBlockDto
from ..models.extra_form_field_dto import ExtraFormFieldDto
from ..models.extra_table_dto import ExtraTableDto
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExtraResultsDto")


@attr.s(auto_attribs=True)
class ExtraResultsDto:
    """
    Attributes:
        line_blocks (Union[Unset, None, List[ExtraBlockDto]]): Extra lineBlocks, only present if requested. If this is
            an old document, or extra results otherwise failed to generate, then the value will be null
        form_fields (Union[Unset, None, List[ExtraFormFieldDto]]): Extra formFields, only present if requested. If this
            is an old document, or extra results otherwise failed to generate, then the value will be null
        tables (Union[Unset, None, List[ExtraTableDto]]): Extra tables, only present if requested. If this is an old
            document, or extra results otherwise failed to generate, then the value will be null
    """

    line_blocks: Union[Unset, None, List[ExtraBlockDto]] = UNSET
    form_fields: Union[Unset, None, List[ExtraFormFieldDto]] = UNSET
    tables: Union[Unset, None, List[ExtraTableDto]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        line_blocks: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.line_blocks, Unset):
            if self.line_blocks is None:
                line_blocks = None
            else:
                line_blocks = []
                for line_blocks_item_data in self.line_blocks:
                    line_blocks_item = line_blocks_item_data.to_dict()

                    line_blocks.append(line_blocks_item)

        form_fields: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.form_fields, Unset):
            if self.form_fields is None:
                form_fields = None
            else:
                form_fields = []
                for form_fields_item_data in self.form_fields:
                    form_fields_item = form_fields_item_data.to_dict()

                    form_fields.append(form_fields_item)

        tables: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tables, Unset):
            if self.tables is None:
                tables = None
            else:
                tables = []
                for tables_item_data in self.tables:
                    tables_item = tables_item_data.to_dict()

                    tables.append(tables_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if line_blocks is not UNSET:
            field_dict["lineBlocks"] = line_blocks
        if form_fields is not UNSET:
            field_dict["formFields"] = form_fields
        if tables is not UNSET:
            field_dict["tables"] = tables

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        line_blocks = []
        _line_blocks = d.pop("lineBlocks", UNSET)
        for line_blocks_item_data in _line_blocks or []:
            line_blocks_item = ExtraBlockDto.from_dict(line_blocks_item_data)

            line_blocks.append(line_blocks_item)

        form_fields = []
        _form_fields = d.pop("formFields", UNSET)
        for form_fields_item_data in _form_fields or []:
            form_fields_item = ExtraFormFieldDto.from_dict(form_fields_item_data)

            form_fields.append(form_fields_item)

        tables = []
        _tables = d.pop("tables", UNSET)
        for tables_item_data in _tables or []:
            tables_item = ExtraTableDto.from_dict(tables_item_data)

            tables.append(tables_item)

        extra_results_dto = cls(
            line_blocks=line_blocks,
            form_fields=form_fields,
            tables=tables,
        )

        extra_results_dto.additional_properties = d
        return extra_results_dto

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
