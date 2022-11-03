from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChargebeeLinkedCustomerDto")


@attr.s(auto_attribs=True)
class ChargebeeLinkedCustomerDto:
    """
    Attributes:
        customer_id (str): Identifier of the customer
        has_billing_address (bool): The customer has billing address
        has_payment_method (bool): The customer has payment method
        has_active_subscription (bool): The customer has at least one active subscription
        email (Union[Unset, str]): Email of the customer. Configured email notifications will be sent to this email
    """

    customer_id: str
    has_billing_address: bool
    has_payment_method: bool
    has_active_subscription: bool
    email: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customer_id = self.customer_id
        has_billing_address = self.has_billing_address
        has_payment_method = self.has_payment_method
        has_active_subscription = self.has_active_subscription
        email = self.email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customer_id": customer_id,
                "has_billing_address": has_billing_address,
                "has_payment_method": has_payment_method,
                "has_active_subscription": has_active_subscription,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        customer_id = d.pop("customer_id")

        has_billing_address = d.pop("has_billing_address")

        has_payment_method = d.pop("has_payment_method")

        has_active_subscription = d.pop("has_active_subscription")

        email = d.pop("email", UNSET)

        chargebee_linked_customer_dto = cls(
            customer_id=customer_id,
            has_billing_address=has_billing_address,
            has_payment_method=has_payment_method,
            has_active_subscription=has_active_subscription,
            email=email,
        )

        chargebee_linked_customer_dto.additional_properties = d
        return chargebee_linked_customer_dto

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
