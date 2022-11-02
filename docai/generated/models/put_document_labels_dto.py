from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.signature_field_with_confidence_labeled_result_dto import SignatureFieldWithConfidenceLabeledResultDto
from ..models.simple_field_with_confidence_labeled_result_dto import SimpleFieldWithConfidenceLabeledResultDto
from ..models.training_table_with_confidence_labeled_result_dto import TrainingTableWithConfidenceLabeledResultDto
from ..types import UNSET, Unset

T = TypeVar("T", bound="PutDocumentLabelsDto")


@attr.s(auto_attribs=True)
class PutDocumentLabelsDto:
    """
    Attributes:
        fields (List[SimpleFieldWithConfidenceLabeledResultDto]): The text and checkbox fields for this document
        signatures (List[SignatureFieldWithConfidenceLabeledResultDto]): The signature fields for this document
        tables (List[TrainingTableWithConfidenceLabeledResultDto]): The table fields for this document
        overwrite (Union[Unset, bool]): Overwrite existing labels if present. Default is true.
    """

    fields: List[SimpleFieldWithConfidenceLabeledResultDto]
    signatures: List[SignatureFieldWithConfidenceLabeledResultDto]
    tables: List[TrainingTableWithConfidenceLabeledResultDto]
    overwrite: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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

        overwrite = self.overwrite

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fields": fields,
                "signatures": signatures,
                "tables": tables,
            }
        )
        if overwrite is not UNSET:
            field_dict["overwrite"] = overwrite

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        fields = []
        _fields = d.pop("fields")
        for fields_item_data in _fields:
            fields_item = SimpleFieldWithConfidenceLabeledResultDto.from_dict(fields_item_data)

            fields.append(fields_item)

        signatures = []
        _signatures = d.pop("signatures")
        for signatures_item_data in _signatures:
            signatures_item = SignatureFieldWithConfidenceLabeledResultDto.from_dict(signatures_item_data)

            signatures.append(signatures_item)

        tables = []
        _tables = d.pop("tables")
        for tables_item_data in _tables:
            tables_item = TrainingTableWithConfidenceLabeledResultDto.from_dict(tables_item_data)

            tables.append(tables_item)

        overwrite = d.pop("overwrite", UNSET)

        put_document_labels_dto = cls(
            fields=fields,
            signatures=signatures,
            tables=tables,
            overwrite=overwrite,
        )

        put_document_labels_dto.additional_properties = d
        return put_document_labels_dto

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
