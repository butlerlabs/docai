from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ReviewerDto")


@attr.s(auto_attribs=True)
class ReviewerDto:
    """
    Attributes:
        id (str): ID of this reviewer
        email_address (str): Email of this reviewer
    """

    id: str
    email_address: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        email_address = self.email_address

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "emailAddress": email_address,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        email_address = d.pop("emailAddress")

        reviewer_dto = cls(
            id=id,
            email_address=email_address,
        )

        reviewer_dto.additional_properties = d
        return reviewer_dto

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
