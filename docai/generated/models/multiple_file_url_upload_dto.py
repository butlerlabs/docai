from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.url_upload_dto import UrlUploadDto

T = TypeVar("T", bound="MultipleFileUrlUploadDto")


@attr.s(auto_attribs=True)
class MultipleFileUrlUploadDto:
    """
    Attributes:
        files (List[UrlUploadDto]): List of files to upload
    """

    files: List[UrlUploadDto]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        files = []
        for files_item_data in self.files:
            files_item = files_item_data.to_dict()

            files.append(files_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "files": files,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        files = []
        _files = d.pop("files")
        for files_item_data in _files:
            files_item = UrlUploadDto.from_dict(files_item_data)

            files.append(files_item)

        multiple_file_url_upload_dto = cls(
            files=files,
        )

        multiple_file_url_upload_dto.additional_properties = d
        return multiple_file_url_upload_dto

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
