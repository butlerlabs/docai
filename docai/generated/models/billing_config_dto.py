from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="BillingConfigDto")


@attr.s(auto_attribs=True)
class BillingConfigDto:
    """
    Attributes:
        site (str): Name of the Chargebee site billing system connects to
        api_key (str): API key that is safe to be used from the UI for the purposes of enabling users to purchase a plan
            and manage their subscriptions
    """

    site: str
    api_key: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        site = self.site
        api_key = self.api_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "site": site,
                "apiKey": api_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        site = d.pop("site")

        api_key = d.pop("apiKey")

        billing_config_dto = cls(
            site=site,
            api_key=api_key,
        )

        billing_config_dto.additional_properties = d
        return billing_config_dto

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
