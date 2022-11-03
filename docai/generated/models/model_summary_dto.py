from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.model_status import ModelStatus
from ..models.model_summary_base_model_type import ModelSummaryBaseModelType
from ..models.model_summary_task_type import ModelSummaryTaskType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelSummaryDto")


@attr.s(auto_attribs=True)
class ModelSummaryDto:
    """
    Attributes:
        id (str): ID of this model
        name (str): Name of this model
        status (ModelStatus):
        task_type (ModelSummaryTaskType):
        base_model (ModelSummaryBaseModelType):
        description (str): Description of this model
        training_failure_reason (Union[Unset, str]): Reason for previous training failure
    """

    id: str
    name: str
    status: ModelStatus
    task_type: ModelSummaryTaskType
    base_model: ModelSummaryBaseModelType
    description: str
    training_failure_reason: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        status = self.status.value

        task_type = self.task_type.value

        base_model = self.base_model.value

        description = self.description
        training_failure_reason = self.training_failure_reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "status": status,
                "taskType": task_type,
                "baseModel": base_model,
                "description": description,
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

        task_type = ModelSummaryTaskType(d.pop("taskType"))

        base_model = ModelSummaryBaseModelType(d.pop("baseModel"))

        description = d.pop("description")

        training_failure_reason = d.pop("trainingFailureReason", UNSET)

        model_summary_dto = cls(
            id=id,
            name=name,
            status=status,
            task_type=task_type,
            base_model=base_model,
            description=description,
            training_failure_reason=training_failure_reason,
        )

        model_summary_dto.additional_properties = d
        return model_summary_dto

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
