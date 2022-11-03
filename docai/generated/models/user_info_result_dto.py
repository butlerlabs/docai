from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="UserInfoResultDto")


@attr.s(auto_attribs=True)
class UserInfoResultDto:
    """
    Attributes:
        id (str):
        email_address (str):
        email_verified (bool):
        last_login (str):
    """

    id: str
    email_address: str
    email_verified: bool
    last_login: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        email_address = self.email_address
        email_verified = self.email_verified
        last_login = self.last_login

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "emailAddress": email_address,
                "emailVerified": email_verified,
                "lastLogin": last_login,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        email_address = d.pop("emailAddress")

        email_verified = d.pop("emailVerified")

        last_login = d.pop("lastLogin")

        user_info_result_dto = cls(
            id=id,
            email_address=email_address,
            email_verified=email_verified,
            last_login=last_login,
        )

        user_info_result_dto.additional_properties = d
        return user_info_result_dto

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
