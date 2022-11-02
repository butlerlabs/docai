from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.model_training_document_status import ModelTrainingDocumentStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="TrainingDocumentSummaryDto")


@attr.s(auto_attribs=True)
class TrainingDocumentSummaryDto:
    """
    Attributes:
        document_id (str): The unique id of the document.
        status (ModelTrainingDocumentStatus):
        size (float): The estimated size of the training document, includes the document and its OCR results
        failure_reason (Union[Unset, str]): Reason for why the document failed
    """

    document_id: str
    status: ModelTrainingDocumentStatus
    size: float
    failure_reason: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        document_id = self.document_id
        status = self.status.value

        size = self.size
        failure_reason = self.failure_reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "documentId": document_id,
                "status": status,
                "size": size,
            }
        )
        if failure_reason is not UNSET:
            field_dict["failureReason"] = failure_reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        document_id = d.pop("documentId")

        status = ModelTrainingDocumentStatus(d.pop("status"))

        size = d.pop("size")

        failure_reason = d.pop("failureReason", UNSET)

        training_document_summary_dto = cls(
            document_id=document_id,
            status=status,
            size=size,
            failure_reason=failure_reason,
        )

        training_document_summary_dto.additional_properties = d
        return training_document_summary_dto

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
