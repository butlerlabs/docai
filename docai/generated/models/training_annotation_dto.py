from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.signature_field_labeled_result_dto import SignatureFieldLabeledResultDto
from ..models.simple_field_labeled_result_dto import SimpleFieldLabeledResultDto
from ..models.training_table_labeled_result_dto import TrainingTableLabeledResultDto

T = TypeVar("T", bound="TrainingAnnotationDto")


@attr.s(auto_attribs=True)
class TrainingAnnotationDto:
    """
    Attributes:
        fields (List[SimpleFieldLabeledResultDto]): The text and checkbox fields annotated for this document
        signatures (List[SignatureFieldLabeledResultDto]): The signature fields annotated for this document
        tables (List[TrainingTableLabeledResultDto]): The table fields annotated for this document
    """

    fields: List[SimpleFieldLabeledResultDto]
    signatures: List[SignatureFieldLabeledResultDto]
    tables: List[TrainingTableLabeledResultDto]
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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fields": fields,
                "signatures": signatures,
                "tables": tables,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
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

        training_annotation_dto = cls(
            fields=fields,
            signatures=signatures,
            tables=tables,
        )

        training_annotation_dto.additional_properties = d
        return training_annotation_dto

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
