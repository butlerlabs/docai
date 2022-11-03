from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.google_ads_dto import GoogleAdsDto
from ..models.survey_response_dto import SurveyResponseDto

T = TypeVar("T", bound="CompleteUserOnboardingDto")


@attr.s(auto_attribs=True)
class CompleteUserOnboardingDto:
    """
    Attributes:
        has_pdt_use_case (bool): Whether or not the onboarded customer has a PDT use case
        survey_response (SurveyResponseDto):
        google_ads (GoogleAdsDto):
    """

    has_pdt_use_case: bool
    survey_response: SurveyResponseDto
    google_ads: GoogleAdsDto
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        has_pdt_use_case = self.has_pdt_use_case
        survey_response = self.survey_response.to_dict()

        google_ads = self.google_ads.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hasPdtUseCase": has_pdt_use_case,
                "surveyResponse": survey_response,
                "googleAds": google_ads,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        has_pdt_use_case = d.pop("hasPdtUseCase")

        survey_response = SurveyResponseDto.from_dict(d.pop("surveyResponse"))

        google_ads = GoogleAdsDto.from_dict(d.pop("googleAds"))

        complete_user_onboarding_dto = cls(
            has_pdt_use_case=has_pdt_use_case,
            survey_response=survey_response,
            google_ads=google_ads,
        )

        complete_user_onboarding_dto.additional_properties = d
        return complete_user_onboarding_dto

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
