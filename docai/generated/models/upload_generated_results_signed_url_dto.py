from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="UploadGeneratedResultsSignedUrlDto")


@attr.s(auto_attribs=True)
class UploadGeneratedResultsSignedUrlDto:
    """
    Attributes:
        url (str): Signed url to download the file
        mime_type (str): Mime type of the file
    """

    url: str
    mime_type: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        mime_type = self.mime_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "mimeType": mime_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        mime_type = d.pop("mimeType")

        upload_generated_results_signed_url_dto = cls(
            url=url,
            mime_type=mime_type,
        )

        upload_generated_results_signed_url_dto.additional_properties = d
        return upload_generated_results_signed_url_dto

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
