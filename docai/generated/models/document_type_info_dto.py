from typing import Any, Dict, List, Optional, Type, TypeVar

import attr

from ..models.base_model_type import BaseModelType
from ..models.model_status import ModelStatus
from ..models.training_document_details import TrainingDocumentDetails

T = TypeVar("T", bound="DocumentTypeInfoDto")


@attr.s(auto_attribs=True)
class DocumentTypeInfoDto:
    """
    Attributes:
        id (str): ID of this doctype
        name (str): Name of this doctype
        status (ModelStatus):
        model_type (BaseModelType):
        is_train_enabled (bool): If training is enabled for this specific Document Type
        training_document_details (Optional[TrainingDocumentDetails]):
    """

    id: str
    name: str
    status: ModelStatus
    model_type: BaseModelType
    is_train_enabled: bool
    training_document_details: Optional[TrainingDocumentDetails]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        status = self.status.value

        model_type = self.model_type.value

        is_train_enabled = self.is_train_enabled
        training_document_details = self.training_document_details.to_dict() if self.training_document_details else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "status": status,
                "modelType": model_type,
                "isTrainEnabled": is_train_enabled,
                "trainingDocumentDetails": training_document_details,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        status = ModelStatus(d.pop("status"))

        model_type = BaseModelType(d.pop("modelType"))

        is_train_enabled = d.pop("isTrainEnabled")

        _training_document_details = d.pop("trainingDocumentDetails")
        training_document_details: Optional[TrainingDocumentDetails]
        if _training_document_details is None:
            training_document_details = None
        else:
            training_document_details = TrainingDocumentDetails.from_dict(_training_document_details)

        document_type_info_dto = cls(
            id=id,
            name=name,
            status=status,
            model_type=model_type,
            is_train_enabled=is_train_enabled,
            training_document_details=training_document_details,
        )

        document_type_info_dto.additional_properties = d
        return document_type_info_dto

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
