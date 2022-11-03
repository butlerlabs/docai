from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="MlModelVersionDto")


@attr.s(auto_attribs=True)
class MlModelVersionDto:
    """
    Attributes:
        model_id (str): The id of the ml model.
        version_id (str): The version id of the ml model.
        version (float): The version number.
        endpoint_id (Union[Unset, str]): The active endpoint id of this model version.
    """

    model_id: str
    version_id: str
    version: float
    endpoint_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        model_id = self.model_id
        version_id = self.version_id
        version = self.version
        endpoint_id = self.endpoint_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "modelId": model_id,
                "versionId": version_id,
                "version": version,
            }
        )
        if endpoint_id is not UNSET:
            field_dict["endpointId"] = endpoint_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        model_id = d.pop("modelId")

        version_id = d.pop("versionId")

        version = d.pop("version")

        endpoint_id = d.pop("endpointId", UNSET)

        ml_model_version_dto = cls(
            model_id=model_id,
            version_id=version_id,
            version=version,
            endpoint_id=endpoint_id,
        )

        ml_model_version_dto.additional_properties = d
        return ml_model_version_dto

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
