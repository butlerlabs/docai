from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.block_result_dto import BlockResultDto

T = TypeVar("T", bound="StaticTrainingDocumentDetailsDto")


@attr.s(auto_attribs=True)
class StaticTrainingDocumentDetailsDto:
    """
    Attributes:
        document_id (str): The unique id of the document.
        signed_url (str): The signed url for this specific document.
        mime_type (str): The type of document that the results were extracted from
        word_blocks (List[BlockResultDto]): The word blocks for this specific document.
    """

    document_id: str
    signed_url: str
    mime_type: str
    word_blocks: List[BlockResultDto]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        document_id = self.document_id
        signed_url = self.signed_url
        mime_type = self.mime_type
        word_blocks = []
        for word_blocks_item_data in self.word_blocks:
            word_blocks_item = word_blocks_item_data.to_dict()

            word_blocks.append(word_blocks_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "documentId": document_id,
                "signedUrl": signed_url,
                "mimeType": mime_type,
                "wordBlocks": word_blocks,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        document_id = d.pop("documentId")

        signed_url = d.pop("signedUrl")

        mime_type = d.pop("mimeType")

        word_blocks = []
        _word_blocks = d.pop("wordBlocks")
        for word_blocks_item_data in _word_blocks:
            word_blocks_item = BlockResultDto.from_dict(word_blocks_item_data)

            word_blocks.append(word_blocks_item)

        static_training_document_details_dto = cls(
            document_id=document_id,
            signed_url=signed_url,
            mime_type=mime_type,
            word_blocks=word_blocks,
        )

        static_training_document_details_dto.additional_properties = d
        return static_training_document_details_dto

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
