from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.model_status_enum import ModelStatusEnum
from ..models.model_type_enum import ModelTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="MlModelDto")


@attr.s(auto_attribs=True)
class MlModelDto:
    """
    Attributes:
        model_id (str): The id of the ml model.
        name (str): The name of the ml model.
        status (ModelStatusEnum):
        model_type (ModelTypeEnum):
        latest_version_id (Union[Unset, str]): The latest version id of the ml model.
    """

    model_id: str
    name: str
    status: ModelStatusEnum
    model_type: ModelTypeEnum
    latest_version_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        model_id = self.model_id
        name = self.name
        status = self.status.value

        model_type = self.model_type.value

        latest_version_id = self.latest_version_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "modelId": model_id,
                "name": name,
                "status": status,
                "modelType": model_type,
            }
        )
        if latest_version_id is not UNSET:
            field_dict["latestVersionId"] = latest_version_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        model_id = d.pop("modelId")

        name = d.pop("name")

        status = ModelStatusEnum(d.pop("status"))

        model_type = ModelTypeEnum(d.pop("modelType"))

        latest_version_id = d.pop("latestVersionId", UNSET)

        ml_model_dto = cls(
            model_id=model_id,
            name=name,
            status=status,
            model_type=model_type,
            latest_version_id=latest_version_id,
        )

        ml_model_dto.additional_properties = d
        return ml_model_dto

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
