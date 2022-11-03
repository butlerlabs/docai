from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.upload_generated_results_signed_url_dto import UploadGeneratedResultsSignedUrlDto
from ..types import UNSET, Unset

T = TypeVar("T", bound="UploadGeneratedResultsDto")


@attr.s(auto_attribs=True)
class UploadGeneratedResultsDto:
    """
    Attributes:
        id (str): Upload Id
        csv_result (UploadGeneratedResultsSignedUrlDto):
        xls_result (Union[Unset, UploadGeneratedResultsSignedUrlDto]):
    """

    id: str
    csv_result: UploadGeneratedResultsSignedUrlDto
    xls_result: Union[Unset, UploadGeneratedResultsSignedUrlDto] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        csv_result = self.csv_result.to_dict()

        xls_result: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.xls_result, Unset):
            xls_result = self.xls_result.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "csvResult": csv_result,
            }
        )
        if xls_result is not UNSET:
            field_dict["xlsResult"] = xls_result

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        csv_result = UploadGeneratedResultsSignedUrlDto.from_dict(d.pop("csvResult"))

        _xls_result = d.pop("xlsResult", UNSET)
        xls_result: Union[Unset, UploadGeneratedResultsSignedUrlDto]
        if isinstance(_xls_result, Unset):
            xls_result = UNSET
        else:
            xls_result = UploadGeneratedResultsSignedUrlDto.from_dict(_xls_result)

        upload_generated_results_dto = cls(
            id=id,
            csv_result=csv_result,
            xls_result=xls_result,
        )

        upload_generated_results_dto.additional_properties = d
        return upload_generated_results_dto

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
