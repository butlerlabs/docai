from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.chargebee_hosted_page_dto_checkout_info import ChargebeeHostedPageDtoCheckoutInfo
from ..types import UNSET, Unset

T = TypeVar("T", bound="ChargebeeHostedPageDto")


@attr.s(auto_attribs=True)
class ChargebeeHostedPageDto:
    """
    Attributes:
        embed (bool): If true then hosted page formatted to be shown in iframe. If false, it is formatted to be shown as
            a separate page
        id (Union[Unset, str]): ID of the plan to use while creating a subscription
        type (Union[Unset, str]): Type of the requested hosted page
        url (Union[Unset, str]): Unique URL for the hosted page that will be included in your website
        state (Union[Unset, str]): Indicating the current state of the hosted page resource
        failure_reason (Union[Unset, str]): Reason hosted page could not be created
        pass_thru_content (Union[Unset, str]): You can pass through any content specific to the hosted page request and
            get it back after user had submitted the hosted page
        created_at (Union[Unset, float]): Indicates when this hosted page url is generated. UTC in seconds
        expires_at (Union[Unset, float]): Indicates when this hosted page url will expire. After this, the hosted page
            cannot be accessed. UTC in seconds
        updated_at (Union[Unset, float]): Timestamp indicating when this hosted page was last updated. UTC in seconds
        resource_version (Union[Unset, float]): Version number of this resource. Each update of this resource results in
            incremental change of this number
        checkout_info (Union[Unset, ChargebeeHostedPageDtoCheckoutInfo]): Customer Info (email, first name and last
            name) given in the checkout page used for tracking abandoned carts
    """

    embed: bool
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    failure_reason: Union[Unset, str] = UNSET
    pass_thru_content: Union[Unset, str] = UNSET
    created_at: Union[Unset, float] = UNSET
    expires_at: Union[Unset, float] = UNSET
    updated_at: Union[Unset, float] = UNSET
    resource_version: Union[Unset, float] = UNSET
    checkout_info: Union[Unset, ChargebeeHostedPageDtoCheckoutInfo] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        embed = self.embed
        id = self.id
        type = self.type
        url = self.url
        state = self.state
        failure_reason = self.failure_reason
        pass_thru_content = self.pass_thru_content
        created_at = self.created_at
        expires_at = self.expires_at
        updated_at = self.updated_at
        resource_version = self.resource_version
        checkout_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.checkout_info, Unset):
            checkout_info = self.checkout_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "embed": embed,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["type"] = type
        if url is not UNSET:
            field_dict["url"] = url
        if state is not UNSET:
            field_dict["state"] = state
        if failure_reason is not UNSET:
            field_dict["failure_reason"] = failure_reason
        if pass_thru_content is not UNSET:
            field_dict["pass_thru_content"] = pass_thru_content
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if resource_version is not UNSET:
            field_dict["resource_version"] = resource_version
        if checkout_info is not UNSET:
            field_dict["checkout_info"] = checkout_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        embed = d.pop("embed")

        id = d.pop("id", UNSET)

        type = d.pop("type", UNSET)

        url = d.pop("url", UNSET)

        state = d.pop("state", UNSET)

        failure_reason = d.pop("failure_reason", UNSET)

        pass_thru_content = d.pop("pass_thru_content", UNSET)

        created_at = d.pop("created_at", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        resource_version = d.pop("resource_version", UNSET)

        _checkout_info = d.pop("checkout_info", UNSET)
        checkout_info: Union[Unset, ChargebeeHostedPageDtoCheckoutInfo]
        if isinstance(_checkout_info, Unset):
            checkout_info = UNSET
        else:
            checkout_info = ChargebeeHostedPageDtoCheckoutInfo.from_dict(_checkout_info)

        chargebee_hosted_page_dto = cls(
            embed=embed,
            id=id,
            type=type,
            url=url,
            state=state,
            failure_reason=failure_reason,
            pass_thru_content=pass_thru_content,
            created_at=created_at,
            expires_at=expires_at,
            updated_at=updated_at,
            resource_version=resource_version,
            checkout_info=checkout_info,
        )

        chargebee_hosted_page_dto.additional_properties = d
        return chargebee_hosted_page_dto

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
