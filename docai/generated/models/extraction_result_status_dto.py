from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.doc_ex_confidence import DocExConfidence
from ..models.document_status import DocumentStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExtractionResultStatusDto")


@attr.s(auto_attribs=True)
class ExtractionResultStatusDto:
    """
    Attributes:
        document_id (str): ID of the document
        document_status (DocumentStatus):
        document_confidence (Union[Unset, DocExConfidence]):
    """

    document_id: str
    document_status: DocumentStatus
    document_confidence: Union[Unset, DocExConfidence] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        document_id = self.document_id
        document_status = self.document_status.value

        document_confidence: Union[Unset, str] = UNSET
        if not isinstance(self.document_confidence, Unset):
            document_confidence = self.document_confidence.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "documentId": document_id,
                "documentStatus": document_status,
            }
        )
        if document_confidence is not UNSET:
            field_dict["documentConfidence"] = document_confidence

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        document_id = d.pop("documentId")

        document_status = DocumentStatus(d.pop("documentStatus"))

        _document_confidence = d.pop("documentConfidence", UNSET)
        document_confidence: Union[Unset, DocExConfidence]
        if isinstance(_document_confidence, Unset):
            document_confidence = UNSET
        else:
            document_confidence = DocExConfidence(_document_confidence)

        extraction_result_status_dto = cls(
            document_id=document_id,
            document_status=document_status,
            document_confidence=document_confidence,
        )

        extraction_result_status_dto.additional_properties = d
        return extraction_result_status_dto

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
