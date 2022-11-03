from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.signature_field_labeled_result_dto import SignatureFieldLabeledResultDto
from ..models.simple_field_labeled_result_dto import SimpleFieldLabeledResultDto
from ..models.training_table_labeled_result_dto import TrainingTableLabeledResultDto

T = TypeVar("T", bound="TrainingDocumentDetailsDto")


@attr.s(auto_attribs=True)
class TrainingDocumentDetailsDto:
    """
    Attributes:
        document_id (str): The unique id of the document.
        label_update_count (float): The number of times the labels have been updated for this document
        fields (List[SimpleFieldLabeledResultDto]): The text and checkbox fields for this document
        signatures (List[SignatureFieldLabeledResultDto]): The signature fields for this document
        tables (List[TrainingTableLabeledResultDto]): The table fields for this document
    """

    document_id: str
    label_update_count: float
    fields: List[SimpleFieldLabeledResultDto]
    signatures: List[SignatureFieldLabeledResultDto]
    tables: List[TrainingTableLabeledResultDto]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        document_id = self.document_id
        label_update_count = self.label_update_count
        fields = []
        for fields_item_data in self.fields:
            fields_item = fields_item_data.to_dict()

            fields.append(fields_item)

        signatures = []
        for signatures_item_data in self.signatures:
            signatures_item = signatures_item_data.to_dict()

            signatures.append(signatures_item)

        tables = []
        for tables_item_data in self.tables:
            tables_item = tables_item_data.to_dict()

            tables.append(tables_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "documentId": document_id,
                "labelUpdateCount": label_update_count,
                "fields": fields,
                "signatures": signatures,
                "tables": tables,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        document_id = d.pop("documentId")

        label_update_count = d.pop("labelUpdateCount")

        fields = []
        _fields = d.pop("fields")
        for fields_item_data in _fields:
            fields_item = SimpleFieldLabeledResultDto.from_dict(fields_item_data)

            fields.append(fields_item)

        signatures = []
        _signatures = d.pop("signatures")
        for signatures_item_data in _signatures:
            signatures_item = SignatureFieldLabeledResultDto.from_dict(signatures_item_data)

            signatures.append(signatures_item)

        tables = []
        _tables = d.pop("tables")
        for tables_item_data in _tables:
            tables_item = TrainingTableLabeledResultDto.from_dict(tables_item_data)

            tables.append(tables_item)

        training_document_details_dto = cls(
            document_id=document_id,
            label_update_count=label_update_count,
            fields=fields,
            signatures=signatures,
            tables=tables,
        )

        training_document_details_dto.additional_properties = d
        return training_document_details_dto

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
