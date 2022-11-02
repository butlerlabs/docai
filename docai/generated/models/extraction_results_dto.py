from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.doc_ex_confidence import DocExConfidence
from ..models.document_status import DocumentStatus
from ..models.extra_results_dto import ExtraResultsDto
from ..models.extracted_field_dto import ExtractedFieldDto
from ..models.extracted_table_dto import ExtractedTableDto
from ..models.extraction_range_dto import ExtractionRangeDto
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExtractionResultsDto")


@attr.s(auto_attribs=True)
class ExtractionResultsDto:
    """
    Attributes:
        document_id (str): ID of the document
        document_status (DocumentStatus):
        file_name (str): Name of the uploaded file
        mime_type (str): Mime Type of the uploaded file
        document_type (str): Name of the document type
        confidence_score (Union[Unset, DocExConfidence]):
        extraction_range (Union[Unset, ExtractionRangeDto]):
        form_fields (Union[Unset, List[ExtractedFieldDto]]): Extracted form fields of this document. May be undefined if
            extraction not completed
        tables (Union[Unset, List[ExtractedTableDto]]): Extracted tables of this document. May be undefined if
            extraction not completed
        extra_results (Union[Unset, ExtraResultsDto]):
    """

    document_id: str
    document_status: DocumentStatus
    file_name: str
    mime_type: str
    document_type: str
    confidence_score: Union[Unset, DocExConfidence] = UNSET
    extraction_range: Union[Unset, ExtractionRangeDto] = UNSET
    form_fields: Union[Unset, List[ExtractedFieldDto]] = UNSET
    tables: Union[Unset, List[ExtractedTableDto]] = UNSET
    extra_results: Union[Unset, ExtraResultsDto] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        document_id = self.document_id
        document_status = self.document_status.value

        file_name = self.file_name
        mime_type = self.mime_type
        document_type = self.document_type
        confidence_score: Union[Unset, str] = UNSET
        if not isinstance(self.confidence_score, Unset):
            confidence_score = self.confidence_score.value

        extraction_range: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.extraction_range, Unset):
            extraction_range = self.extraction_range.to_dict()

        form_fields: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.form_fields, Unset):
            form_fields = []
            for form_fields_item_data in self.form_fields:
                form_fields_item = form_fields_item_data.to_dict()

                form_fields.append(form_fields_item)

        tables: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tables, Unset):
            tables = []
            for tables_item_data in self.tables:
                tables_item = tables_item_data.to_dict()

                tables.append(tables_item)

        extra_results: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.extra_results, Unset):
            extra_results = self.extra_results.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "documentId": document_id,
                "documentStatus": document_status,
                "fileName": file_name,
                "mimeType": mime_type,
                "documentType": document_type,
            }
        )
        if confidence_score is not UNSET:
            field_dict["confidenceScore"] = confidence_score
        if extraction_range is not UNSET:
            field_dict["extractionRange"] = extraction_range
        if form_fields is not UNSET:
            field_dict["formFields"] = form_fields
        if tables is not UNSET:
            field_dict["tables"] = tables
        if extra_results is not UNSET:
            field_dict["extraResults"] = extra_results

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        document_id = d.pop("documentId")

        document_status = DocumentStatus(d.pop("documentStatus"))

        file_name = d.pop("fileName")

        mime_type = d.pop("mimeType")

        document_type = d.pop("documentType")

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

        form_fields = []
        _form_fields = d.pop("formFields", UNSET)
        for form_fields_item_data in _form_fields or []:
            form_fields_item = ExtractedFieldDto.from_dict(form_fields_item_data)

            form_fields.append(form_fields_item)

        tables = []
        _tables = d.pop("tables", UNSET)
        for tables_item_data in _tables or []:
            tables_item = ExtractedTableDto.from_dict(tables_item_data)

            tables.append(tables_item)

        _extra_results = d.pop("extraResults", UNSET)
        extra_results: Union[Unset, ExtraResultsDto]
        if isinstance(_extra_results, Unset):
            extra_results = UNSET
        else:
            extra_results = ExtraResultsDto.from_dict(_extra_results)

        extraction_results_dto = cls(
            document_id=document_id,
            document_status=document_status,
            file_name=file_name,
            mime_type=mime_type,
            document_type=document_type,
            confidence_score=confidence_score,
            extraction_range=extraction_range,
            form_fields=form_fields,
            tables=tables,
            extra_results=extra_results,
        )

        extraction_results_dto.additional_properties = d
        return extraction_results_dto

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
