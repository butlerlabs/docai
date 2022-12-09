from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PredictionDocumentSummaryDto")


@attr.s(auto_attribs=True)
class PredictionDocumentSummaryDto:
    """
    Attributes:
        document_id (str): The ID of the document.
        file_name (str): The file name of this document.
        mime_type (str): The mime type of the document.
        created_at (str): The UTC ISO-8601 timestamp of when the document was uploaded.
        num_pages (float): Number of pages in the document.
    """

    document_id: str
    file_name: str
    mime_type: str
    created_at: str
    num_pages: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        document_id = self.document_id
        file_name = self.file_name
        mime_type = self.mime_type
        created_at = self.created_at
        num_pages = self.num_pages

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "documentId": document_id,
                "fileName": file_name,
                "mimeType": mime_type,
                "createdAt": created_at,
                "numPages": num_pages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        document_id = d.pop("documentId")

        file_name = d.pop("fileName")

        mime_type = d.pop("mimeType")

        created_at = d.pop("createdAt")

        num_pages = d.pop("numPages")

        prediction_document_summary_dto = cls(
            document_id=document_id,
            file_name=file_name,
            mime_type=mime_type,
            created_at=created_at,
            num_pages=num_pages,
        )

        prediction_document_summary_dto.additional_properties = d
        return prediction_document_summary_dto

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
