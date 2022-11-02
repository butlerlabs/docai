from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.doc_ex_confidence import DocExConfidence
from ..models.extracted_field_dto import ExtractedFieldDto
from ..models.extracted_table_dto import ExtractedTableDto
from ..models.extraction_range_dto import ExtractionRangeDto
from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentExtractionResultsDto")


@attr.s(auto_attribs=True)
class DocumentExtractionResultsDto:
    """
    Attributes:
        id (str): ID of the document
        file_name (str):
        mime_type (str):
        document_type (str):
        extracted_fields (List[ExtractedFieldDto]):
        tables (List[ExtractedTableDto]):
        confidence_score (Union[Unset, DocExConfidence]):
        extraction_range (Union[Unset, ExtractionRangeDto]):
    """

    id: str
    file_name: str
    mime_type: str
    document_type: str
    extracted_fields: List[ExtractedFieldDto]
    tables: List[ExtractedTableDto]
    confidence_score: Union[Unset, DocExConfidence] = UNSET
    extraction_range: Union[Unset, ExtractionRangeDto] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        file_name = self.file_name
        mime_type = self.mime_type
        document_type = self.document_type
        extracted_fields = []
        for extracted_fields_item_data in self.extracted_fields:
            extracted_fields_item = extracted_fields_item_data.to_dict()

            extracted_fields.append(extracted_fields_item)

        tables = []
        for tables_item_data in self.tables:
            tables_item = tables_item_data.to_dict()

            tables.append(tables_item)

        confidence_score: Union[Unset, str] = UNSET
        if not isinstance(self.confidence_score, Unset):
            confidence_score = self.confidence_score.value

        extraction_range: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.extraction_range, Unset):
            extraction_range = self.extraction_range.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "fileName": file_name,
                "mimeType": mime_type,
                "documentType": document_type,
                "extractedFields": extracted_fields,
                "tables": tables,
            }
        )
        if confidence_score is not UNSET:
            field_dict["confidenceScore"] = confidence_score
        if extraction_range is not UNSET:
            field_dict["extractionRange"] = extraction_range

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        file_name = d.pop("fileName")

        mime_type = d.pop("mimeType")

        document_type = d.pop("documentType")

        extracted_fields = []
        _extracted_fields = d.pop("extractedFields")
        for extracted_fields_item_data in _extracted_fields:
            extracted_fields_item = ExtractedFieldDto.from_dict(extracted_fields_item_data)

            extracted_fields.append(extracted_fields_item)

        tables = []
        _tables = d.pop("tables")
        for tables_item_data in _tables:
            tables_item = ExtractedTableDto.from_dict(tables_item_data)

            tables.append(tables_item)

        _confidence_score = d.pop("confidenceScore", UNSET)
        confidence_score: Union[Unset, DocExConfidence]
        if isinstance(_confidence_score, Unset):
            confidence_score = UNSET
        else:
            confidence_score = DocExConfidence(_confidence_score)

        _extraction_range = d.pop("extractionRange", UNSET)
        extraction_range: Union[Unset, ExtractionRangeDto]
        if isinstance(_extraction_range, Unset):
            extraction_range = UNSET
        else:
            extraction_range = ExtractionRangeDto.from_dict(_extraction_range)

        document_extraction_results_dto = cls(
            id=id,
            file_name=file_name,
            mime_type=mime_type,
            document_type=document_type,
            extracted_fields=extracted_fields,
            tables=tables,
            confidence_score=confidence_score,
            extraction_range=extraction_range,
        )

        document_extraction_results_dto.additional_properties = d
        return document_extraction_results_dto

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
