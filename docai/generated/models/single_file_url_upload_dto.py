from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.url_upload_dto import UrlUploadDto

T = TypeVar("T", bound="SingleFileUrlUploadDto")


@attr.s(auto_attribs=True)
class SingleFileUrlUploadDto:
    """
    Attributes:
        file (UrlUploadDto):
    """

    file: UrlUploadDto
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        file = self.file.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        file = UrlUploadDto.from_dict(d.pop("file"))

        single_file_url_upload_dto = cls(
            file=file,
        )

        single_file_url_upload_dto.additional_properties = d
        return single_file_url_upload_dto

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
