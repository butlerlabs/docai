from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="EnvironmentDto")


@attr.s(auto_attribs=True)
class EnvironmentDto:
    """
    Attributes:
        auth_0_client_id (str): Auth0 client ID
        analytics_write_key (str): Segment write key
        deployment (str): Deployment name
    """

    auth_0_client_id: str
    analytics_write_key: str
    deployment: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        auth_0_client_id = self.auth_0_client_id
        analytics_write_key = self.analytics_write_key
        deployment = self.deployment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "auth0ClientId": auth_0_client_id,
                "analyticsWriteKey": analytics_write_key,
                "deployment": deployment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        auth_0_client_id = d.pop("auth0ClientId")

        analytics_write_key = d.pop("analyticsWriteKey")

        deployment = d.pop("deployment")

        environment_dto = cls(
            auth_0_client_id=auth_0_client_id,
            analytics_write_key=analytics_write_key,
            deployment=deployment,
        )

        environment_dto.additional_properties = d
        return environment_dto

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
