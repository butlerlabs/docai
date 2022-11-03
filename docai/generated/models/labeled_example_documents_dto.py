from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="LabeledExampleDocumentsDto")


@attr.s(auto_attribs=True)
class LabeledExampleDocumentsDto:
    """
    Attributes:
        example_document_ids (List[str]): A list of labeled example document ids
    """

    example_document_ids: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        example_document_ids = self.example_document_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "exampleDocumentIds": example_document_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        example_document_ids = cast(List[str], d.pop("exampleDocumentIds"))

        labeled_example_documents_dto = cls(
            example_document_ids=example_document_ids,
        )

        labeled_example_documents_dto.additional_properties = d
        return labeled_example_documents_dto

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
