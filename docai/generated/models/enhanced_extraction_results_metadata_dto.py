from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.block_result_dto import BlockResultDto
from ..models.doc_ex_confidence import DocExConfidence
from ..types import UNSET, Unset

T = TypeVar("T", bound="EnhancedExtractionResultsMetadataDto")


@attr.s(auto_attribs=True)
class EnhancedExtractionResultsMetadataDto:
    """
    Attributes:
        id (str): Id of the extracted document
        file_name (str): Name of the file that these results were extracted from
        doc_uri (str): Identifier for the hosted document that the results were extracted from
        mime_type (str): The type of document that the results were extracted from
        doc_type_id (str): The id of the Document Type that was used to generate these extraction results.
        doc_type_name (str): The name of the Document Type that was used to generate these extraction results.
        confidence_score (DocExConfidence):
        word_blocks (List[BlockResultDto]): Word blocks detected on the document
        doc_type_notes_url (Union[Unset, str]): The URL of the notes for the Document Type that was used to generate
            these extraction results. Will be empty if no notes exist.
    """

    id: str
    file_name: str
    doc_uri: str
    mime_type: str
    doc_type_id: str
    doc_type_name: str
    confidence_score: DocExConfidence
    word_blocks: List[BlockResultDto]
    doc_type_notes_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        file_name = self.file_name
        doc_uri = self.doc_uri
        mime_type = self.mime_type
        doc_type_id = self.doc_type_id
        doc_type_name = self.doc_type_name
        confidence_score = self.confidence_score.value

        word_blocks = []
        for word_blocks_item_data in self.word_blocks:
            word_blocks_item = word_blocks_item_data.to_dict()

            word_blocks.append(word_blocks_item)

        doc_type_notes_url = self.doc_type_notes_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "fileName": file_name,
                "docUri": doc_uri,
                "mimeType": mime_type,
                "docTypeId": doc_type_id,
                "docTypeName": doc_type_name,
                "confidenceScore": confidence_score,
                "wordBlocks": word_blocks,
            }
        )
        if doc_type_notes_url is not UNSET:
            field_dict["docTypeNotesUrl"] = doc_type_notes_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        file_name = d.pop("fileName")

        doc_uri = d.pop("docUri")

        mime_type = d.pop("mimeType")

        doc_type_id = d.pop("docTypeId")

        doc_type_name = d.pop("docTypeName")

        confidence_score = DocExConfidence(d.pop("confidenceScore"))

        word_blocks = []
        _word_blocks = d.pop("wordBlocks")
        for word_blocks_item_data in _word_blocks:
            word_blocks_item = BlockResultDto.from_dict(word_blocks_item_data)

            word_blocks.append(word_blocks_item)

        doc_type_notes_url = d.pop("docTypeNotesUrl", UNSET)

        enhanced_extraction_results_metadata_dto = cls(
            id=id,
            file_name=file_name,
            doc_uri=doc_uri,
            mime_type=mime_type,
            doc_type_id=doc_type_id,
            doc_type_name=doc_type_name,
            confidence_score=confidence_score,
            word_blocks=word_blocks,
            doc_type_notes_url=doc_type_notes_url,
        )

        enhanced_extraction_results_metadata_dto.additional_properties = d
        return enhanced_extraction_results_metadata_dto

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
