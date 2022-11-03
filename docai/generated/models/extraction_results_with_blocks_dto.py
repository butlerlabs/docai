from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.block_result_dto import BlockResultDto
from ..models.deprecated_extracted_table_with_blocks_dto import DeprecatedExtractedTableWithBlocksDto
from ..models.doc_ex_confidence import DocExConfidence
from ..models.extracted_form_fields_with_blocks_dto import ExtractedFormFieldsWithBlocksDto

T = TypeVar("T", bound="ExtractionResultsWithBlocksDto")


@attr.s(auto_attribs=True)
class ExtractionResultsWithBlocksDto:
    """
    Attributes:
        id (str): Id of the extracted document
        file_name (str): Name of the file that these results were extracted from
        doc_uri (str): Identifier for the hosted document that the results were extracted from
        mime_type (str): The type of document that the results were extracted from
        word_blocks (List[BlockResultDto]): Word Blocks extracted from the document, with associated blocks
        form_fields (List[ExtractedFormFieldsWithBlocksDto]): Form Fields extracted from the document, with associated
            blocks
        tables (List[DeprecatedExtractedTableWithBlocksDto]): Tables extracted from the document, with associated blocks
        confidence_score (DocExConfidence):
    """

    id: str
    file_name: str
    doc_uri: str
    mime_type: str
    word_blocks: List[BlockResultDto]
    form_fields: List[ExtractedFormFieldsWithBlocksDto]
    tables: List[DeprecatedExtractedTableWithBlocksDto]
    confidence_score: DocExConfidence
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        file_name = self.file_name
        doc_uri = self.doc_uri
        mime_type = self.mime_type
        word_blocks = []
        for word_blocks_item_data in self.word_blocks:
            word_blocks_item = word_blocks_item_data.to_dict()

            word_blocks.append(word_blocks_item)

        form_fields = []
        for form_fields_item_data in self.form_fields:
            form_fields_item = form_fields_item_data.to_dict()

            form_fields.append(form_fields_item)

        tables = []
        for tables_item_data in self.tables:
            tables_item = tables_item_data.to_dict()

            tables.append(tables_item)

        confidence_score = self.confidence_score.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "fileName": file_name,
                "docUri": doc_uri,
                "mimeType": mime_type,
                "wordBlocks": word_blocks,
                "formFields": form_fields,
                "tables": tables,
                "confidenceScore": confidence_score,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        file_name = d.pop("fileName")

        doc_uri = d.pop("docUri")

        mime_type = d.pop("mimeType")

        word_blocks = []
        _word_blocks = d.pop("wordBlocks")
        for word_blocks_item_data in _word_blocks:
            word_blocks_item = BlockResultDto.from_dict(word_blocks_item_data)

            word_blocks.append(word_blocks_item)

        form_fields = []
        _form_fields = d.pop("formFields")
        for form_fields_item_data in _form_fields:
            form_fields_item = ExtractedFormFieldsWithBlocksDto.from_dict(form_fields_item_data)

            form_fields.append(form_fields_item)

        tables = []
        _tables = d.pop("tables")
        for tables_item_data in _tables:
            tables_item = DeprecatedExtractedTableWithBlocksDto.from_dict(tables_item_data)

            tables.append(tables_item)

        confidence_score = DocExConfidence(d.pop("confidenceScore"))

        extraction_results_with_blocks_dto = cls(
            id=id,
            file_name=file_name,
            doc_uri=doc_uri,
            mime_type=mime_type,
            word_blocks=word_blocks,
            form_fields=form_fields,
            tables=tables,
            confidence_score=confidence_score,
        )

        extraction_results_with_blocks_dto.additional_properties = d
        return extraction_results_with_blocks_dto

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
