from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.training_cell_with_confidence_labeled_result_dto import TrainingCellWithConfidenceLabeledResultDto

T = TypeVar("T", bound="TrainingRowWithConfidenceLabeledResultDto")


@attr.s(auto_attribs=True)
class TrainingRowWithConfidenceLabeledResultDto:
    """
    Attributes:
        id (str): The unique id of this row.
        cells (List[TrainingCellWithConfidenceLabeledResultDto]): The labeled results for this cell.
    """

    id: str
    cells: List[TrainingCellWithConfidenceLabeledResultDto]
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
            cells_item = TrainingCellWithConfidenceLabeledResultDto.from_dict(cells_item_data)

            cells.append(cells_item)

        training_row_with_confidence_labeled_result_dto = cls(
            id=id,
            cells=cells,
        )

        training_row_with_confidence_labeled_result_dto.additional_properties = d
        return training_row_with_confidence_labeled_result_dto

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
