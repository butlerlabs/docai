from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.upload_document_response_dto import UploadDocumentResponseDto

T = TypeVar("T", bound="UploadDocumentsUploadResponseDto")


@attr.s(auto_attribs=True)
class UploadDocumentsUploadResponseDto:
    """
    Attributes:
        upload_id (str): The ID of the newly created upload.
        documents (List[UploadDocumentResponseDto]): An array of info about the documents uploaded.
    """

    upload_id: str
    documents: List[UploadDocumentResponseDto]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        upload_id = self.upload_id
        documents = []
        for documents_item_data in self.documents:
            documents_item = documents_item_data.to_dict()

            documents.append(documents_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uploadId": upload_id,
                "documents": documents,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        upload_id = d.pop("uploadId")

        documents = []
        _documents = d.pop("documents")
        for documents_item_data in _documents:
            documents_item = UploadDocumentResponseDto.from_dict(documents_item_data)

            documents.append(documents_item)

        upload_documents_upload_response_dto = cls(
            upload_id=upload_id,
            documents=documents,
        )

        upload_documents_upload_response_dto.additional_properties = d
        return upload_documents_upload_response_dto

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
