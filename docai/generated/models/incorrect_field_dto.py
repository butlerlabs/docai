from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.doc_ex_field_type import DocExFieldType
from ..models.field_result_dto import FieldResultDto
from ..models.incorrect_status import IncorrectStatus

T = TypeVar("T", bound="IncorrectFieldDto")


@attr.s(auto_attribs=True)
class IncorrectFieldDto:
    """
    Attributes:
        id (str): ID of this incorrect field
        name (str): Name of this incorrect field
        display_name (str): Display name of this incorrect field used by the UI to tell the Butler Reviewer more about
            the field
        field_type (DocExFieldType):
        status (IncorrectStatus):
        butler_result (FieldResultDto):
        reviewer_result (FieldResultDto):
        customer_result (FieldResultDto):
    """

    id: str
    name: str
    display_name: str
    field_type: DocExFieldType
    status: IncorrectStatus
    butler_result: FieldResultDto
    reviewer_result: FieldResultDto
    customer_result: FieldResultDto
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        display_name = self.display_name
        field_type = self.field_type.value

        status = self.status.value

        butler_result = self.butler_result.to_dict()

        reviewer_result = self.reviewer_result.to_dict()

        customer_result = self.customer_result.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "displayName": display_name,
                "fieldType": field_type,
                "status": status,
                "butlerResult": butler_result,
                "reviewerResult": reviewer_result,
                "customerResult": customer_result,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        display_name = d.pop("displayName")

        field_type = DocExFieldType(d.pop("fieldType"))

        status = IncorrectStatus(d.pop("status"))

        butler_result = FieldResultDto.from_dict(d.pop("butlerResult"))

        reviewer_result = FieldResultDto.from_dict(d.pop("reviewerResult"))

        customer_result = FieldResultDto.from_dict(d.pop("customerResult"))

        incorrect_field_dto = cls(
            id=id,
            name=name,
            display_name=display_name,
            field_type=field_type,
            status=status,
            butler_result=butler_result,
            reviewer_result=reviewer_result,
            customer_result=customer_result,
        )

        incorrect_field_dto.additional_properties = d
        return incorrect_field_dto

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
