from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.ml_inference_status_enum import MlInferenceStatusEnum

T = TypeVar("T", bound="ImageClassificationResultDto")


@attr.s(auto_attribs=True)
class ImageClassificationResultDto:
    """
    Attributes:
        request_id (str): The id of the image classification request
        file_name (str): The file name of the uploaded image
        uri (str): The uri of the uploaded image
        label (str): The result of the image classification request
        status (MlInferenceStatusEnum):
    """

    request_id: str
    file_name: str
    uri: str
    label: str
    status: MlInferenceStatusEnum
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        request_id = self.request_id
        file_name = self.file_name
        uri = self.uri
        label = self.label
        status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requestId": request_id,
                "fileName": file_name,
                "uri": uri,
                "label": label,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        request_id = d.pop("requestId")

        file_name = d.pop("fileName")

        uri = d.pop("uri")

        label = d.pop("label")

        status = MlInferenceStatusEnum(d.pop("status"))

        image_classification_result_dto = cls(
            request_id=request_id,
            file_name=file_name,
            uri=uri,
            label=label,
            status=status,
        )

        image_classification_result_dto.additional_properties = d
        return image_classification_result_dto

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
