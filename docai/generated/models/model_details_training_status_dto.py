from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.training_disabled_reason import TrainingDisabledReason
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelDetailsTrainingStatusDto")


@attr.s(auto_attribs=True)
class ModelDetailsTrainingStatusDto:
    """
    Attributes:
        num_documents_labeled (float): The number of documents labeled for this model
        num_documents_required_for_training (float): The number of documents that need to be labeled for training to be
            enabled
        training_disabled_reason (Union[Unset, TrainingDisabledReason]):
    """

    num_documents_labeled: float
    num_documents_required_for_training: float
    training_disabled_reason: Union[Unset, TrainingDisabledReason] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        num_documents_labeled = self.num_documents_labeled
        num_documents_required_for_training = self.num_documents_required_for_training
        training_disabled_reason: Union[Unset, str] = UNSET
        if not isinstance(self.training_disabled_reason, Unset):
            training_disabled_reason = self.training_disabled_reason.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "numDocumentsLabeled": num_documents_labeled,
                "numDocumentsRequiredForTraining": num_documents_required_for_training,
            }
        )
        if training_disabled_reason is not UNSET:
            field_dict["trainingDisabledReason"] = training_disabled_reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        num_documents_labeled = d.pop("numDocumentsLabeled")

        num_documents_required_for_training = d.pop("numDocumentsRequiredForTraining")

        _training_disabled_reason = d.pop("trainingDisabledReason", UNSET)
        training_disabled_reason: Union[Unset, TrainingDisabledReason]
        if isinstance(_training_disabled_reason, Unset):
            training_disabled_reason = UNSET
        else:
            training_disabled_reason = TrainingDisabledReason(_training_disabled_reason)

        model_details_training_status_dto = cls(
            num_documents_labeled=num_documents_labeled,
            num_documents_required_for_training=num_documents_required_for_training,
            training_disabled_reason=training_disabled_reason,
        )

        model_details_training_status_dto.additional_properties = d
        return model_details_training_status_dto

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
