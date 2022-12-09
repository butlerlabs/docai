from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="LoginResponseDto")


@attr.s(auto_attribs=True)
class LoginResponseDto:
    """
    Attributes:
        api_token (str): API token.
    """

    api_token: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        api_token = self.api_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiToken": api_token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        api_token = d.pop("apiToken")

        login_response_dto = cls(
            api_token=api_token,
        )

        login_response_dto.additional_properties = d
        return login_response_dto

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
