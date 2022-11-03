from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.base_model_type import BaseModelType
from ..models.model_status import ModelStatus

T = TypeVar("T", bound="DocumentTypeSummaryDto")


@attr.s(auto_attribs=True)
class DocumentTypeSummaryDto:
    """
    Attributes:
        id (str): ID of this doctype
        name (str): Name of this doctype
        status (ModelStatus):
        model_type (BaseModelType):
    """

    id: str
    name: str
    status: ModelStatus
    model_type: BaseModelType
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        status = self.status.value

        model_type = self.model_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "status": status,
                "modelType": model_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        status = ModelStatus(d.pop("status"))

        model_type = BaseModelType(d.pop("modelType"))

        document_type_summary_dto = cls(
            id=id,
            name=name,
            status=status,
            model_type=model_type,
        )

        document_type_summary_dto.additional_properties = d
        return document_type_summary_dto

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
