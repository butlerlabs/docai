from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.page_range_dto import PageRangeDto
from ..models.user_review_setting import UserReviewSetting

T = TypeVar("T", bound="QueueSettingsDto")


@attr.s(auto_attribs=True)
class QueueSettingsDto:
    """
    Attributes:
        notification_email (str): Email address to send notifications to
        user_review_setting (UserReviewSetting):
        butler_reviewers_on (bool): Whether Butler Ops should review the documents in this queue
        page_range (PageRangeDto):
        id (str): ID of this queue
        page_limit (float): Max number of pages that will be extracted per document
    """

    notification_email: str
    user_review_setting: UserReviewSetting
    butler_reviewers_on: bool
    page_range: PageRangeDto
    id: str
    page_limit: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        notification_email = self.notification_email
        user_review_setting = self.user_review_setting.value

        butler_reviewers_on = self.butler_reviewers_on
        page_range = self.page_range.to_dict()

        id = self.id
        page_limit = self.page_limit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "notificationEmail": notification_email,
                "userReviewSetting": user_review_setting,
                "butlerReviewersOn": butler_reviewers_on,
                "pageRange": page_range,
                "id": id,
                "pageLimit": page_limit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        notification_email = d.pop("notificationEmail")

        user_review_setting = UserReviewSetting(d.pop("userReviewSetting"))

        butler_reviewers_on = d.pop("butlerReviewersOn")

        page_range = PageRangeDto.from_dict(d.pop("pageRange"))

        id = d.pop("id")

        page_limit = d.pop("pageLimit")

        queue_settings_dto = cls(
            notification_email=notification_email,
            user_review_setting=user_review_setting,
            butler_reviewers_on=butler_reviewers_on,
            page_range=page_range,
            id=id,
            page_limit=page_limit,
        )

        queue_settings_dto.additional_properties = d
        return queue_settings_dto

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
