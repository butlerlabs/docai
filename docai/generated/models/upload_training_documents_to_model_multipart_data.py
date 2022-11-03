import json
from io import BytesIO
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="UploadTrainingDocumentsToModelMultipartData")


@attr.s(auto_attribs=True)
class UploadTrainingDocumentsToModelMultipartData:
    """
    Attributes:
        files (Union[Unset, List[File]]):
    """

    files: Union[Unset, List[File]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        files: Union[Unset, List[FileJsonType]] = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_tuple()

                files.append(files_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if files is not UNSET:
            field_dict["files"] = files

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        files: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.files, Unset):
            _temp_files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_tuple()

                _temp_files.append(files_item)
            files = (None, json.dumps(_temp_files).encode(), "application/json")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if files is not UNSET:
            field_dict["files"] = files

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        files = []
        _files = d.pop("files", UNSET)
        for files_item_data in _files or []:
            files_item = File(payload=BytesIO(files_item_data))

            files.append(files_item)

        upload_training_documents_to_model_multipart_data = cls(
            files=files,
        )

        upload_training_documents_to_model_multipart_data.additional_properties = d
        return upload_training_documents_to_model_multipart_data

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
