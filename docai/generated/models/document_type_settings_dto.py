from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="DocumentTypeSettingsDto")


@attr.s(auto_attribs=True)
class DocumentTypeSettingsDto:
    """
    Attributes:
        butler_ops_enabled (bool): Whether or not butler ops is enabled for training this Document Type
    """

    butler_ops_enabled: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        butler_ops_enabled = self.butler_ops_enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "butlerOpsEnabled": butler_ops_enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        butler_ops_enabled = d.pop("butlerOpsEnabled")

        document_type_settings_dto = cls(
            butler_ops_enabled=butler_ops_enabled,
        )

        document_type_settings_dto.additional_properties = d
        return document_type_settings_dto

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
