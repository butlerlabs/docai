from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.extra_block_dto import ExtraBlockDto

T = TypeVar("T", bound="ExtraRowDto")


@attr.s(auto_attribs=True)
class ExtraRowDto:
    """
    Attributes:
        cells (List[ExtraBlockDto]): An array of this row's cells
    """

    cells: List[ExtraBlockDto]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cells = []
        for cells_item_data in self.cells:
            cells_item = cells_item_data.to_dict()

            cells.append(cells_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cells": cells,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cells = []
        _cells = d.pop("cells")
        for cells_item_data in _cells:
            cells_item = ExtraBlockDto.from_dict(cells_item_data)

            cells.append(cells_item)

        extra_row_dto = cls(
            cells=cells,
        )

        extra_row_dto.additional_properties = d
        return extra_row_dto

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
