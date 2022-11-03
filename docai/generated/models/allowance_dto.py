from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.allowance_refresh_interval import AllowanceRefreshInterval

T = TypeVar("T", bound="AllowanceDto")


@attr.s(auto_attribs=True)
class AllowanceDto:
    """
    Attributes:
        remaining (float): Allowance currently remaining
        refresh_interval (AllowanceRefreshInterval):
        refresh_amount (float): Allowance amount that we refresh to on the refresh interval
        next_refresh_time (float): Unix timestamp for next refresh time. When allowance type is Never, this will be a
            very large number that should be ignored
    """

    remaining: float
    refresh_interval: AllowanceRefreshInterval
    refresh_amount: float
    next_refresh_time: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        remaining = self.remaining
        refresh_interval = self.refresh_interval.value

        refresh_amount = self.refresh_amount
        next_refresh_time = self.next_refresh_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "remaining": remaining,
                "refreshInterval": refresh_interval,
                "refreshAmount": refresh_amount,
                "nextRefreshTime": next_refresh_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        remaining = d.pop("remaining")

        refresh_interval = AllowanceRefreshInterval(d.pop("refreshInterval"))

        refresh_amount = d.pop("refreshAmount")

        next_refresh_time = d.pop("nextRefreshTime")

        allowance_dto = cls(
            remaining=remaining,
            refresh_interval=refresh_interval,
            refresh_amount=refresh_amount,
            next_refresh_time=next_refresh_time,
        )

        allowance_dto.additional_properties = d
        return allowance_dto

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
