from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.butler_ops_label_row_dto import ButlerOpsLabelRowDto
from ..types import UNSET, Unset

T = TypeVar("T", bound="ButlerOpsLabelTableDto")


@attr.s(auto_attribs=True)
class ButlerOpsLabelTableDto:
    """
    Attributes:
        column_headers (ButlerOpsLabelRowDto):
        rows (List[ButlerOpsLabelRowDto]): Rows to label for this table
        is_unsure (Union[Unset, bool]): If the Butler Ops agent was unsure about this form field
        unsure_details (Union[Unset, str]): Details on why the Butler Ops agent was unsure about this form field
    """

    column_headers: ButlerOpsLabelRowDto
    rows: List[ButlerOpsLabelRowDto]
    is_unsure: Union[Unset, bool] = UNSET
    unsure_details: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        column_headers = self.column_headers.to_dict()

        rows = []
        for rows_item_data in self.rows:
            rows_item = rows_item_data.to_dict()

            rows.append(rows_item)

        is_unsure = self.is_unsure
        unsure_details = self.unsure_details

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "columnHeaders": column_headers,
                "rows": rows,
            }
        )
        if is_unsure is not UNSET:
            field_dict["isUnsure"] = is_unsure
        if unsure_details is not UNSET:
            field_dict["unsureDetails"] = unsure_details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        column_headers = ButlerOpsLabelRowDto.from_dict(d.pop("columnHeaders"))

        rows = []
        _rows = d.pop("rows")
        for rows_item_data in _rows:
            rows_item = ButlerOpsLabelRowDto.from_dict(rows_item_data)

            rows.append(rows_item)

        is_unsure = d.pop("isUnsure", UNSET)

        unsure_details = d.pop("unsureDetails", UNSET)

        butler_ops_label_table_dto = cls(
            column_headers=column_headers,
            rows=rows,
            is_unsure=is_unsure,
            unsure_details=unsure_details,
        )

        butler_ops_label_table_dto.additional_properties = d
        return butler_ops_label_table_dto

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
