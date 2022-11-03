from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.role_name import RoleName

T = TypeVar("T", bound="RoleDto")


@attr.s(auto_attribs=True)
class RoleDto:
    """
    Attributes:
        name (RoleName):
    """

    name: RoleName
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = RoleName(d.pop("name"))

        role_dto = cls(
            name=name,
        )

        role_dto.additional_properties = d
        return role_dto

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
