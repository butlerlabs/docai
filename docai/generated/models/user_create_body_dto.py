from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="UserCreateBodyDto")


@attr.s(auto_attribs=True)
class UserCreateBodyDto:
    """
    Attributes:
        email_address (str):
    """

    email_address: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email_address = self.email_address

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "emailAddress": email_address,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email_address = d.pop("emailAddress")

        user_create_body_dto = cls(
            email_address=email_address,
        )

        user_create_body_dto.additional_properties = d
        return user_create_body_dto

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
