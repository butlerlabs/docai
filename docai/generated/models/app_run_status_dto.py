from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.app_run_status import AppRunStatus

T = TypeVar("T", bound="AppRunStatusDto")


@attr.s(auto_attribs=True)
class AppRunStatusDto:
    """
    Attributes:
        app_run_id (str):
        status (AppRunStatus):
    """

    app_run_id: str
    status: AppRunStatus
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        app_run_id = self.app_run_id
        status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "appRunId": app_run_id,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        app_run_id = d.pop("appRunId")

        status = AppRunStatus(d.pop("status"))

        app_run_status_dto = cls(
            app_run_id=app_run_id,
            status=status,
        )

        app_run_status_dto.additional_properties = d
        return app_run_status_dto

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
