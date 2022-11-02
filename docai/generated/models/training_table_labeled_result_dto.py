from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.model_field_type import ModelFieldType
from ..models.training_column_dto import TrainingColumnDto
from ..models.training_row_labeled_result_dto import TrainingRowLabeledResultDto

T = TypeVar("T", bound="TrainingTableLabeledResultDto")


@attr.s(auto_attribs=True)
class TrainingTableLabeledResultDto:
    """
    Attributes:
        id (str): The unique id of this table.
        name (str): The name of the table.
        type (ModelFieldType):
        columns (List[TrainingColumnDto]): The columns for this table.
        rows (List[TrainingRowLabeledResultDto]): The rows and labeled results for this table.
    """

    id: str
    name: str
    type: ModelFieldType
    columns: List[TrainingColumnDto]
    rows: List[TrainingRowLabeledResultDto]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        type = self.type.value

        columns = []
        for columns_item_data in self.columns:
            columns_item = columns_item_data.to_dict()

            columns.append(columns_item)

        rows = []
        for rows_item_data in self.rows:
            rows_item = rows_item_data.to_dict()

            rows.append(rows_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "type": type,
                "columns": columns,
                "rows": rows,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        type = ModelFieldType(d.pop("type"))

        columns = []
        _columns = d.pop("columns")
        for columns_item_data in _columns:
            columns_item = TrainingColumnDto.from_dict(columns_item_data)

            columns.append(columns_item)

        rows = []
        _rows = d.pop("rows")
        for rows_item_data in _rows:
            rows_item = TrainingRowLabeledResultDto.from_dict(rows_item_data)

            rows.append(rows_item)

        training_table_labeled_result_dto = cls(
            id=id,
            name=name,
            type=type,
            columns=columns,
            rows=rows,
        )

        training_table_labeled_result_dto.additional_properties = d
        return training_table_labeled_result_dto

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
