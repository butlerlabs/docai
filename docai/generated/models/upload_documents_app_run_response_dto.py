from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.upload_document_response_dto import UploadDocumentResponseDto

T = TypeVar("T", bound="UploadDocumentsAppRunResponseDto")


@attr.s(auto_attribs=True)
class UploadDocumentsAppRunResponseDto:
    """
    Attributes:
        app_run_id (str):
        documents (List[UploadDocumentResponseDto]):
    """

    app_run_id: str
    documents: List[UploadDocumentResponseDto]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        app_run_id = self.app_run_id
        documents = []
        for documents_item_data in self.documents:
            documents_item = documents_item_data.to_dict()

            documents.append(documents_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "appRunId": app_run_id,
                "documents": documents,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        app_run_id = d.pop("appRunId")

        documents = []
        _documents = d.pop("documents")
        for documents_item_data in _documents:
            documents_item = UploadDocumentResponseDto.from_dict(documents_item_data)

            documents.append(documents_item)

        upload_documents_app_run_response_dto = cls(
            app_run_id=app_run_id,
            documents=documents,
        )

        upload_documents_app_run_response_dto.additional_properties = d
        return upload_documents_app_run_response_dto

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
