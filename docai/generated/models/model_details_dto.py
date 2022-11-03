from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.base_model_type import BaseModelType
from ..models.model_field_dto import ModelFieldDto
from ..models.model_status import ModelStatus
from ..models.model_table_dto import ModelTableDto
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelDetailsDto")


@attr.s(auto_attribs=True)
class ModelDetailsDto:
    """
    Attributes:
        id (str): The unique id of this model.
        name (str): Name of the model.
        status (ModelStatus):
        model_type (BaseModelType):
        fields (List[ModelFieldDto]): The text, checkbox, and signature fields for this model
        tables (List[ModelTableDto]): The table fields for this model
        training_failure_reason (Union[Unset, str]): Reason for previous training failure
    """

    id: str
    name: str
    status: ModelStatus
    model_type: BaseModelType
    fields: List[ModelFieldDto]
    tables: List[ModelTableDto]
    training_failure_reason: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        status = self.status.value

        model_type = self.model_type.value

        fields = []
        for fields_item_data in self.fields:
            fields_item = fields_item_data.to_dict()

            fields.append(fields_item)

        tables = []
        for tables_item_data in self.tables:
            tables_item = tables_item_data.to_dict()

            tables.append(tables_item)

        training_failure_reason = self.training_failure_reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "status": status,
                "modelType": model_type,
                "fields": fields,
                "tables": tables,
            }
        )
        if training_failure_reason is not UNSET:
            field_dict["trainingFailureReason"] = training_failure_reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        status = ModelStatus(d.pop("status"))

        model_type = BaseModelType(d.pop("modelType"))

        fields = []
        _fields = d.pop("fields")
        for fields_item_data in _fields:
            fields_item = ModelFieldDto.from_dict(fields_item_data)

            fields.append(fields_item)

        tables = []
        _tables = d.pop("tables")
        for tables_item_data in _tables:
            tables_item = ModelTableDto.from_dict(tables_item_data)

            tables.append(tables_item)

        training_failure_reason = d.pop("trainingFailureReason", UNSET)

        model_details_dto = cls(
            id=id,
            name=name,
            status=status,
            model_type=model_type,
            fields=fields,
            tables=tables,
            training_failure_reason=training_failure_reason,
        )

        model_details_dto.additional_properties = d
        return model_details_dto

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
