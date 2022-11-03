from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.cdt_self_service_tour_step_enum import CdtSelfServiceTourStepEnum
from ..models.create_first_doc_type_step_enum import CreateFirstDocTypeStepEnum
from ..models.pdt_self_service_tour_step_enum import PdtSelfServiceTourStepEnum
from ..models.training_a_custom_model_tour_step_enum import TrainingACustomModelTourStepEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserTourPatchDto")


@attr.s(auto_attribs=True)
class UserTourPatchDto:
    """
    Attributes:
        first_doc_type_tour_step (Union[Unset, CreateFirstDocTypeStepEnum]):
        pdt_self_service_tour_step (Union[Unset, PdtSelfServiceTourStepEnum]):
        cdt_self_service_tour_step (Union[Unset, CdtSelfServiceTourStepEnum]):
        training_a_custom_model_tour_step (Union[Unset, TrainingACustomModelTourStepEnum]):
    """

    first_doc_type_tour_step: Union[Unset, CreateFirstDocTypeStepEnum] = UNSET
    pdt_self_service_tour_step: Union[Unset, PdtSelfServiceTourStepEnum] = UNSET
    cdt_self_service_tour_step: Union[Unset, CdtSelfServiceTourStepEnum] = UNSET
    training_a_custom_model_tour_step: Union[Unset, TrainingACustomModelTourStepEnum] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        first_doc_type_tour_step: Union[Unset, str] = UNSET
        if not isinstance(self.first_doc_type_tour_step, Unset):
            first_doc_type_tour_step = self.first_doc_type_tour_step.value

        pdt_self_service_tour_step: Union[Unset, str] = UNSET
        if not isinstance(self.pdt_self_service_tour_step, Unset):
            pdt_self_service_tour_step = self.pdt_self_service_tour_step.value

        cdt_self_service_tour_step: Union[Unset, str] = UNSET
        if not isinstance(self.cdt_self_service_tour_step, Unset):
            cdt_self_service_tour_step = self.cdt_self_service_tour_step.value

        training_a_custom_model_tour_step: Union[Unset, str] = UNSET
        if not isinstance(self.training_a_custom_model_tour_step, Unset):
            training_a_custom_model_tour_step = self.training_a_custom_model_tour_step.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_doc_type_tour_step is not UNSET:
            field_dict["firstDocTypeTourStep"] = first_doc_type_tour_step
        if pdt_self_service_tour_step is not UNSET:
            field_dict["pdtSelfServiceTourStep"] = pdt_self_service_tour_step
        if cdt_self_service_tour_step is not UNSET:
            field_dict["cdtSelfServiceTourStep"] = cdt_self_service_tour_step
        if training_a_custom_model_tour_step is not UNSET:
            field_dict["trainingACustomModelTourStep"] = training_a_custom_model_tour_step

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _first_doc_type_tour_step = d.pop("firstDocTypeTourStep", UNSET)
        first_doc_type_tour_step: Union[Unset, CreateFirstDocTypeStepEnum]
        if isinstance(_first_doc_type_tour_step, Unset):
            first_doc_type_tour_step = UNSET
        else:
            first_doc_type_tour_step = CreateFirstDocTypeStepEnum(_first_doc_type_tour_step)

        _pdt_self_service_tour_step = d.pop("pdtSelfServiceTourStep", UNSET)
        pdt_self_service_tour_step: Union[Unset, PdtSelfServiceTourStepEnum]
        if isinstance(_pdt_self_service_tour_step, Unset):
            pdt_self_service_tour_step = UNSET
        else:
            pdt_self_service_tour_step = PdtSelfServiceTourStepEnum(_pdt_self_service_tour_step)

        _cdt_self_service_tour_step = d.pop("cdtSelfServiceTourStep", UNSET)
        cdt_self_service_tour_step: Union[Unset, CdtSelfServiceTourStepEnum]
        if isinstance(_cdt_self_service_tour_step, Unset):
            cdt_self_service_tour_step = UNSET
        else:
            cdt_self_service_tour_step = CdtSelfServiceTourStepEnum(_cdt_self_service_tour_step)

        _training_a_custom_model_tour_step = d.pop("trainingACustomModelTourStep", UNSET)
        training_a_custom_model_tour_step: Union[Unset, TrainingACustomModelTourStepEnum]
        if isinstance(_training_a_custom_model_tour_step, Unset):
            training_a_custom_model_tour_step = UNSET
        else:
            training_a_custom_model_tour_step = TrainingACustomModelTourStepEnum(_training_a_custom_model_tour_step)

        user_tour_patch_dto = cls(
            first_doc_type_tour_step=first_doc_type_tour_step,
            pdt_self_service_tour_step=pdt_self_service_tour_step,
            cdt_self_service_tour_step=cdt_self_service_tour_step,
            training_a_custom_model_tour_step=training_a_custom_model_tour_step,
        )

        user_tour_patch_dto.additional_properties = d
        return user_tour_patch_dto

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
