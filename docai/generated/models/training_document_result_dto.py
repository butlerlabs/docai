from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.block_dto import BlockDto
from ..models.training_annotation_dto import TrainingAnnotationDto

T = TypeVar("T", bound="TrainingDocumentResultDto")


@attr.s(auto_attribs=True)
class TrainingDocumentResultDto:
    """
    Attributes:
        model_id (str): The id of the model.
        document_id (str): The id of the document.
        file_name (str): The file name of this document.
        temp_doc_url (str): The temporary url for this specific document.
        mime_type (str): The type of document that the results were extracted from.
        word_blocks (List[BlockDto]): The word blocks for this specific document.
        annotations (TrainingAnnotationDto):
    """

    model_id: str
    document_id: str
    file_name: str
    temp_doc_url: str
    mime_type: str
    word_blocks: List[BlockDto]
    annotations: TrainingAnnotationDto
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        model_id = self.model_id
        document_id = self.document_id
        file_name = self.file_name
        temp_doc_url = self.temp_doc_url
        mime_type = self.mime_type
        word_blocks = []
        for word_blocks_item_data in self.word_blocks:
            word_blocks_item = word_blocks_item_data.to_dict()

            word_blocks.append(word_blocks_item)

        annotations = self.annotations.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "modelId": model_id,
                "documentId": document_id,
                "fileName": file_name,
                "tempDocUrl": temp_doc_url,
                "mimeType": mime_type,
                "wordBlocks": word_blocks,
                "annotations": annotations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        model_id = d.pop("modelId")

        document_id = d.pop("documentId")

        file_name = d.pop("fileName")

        temp_doc_url = d.pop("tempDocUrl")

        mime_type = d.pop("mimeType")

        word_blocks = []
        _word_blocks = d.pop("wordBlocks")
        for word_blocks_item_data in _word_blocks:
            word_blocks_item = BlockDto.from_dict(word_blocks_item_data)

            word_blocks.append(word_blocks_item)

        annotations = TrainingAnnotationDto.from_dict(d.pop("annotations"))

        training_document_result_dto = cls(
            model_id=model_id,
            document_id=document_id,
            file_name=file_name,
            temp_doc_url=temp_doc_url,
            mime_type=mime_type,
            word_blocks=word_blocks,
            annotations=annotations,
        )

        training_document_result_dto.additional_properties = d
        return training_document_result_dto

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
