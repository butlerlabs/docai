from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.base_model_type import BaseModelType
from ..models.model_field_dto import ModelFieldDto
from ..models.model_status import ModelStatus
from ..models.model_table_dto import ModelTableDto
from ..models.submit_training_documents_disabled_reason import SubmitTrainingDocumentsDisabledReason
from ..models.training_disabled_reason import TrainingDisabledReason
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelInfoDto")


@attr.s(auto_attribs=True)
class ModelInfoDto:
    """
    Attributes:
        id (str): The unique id of this model.
        name (str): Name of the model.
        status (ModelStatus):
        model_type (BaseModelType):
        fields (List[ModelFieldDto]): The text, checkbox, and signature fields for this model
        tables (List[ModelTableDto]): The table fields for this model
        queue_id (str): The id of the queue for this model.
        num_training_documents (float): The number of training documents for this model
        training_disabled_reason (Union[Unset, TrainingDisabledReason]):
        training_failure_reason (Union[Unset, str]): Reason for previous training failure
        submit_training_documents_disabled_reason (Union[Unset, SubmitTrainingDocumentsDisabledReason]):
    """

    id: str
    name: str
    status: ModelStatus
    model_type: BaseModelType
    fields: List[ModelFieldDto]
    tables: List[ModelTableDto]
    queue_id: str
    num_training_documents: float
    training_disabled_reason: Union[Unset, TrainingDisabledReason] = UNSET
    training_failure_reason: Union[Unset, str] = UNSET
    submit_training_documents_disabled_reason: Union[Unset, SubmitTrainingDocumentsDisabledReason] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        status = self.status.value

        model_type = self.model_type.value

        fields = []
        for fields_item_data in self.fields:
            fields_item = fields_item_data.to_dict()

            fields.append(fields_item)

        tables = []
        for tables_item_data in self.tables:
            tables_item = tables_item_data.to_dict()

            tables.append(tables_item)

        queue_id = self.queue_id
        num_training_documents = self.num_training_documents
        training_disabled_reason: Union[Unset, str] = UNSET
        if not isinstance(self.training_disabled_reason, Unset):
            training_disabled_reason = self.training_disabled_reason.value

        training_failure_reason = self.training_failure_reason
        submit_training_documents_disabled_reason: Union[Unset, str] = UNSET
        if not isinstance(self.submit_training_documents_disabled_reason, Unset):
            submit_training_documents_disabled_reason = self.submit_training_documents_disabled_reason.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "status": status,
                "modelType": model_type,
                "fields": fields,
                "tables": tables,
                "queueId": queue_id,
                "numTrainingDocuments": num_training_documents,
            }
        )
        if training_disabled_reason is not UNSET:
            field_dict["trainingDisabledReason"] = training_disabled_reason
        if training_failure_reason is not UNSET:
            field_dict["trainingFailureReason"] = training_failure_reason
        if submit_training_documents_disabled_reason is not UNSET:
            field_dict["submitTrainingDocumentsDisabledReason"] = submit_training_documents_disabled_reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        status = ModelStatus(d.pop("status"))

        model_type = BaseModelType(d.pop("modelType"))

        fields = []
        _fields = d.pop("fields")
        for fields_item_data in _fields:
            fields_item = ModelFieldDto.from_dict(fields_item_data)

            fields.append(fields_item)

        tables = []
        _tables = d.pop("tables")
        for tables_item_data in _tables:
            tables_item = ModelTableDto.from_dict(tables_item_data)

            tables.append(tables_item)

        queue_id = d.pop("queueId")

        num_training_documents = d.pop("numTrainingDocuments")

        _training_disabled_reason = d.pop("trainingDisabledReason", UNSET)
        training_disabled_reason: Union[Unset, TrainingDisabledReason]
        if isinstance(_training_disabled_reason, Unset):
            training_disabled_reason = UNSET
        else:
            training_disabled_reason = TrainingDisabledReason(_training_disabled_reason)

        training_failure_reason = d.pop("trainingFailureReason", UNSET)

        _submit_training_documents_disabled_reason = d.pop("submitTrainingDocumentsDisabledReason", UNSET)
        submit_training_documents_disabled_reason: Union[Unset, SubmitTrainingDocumentsDisabledReason]
        if isinstance(_submit_training_documents_disabled_reason, Unset):
            submit_training_documents_disabled_reason = UNSET
        else:
            submit_training_documents_disabled_reason = SubmitTrainingDocumentsDisabledReason(
                _submit_training_documents_disabled_reason
            )

        model_info_dto = cls(
            id=id,
            name=name,
            status=status,
            model_type=model_type,
            fields=fields,
            tables=tables,
            queue_id=queue_id,
            num_training_documents=num_training_documents,
            training_disabled_reason=training_disabled_reason,
            training_failure_reason=training_failure_reason,
            submit_training_documents_disabled_reason=submit_training_documents_disabled_reason,
        )

        model_info_dto.additional_properties = d
        return model_info_dto

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
