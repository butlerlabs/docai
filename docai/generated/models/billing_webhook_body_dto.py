from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.billing_webhook_body_dto_content import BillingWebhookBodyDtoContent
from ..models.billing_webhook_dto import BillingWebhookDto
from ..types import UNSET, Unset

T = TypeVar("T", bound="BillingWebhookBodyDto")


@attr.s(auto_attribs=True)
class BillingWebhookBodyDto:
    """
    Attributes:
        id (str): Uniquely identifies a event
        occurred_at (float): Timestamp indicating when this event had occurred. UTC in seconds
        source (str): Source of the event
        webhook_status (str): The webhooks object is unavailable on the first webhook call for the event. For subsequent
            calls, this attribute holds the status from after the last retry
        content (BillingWebhookBodyDtoContent): The JSON data associated with this event
        user (Union[Unset, str]): The “user” that triggered the event. The value depends on the source attribute
        webhook_failure_reason (Union[Unset, str]): The reason why the webhook failed
        webhooks (Union[Unset, List[BillingWebhookDto]]): Array of webhook call statuses: one for each of the webhooks
            configured for the site
        event_type (Union[Unset, str]): The types of event provided by chargebee
        api_version (Union[Unset, str]): The Chargebee API Version used for rendering this event content. While
            processing webhooks, ensure this version is same as the API version used by your webhook server's client library
    """

    id: str
    occurred_at: float
    source: str
    webhook_status: str
    content: BillingWebhookBodyDtoContent
    user: Union[Unset, str] = UNSET
    webhook_failure_reason: Union[Unset, str] = UNSET
    webhooks: Union[Unset, List[BillingWebhookDto]] = UNSET
    event_type: Union[Unset, str] = UNSET
    api_version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        occurred_at = self.occurred_at
        source = self.source
        webhook_status = self.webhook_status
        content = self.content.to_dict()

        user = self.user
        webhook_failure_reason = self.webhook_failure_reason
        webhooks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.webhooks, Unset):
            webhooks = []
            for webhooks_item_data in self.webhooks:
                webhooks_item = webhooks_item_data.to_dict()

                webhooks.append(webhooks_item)

        event_type = self.event_type
        api_version = self.api_version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "occurred_at": occurred_at,
                "source": source,
                "webhook_status": webhook_status,
                "content": content,
            }
        )
        if user is not UNSET:
            field_dict["user"] = user
        if webhook_failure_reason is not UNSET:
            field_dict["webhook_failure_reason"] = webhook_failure_reason
        if webhooks is not UNSET:
            field_dict["webhooks"] = webhooks
        if event_type is not UNSET:
            field_dict["event_type"] = event_type
        if api_version is not UNSET:
            field_dict["api_version"] = api_version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        occurred_at = d.pop("occurred_at")

        source = d.pop("source")

        webhook_status = d.pop("webhook_status")

        content = BillingWebhookBodyDtoContent.from_dict(d.pop("content"))

        user = d.pop("user", UNSET)

        webhook_failure_reason = d.pop("webhook_failure_reason", UNSET)

        webhooks = []
        _webhooks = d.pop("webhooks", UNSET)
        for webhooks_item_data in _webhooks or []:
            webhooks_item = BillingWebhookDto.from_dict(webhooks_item_data)

            webhooks.append(webhooks_item)

        event_type = d.pop("event_type", UNSET)

        api_version = d.pop("api_version", UNSET)

        billing_webhook_body_dto = cls(
            id=id,
            occurred_at=occurred_at,
            source=source,
            webhook_status=webhook_status,
            content=content,
            user=user,
            webhook_failure_reason=webhook_failure_reason,
            webhooks=webhooks,
            event_type=event_type,
            api_version=api_version,
        )

        billing_webhook_body_dto.additional_properties = d
        return billing_webhook_body_dto

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
