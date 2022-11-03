from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.training_document_type_status import TrainingDocumentTypeStatus

T = TypeVar("T", bound="TrainingDocumentDetails")


@attr.s(auto_attribs=True)
class TrainingDocumentDetails:
    """
    Attributes:
        documents_required_for_training (float): Number of documents required to label before training is enabled
        documents_reviewed (float): Number of documents the user has reviewed for training
        total_training_documents (float): Total number of training documents that the user has uploaded
        status (TrainingDocumentTypeStatus):
    """

    documents_required_for_training: float
    documents_reviewed: float
    total_training_documents: float
    status: TrainingDocumentTypeStatus
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        documents_required_for_training = self.documents_required_for_training
        documents_reviewed = self.documents_reviewed
        total_training_documents = self.total_training_documents
        status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "documentsRequiredForTraining": documents_required_for_training,
                "documentsReviewed": documents_reviewed,
                "totalTrainingDocuments": total_training_documents,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        documents_required_for_training = d.pop("documentsRequiredForTraining")

        documents_reviewed = d.pop("documentsReviewed")

        total_training_documents = d.pop("totalTrainingDocuments")

        status = TrainingDocumentTypeStatus(d.pop("status"))

        training_document_details = cls(
            documents_required_for_training=documents_required_for_training,
            documents_reviewed=documents_reviewed,
            total_training_documents=total_training_documents,
            status=status,
        )

        training_document_details.additional_properties = d
        return training_document_details

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
