from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.feature_name import FeatureName

T = TypeVar("T", bound="FeatureDto")


@attr.s(auto_attribs=True)
class FeatureDto:
    """
    Attributes:
        name (FeatureName):
        enabled (bool): Whether the feature is enabled
    """

    name: FeatureName
    enabled: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name.value

        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "enabled": enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = FeatureName(d.pop("name"))

        enabled = d.pop("enabled")

        feature_dto = cls(
            name=name,
            enabled=enabled,
        )

        feature_dto.additional_properties = d
        return feature_dto

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
