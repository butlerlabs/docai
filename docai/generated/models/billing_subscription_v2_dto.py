from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.allowance_dto import AllowanceDto
from ..models.billing_plan_id import BillingPlanId
from ..models.billing_subscription_name_v2 import BillingSubscriptionNameV2
from ..types import UNSET, Unset

T = TypeVar("T", bound="BillingSubscriptionV2Dto")


@attr.s(auto_attribs=True)
class BillingSubscriptionV2Dto:
    """
    Attributes:
        name (BillingSubscriptionNameV2):
        free_pages (AllowanceDto):
        chargebee_plan_id (Union[Unset, BillingPlanId]):
    """

    name: BillingSubscriptionNameV2
    free_pages: AllowanceDto
    chargebee_plan_id: Union[Unset, BillingPlanId] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name.value

        free_pages = self.free_pages.to_dict()

        chargebee_plan_id: Union[Unset, str] = UNSET
        if not isinstance(self.chargebee_plan_id, Unset):
            chargebee_plan_id = self.chargebee_plan_id.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "freePages": free_pages,
            }
        )
        if chargebee_plan_id is not UNSET:
            field_dict["chargebeePlanId"] = chargebee_plan_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = BillingSubscriptionNameV2(d.pop("name"))

        free_pages = AllowanceDto.from_dict(d.pop("freePages"))

        _chargebee_plan_id = d.pop("chargebeePlanId", UNSET)
        chargebee_plan_id: Union[Unset, BillingPlanId]
        if isinstance(_chargebee_plan_id, Unset):
            chargebee_plan_id = UNSET
        else:
            chargebee_plan_id = BillingPlanId(_chargebee_plan_id)

        billing_subscription_v2_dto = cls(
            name=name,
            free_pages=free_pages,
            chargebee_plan_id=chargebee_plan_id,
        )

        billing_subscription_v2_dto.additional_properties = d
        return billing_subscription_v2_dto

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
