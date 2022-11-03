from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.base_model_type import BaseModelType
from ..models.model_status import ModelStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentTypeDto")


@attr.s(auto_attribs=True)
class DocumentTypeDto:
    """
    Attributes:
        id (str): ID of this doctype
        name (str): Name of this doctype
        status (ModelStatus):
        model_type (BaseModelType):
        description (str): Description of this doctype
        training_failure_reason (Union[Unset, str]): Reason for previous training failure
    """

    id: str
    name: str
    status: ModelStatus
    model_type: BaseModelType
    description: str
    training_failure_reason: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        status = self.status.value

        model_type = self.model_type.value

        description = self.description
        training_failure_reason = self.training_failure_reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "status": status,
                "modelType": model_type,
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

        model_type = BaseModelType(d.pop("modelType"))

        description = d.pop("description")

        training_failure_reason = d.pop("trainingFailureReason", UNSET)

        document_type_dto = cls(
            id=id,
            name=name,
            status=status,
            model_type=model_type,
            description=description,
            training_failure_reason=training_failure_reason,
        )

        document_type_dto.additional_properties = d
        return document_type_dto

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
