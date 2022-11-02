from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.extra_row_dto import ExtraRowDto

T = TypeVar("T", bound="ExtraTableDto")


@attr.s(auto_attribs=True)
class ExtraTableDto:
    """
    Attributes:
        rows (List[ExtraRowDto]): An array of this table's rows
    """

    rows: List[ExtraRowDto]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rows = []
        for rows_item_data in self.rows:
            rows_item = rows_item_data.to_dict()

            rows.append(rows_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rows": rows,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        rows = []
        _rows = d.pop("rows")
        for rows_item_data in _rows:
            rows_item = ExtraRowDto.from_dict(rows_item_data)

            rows.append(rows_item)

        extra_table_dto = cls(
            rows=rows,
        )

        extra_table_dto.additional_properties = d
        return extra_table_dto

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
