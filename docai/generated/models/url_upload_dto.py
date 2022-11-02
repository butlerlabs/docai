from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UrlUploadDto")


@attr.s(auto_attribs=True)
class UrlUploadDto:
    """
    Attributes:
        url (str): URL to download the file from using a GET request
        file_name (Union[Unset, str]): Filename to save for the file. If empty, will use the final portion of the URL
            path
        mime_type (Union[Unset, str]): Mime type of file. If empty, will use the response content type of the download
    """

    url: str
    file_name: Union[Unset, str] = UNSET
    mime_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        file_name = self.file_name
        mime_type = self.mime_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        file_name = d.pop("fileName", UNSET)

        mime_type = d.pop("mimeType", UNSET)

        url_upload_dto = cls(
            url=url,
            file_name=file_name,
            mime_type=mime_type,
        )

        url_upload_dto.additional_properties = d
        return url_upload_dto

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
