from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.extracted_field_labeling_results_dto import ExtractedFieldLabelingResultsDto

T = TypeVar("T", bound="ButlerOpsLabelRowDto")


@attr.s(auto_attribs=True)
class ButlerOpsLabelRowDto:
    """
    Attributes:
        id (str): Id of the row to label
        cells (List[ExtractedFieldLabelingResultsDto]): Value to label for the cells in this row
    """

    id: str
    cells: List[ExtractedFieldLabelingResultsDto]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        cells = []
        for cells_item_data in self.cells:
            cells_item = cells_item_data.to_dict()

            cells.append(cells_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "cells": cells,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        cells = []
        _cells = d.pop("cells")
        for cells_item_data in _cells:
            cells_item = ExtractedFieldLabelingResultsDto.from_dict(cells_item_data)

            cells.append(cells_item)

        butler_ops_label_row_dto = cls(
            id=id,
            cells=cells,
        )

        butler_ops_label_row_dto.additional_properties = d
        return butler_ops_label_row_dto

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
