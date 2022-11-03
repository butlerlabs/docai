from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="StaticTrainingDocumentSummaryDto")


@attr.s(auto_attribs=True)
class StaticTrainingDocumentSummaryDto:
    """
    Attributes:
        document_id (str): The unique id of the document this signedUrl is for.
        file_name (str): The file name of this document
        thumbnail_signed_url (str): The signed url that the thumbnail file can be downloaded from.
    """

    document_id: str
    file_name: str
    thumbnail_signed_url: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        document_id = self.document_id
        file_name = self.file_name
        thumbnail_signed_url = self.thumbnail_signed_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "documentId": document_id,
                "fileName": file_name,
                "thumbnailSignedUrl": thumbnail_signed_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        document_id = d.pop("documentId")

        file_name = d.pop("fileName")

        thumbnail_signed_url = d.pop("thumbnailSignedUrl")

        static_training_document_summary_dto = cls(
            document_id=document_id,
            file_name=file_name,
            thumbnail_signed_url=thumbnail_signed_url,
        )

        static_training_document_summary_dto.additional_properties = d
        return static_training_document_summary_dto

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
