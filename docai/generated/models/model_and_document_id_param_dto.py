from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ModelAndDocumentIdParamDto")


@attr.s(auto_attribs=True)
class ModelAndDocumentIdParamDto:
    """
    Attributes:
        id (str): The ID of the model.
        document_id (str): The ID of the document.
    """

    id: str
    document_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        document_id = self.document_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "documentId": document_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        document_id = d.pop("documentId")

        model_and_document_id_param_dto = cls(
            id=id,
            document_id=document_id,
        )

        model_and_document_id_param_dto.additional_properties = d
        return model_and_document_id_param_dto

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
