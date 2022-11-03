from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ChargebeeHostedPageDtoCheckoutInfo")


@attr.s(auto_attribs=True)
class ChargebeeHostedPageDtoCheckoutInfo:
    """Customer Info (email, first name and last name) given in the checkout page used for tracking abandoned carts"""

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        chargebee_hosted_page_dto_checkout_info = cls()

        chargebee_hosted_page_dto_checkout_info.additional_properties = d
        return chargebee_hosted_page_dto_checkout_info

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
