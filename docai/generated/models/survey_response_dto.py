from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="SurveyResponseDto")


@attr.s(auto_attribs=True)
class SurveyResponseDto:
    """
    Attributes:
        user_role (str): The Users Role
        document_types (List[str]): The types of documents the user would like to process
        number_pages (str): The number of pages the user would like to process
    """

    user_role: str
    document_types: List[str]
    number_pages: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_role = self.user_role
        document_types = self.document_types

        number_pages = self.number_pages

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userRole": user_role,
                "documentTypes": document_types,
                "numberPages": number_pages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_role = d.pop("userRole")

        document_types = cast(List[str], d.pop("documentTypes"))

        number_pages = d.pop("numberPages")

        survey_response_dto = cls(
            user_role=user_role,
            document_types=document_types,
            number_pages=number_pages,
        )

        survey_response_dto.additional_properties = d
        return survey_response_dto

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
