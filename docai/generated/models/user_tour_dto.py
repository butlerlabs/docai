from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.cdt_self_service_tour_step_enum import CdtSelfServiceTourStepEnum
from ..models.create_first_doc_type_step_enum import CreateFirstDocTypeStepEnum
from ..models.pdt_self_service_tour_step_enum import PdtSelfServiceTourStepEnum
from ..models.survey_response_dto import SurveyResponseDto
from ..models.training_a_custom_model_tour_step_enum import TrainingACustomModelTourStepEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserTourDto")


@attr.s(auto_attribs=True)
class UserTourDto:
    """
    Attributes:
        first_doc_type_tour_step (CreateFirstDocTypeStepEnum):
        pdt_self_service_tour_step (PdtSelfServiceTourStepEnum):
        cdt_self_service_tour_step (CdtSelfServiceTourStepEnum):
        training_a_custom_model_tour_step (TrainingACustomModelTourStepEnum):
        survey_response (Union[Unset, SurveyResponseDto]):
    """

    first_doc_type_tour_step: CreateFirstDocTypeStepEnum
    pdt_self_service_tour_step: PdtSelfServiceTourStepEnum
    cdt_self_service_tour_step: CdtSelfServiceTourStepEnum
    training_a_custom_model_tour_step: TrainingACustomModelTourStepEnum
    survey_response: Union[Unset, SurveyResponseDto] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        first_doc_type_tour_step = self.first_doc_type_tour_step.value

        pdt_self_service_tour_step = self.pdt_self_service_tour_step.value

        cdt_self_service_tour_step = self.cdt_self_service_tour_step.value

        training_a_custom_model_tour_step = self.training_a_custom_model_tour_step.value

        survey_response: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.survey_response, Unset):
            survey_response = self.survey_response.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "firstDocTypeTourStep": first_doc_type_tour_step,
                "pdtSelfServiceTourStep": pdt_self_service_tour_step,
                "cdtSelfServiceTourStep": cdt_self_service_tour_step,
                "trainingACustomModelTourStep": training_a_custom_model_tour_step,
            }
        )
        if survey_response is not UNSET:
            field_dict["surveyResponse"] = survey_response

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        first_doc_type_tour_step = CreateFirstDocTypeStepEnum(d.pop("firstDocTypeTourStep"))

        pdt_self_service_tour_step = PdtSelfServiceTourStepEnum(d.pop("pdtSelfServiceTourStep"))

        cdt_self_service_tour_step = CdtSelfServiceTourStepEnum(d.pop("cdtSelfServiceTourStep"))

        training_a_custom_model_tour_step = TrainingACustomModelTourStepEnum(d.pop("trainingACustomModelTourStep"))

        _survey_response = d.pop("surveyResponse", UNSET)
        survey_response: Union[Unset, SurveyResponseDto]
        if isinstance(_survey_response, Unset):
            survey_response = UNSET
        else:
            survey_response = SurveyResponseDto.from_dict(_survey_response)

        user_tour_dto = cls(
            first_doc_type_tour_step=first_doc_type_tour_step,
            pdt_self_service_tour_step=pdt_self_service_tour_step,
            cdt_self_service_tour_step=cdt_self_service_tour_step,
            training_a_custom_model_tour_step=training_a_custom_model_tour_step,
            survey_response=survey_response,
        )

        user_tour_dto.additional_properties = d
        return user_tour_dto

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
