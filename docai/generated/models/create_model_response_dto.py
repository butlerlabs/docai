from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CreateModelResponseDto")


@attr.s(auto_attribs=True)
class CreateModelResponseDto:
    """
    Attributes:
        model_id (str): the id of the generated model
    """

    model_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        model_id = self.model_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "modelId": model_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        model_id = d.pop("modelId")

        create_model_response_dto = cls(
            model_id=model_id,
        )

        create_model_response_dto.additional_properties = d
        return create_model_response_dto

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
