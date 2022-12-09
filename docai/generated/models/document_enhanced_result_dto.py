from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.block_dto import BlockDto
from ..models.label_dto import LabelDto

T = TypeVar("T", bound="DocumentEnhancedResultDto")


@attr.s(auto_attribs=True)
class DocumentEnhancedResultDto:
    """
    Attributes:
        document_id (str): The ID of the document.
        file_name (str): The file name of this document.
        mime_type (str): The mime type of document.
        model_id (str): The ID of the model.
        temp_doc_url (str): The temporary url for this specific document.
        word_blocks (List[BlockDto]): The word blocks for this specific document.
        results (LabelDto):
    """

    document_id: str
    file_name: str
    mime_type: str
    model_id: str
    temp_doc_url: str
    word_blocks: List[BlockDto]
    results: LabelDto
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        document_id = self.document_id
        file_name = self.file_name
        mime_type = self.mime_type
        model_id = self.model_id
        temp_doc_url = self.temp_doc_url
        word_blocks = []
        for word_blocks_item_data in self.word_blocks:
            word_blocks_item = word_blocks_item_data.to_dict()

            word_blocks.append(word_blocks_item)

        results = self.results.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "documentId": document_id,
                "fileName": file_name,
                "mimeType": mime_type,
                "modelId": model_id,
                "tempDocUrl": temp_doc_url,
                "wordBlocks": word_blocks,
                "results": results,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        document_id = d.pop("documentId")

        file_name = d.pop("fileName")

        mime_type = d.pop("mimeType")

        model_id = d.pop("modelId")

        temp_doc_url = d.pop("tempDocUrl")

        word_blocks = []
        _word_blocks = d.pop("wordBlocks")
        for word_blocks_item_data in _word_blocks:
            word_blocks_item = BlockDto.from_dict(word_blocks_item_data)

            word_blocks.append(word_blocks_item)

        results = LabelDto.from_dict(d.pop("results"))

        document_enhanced_result_dto = cls(
            document_id=document_id,
            file_name=file_name,
            mime_type=mime_type,
            model_id=model_id,
            temp_doc_url=temp_doc_url,
            word_blocks=word_blocks,
            results=results,
        )

        document_enhanced_result_dto.additional_properties = d
        return document_enhanced_result_dto

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
