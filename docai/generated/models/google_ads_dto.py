from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GoogleAdsDto")


@attr.s(auto_attribs=True)
class GoogleAdsDto:
    """
    Attributes:
        gclid (Union[Unset, str]): The GCLID from Google Ads associated with this user
        utm_term (Union[Unset, str]): The UTM_TERM from Google Ads associated with this user
        utm_campaign (Union[Unset, str]): The UTM_CAMPAIGN from Google Ads associated with this user
        utm_source (Union[Unset, str]): The UTM_SOURCE from Google Ads associated with this user
        utm_medium (Union[Unset, str]): The UTM_MEDIUM from Google Ads associated with this user
    """

    gclid: Union[Unset, str] = UNSET
    utm_term: Union[Unset, str] = UNSET
    utm_campaign: Union[Unset, str] = UNSET
    utm_source: Union[Unset, str] = UNSET
    utm_medium: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        gclid = self.gclid
        utm_term = self.utm_term
        utm_campaign = self.utm_campaign
        utm_source = self.utm_source
        utm_medium = self.utm_medium

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gclid is not UNSET:
            field_dict["gclid"] = gclid
        if utm_term is not UNSET:
            field_dict["utmTerm"] = utm_term
        if utm_campaign is not UNSET:
            field_dict["utmCampaign"] = utm_campaign
        if utm_source is not UNSET:
            field_dict["utmSource"] = utm_source
        if utm_medium is not UNSET:
            field_dict["utmMedium"] = utm_medium

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        gclid = d.pop("gclid", UNSET)

        utm_term = d.pop("utmTerm", UNSET)

        utm_campaign = d.pop("utmCampaign", UNSET)

        utm_source = d.pop("utmSource", UNSET)

        utm_medium = d.pop("utmMedium", UNSET)

        google_ads_dto = cls(
            gclid=gclid,
            utm_term=utm_term,
            utm_campaign=utm_campaign,
            utm_source=utm_source,
            utm_medium=utm_medium,
        )

        google_ads_dto.additional_properties = d
        return google_ads_dto

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
