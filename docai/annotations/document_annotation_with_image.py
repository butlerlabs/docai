import logging
from typing import List

from PIL import Image

from docai.annotations.image_utils import load_file_as_img
from docai.generated.models import BlockResultDto, TrainingDocumentResultDto


# filter blocks to first page and by ids
def filter_blocks(blocks_list: List[BlockResultDto], banned_ids=None):
    return [b for b in blocks_list if b.bounding_box.page == 0 and (banned_ids is None or b.id not in banned_ids)]


class DocumentAnnotationWithImage(TrainingDocumentResultDto):
    """
    This class represents the annotations for a single document that can be
    used to train a document extraction model.

    Limitations:
    - Does not support multi-page documents. If a multi-page document is provided, only the first page will be used,
    and blocks from subsequent pages will be filtered out.
    """

    image: Image

    def __init__(self, training_document: TrainingDocumentResultDto):
        self.model_id = training_document.model_id
        self.document_id = training_document.document_id
        self.file_name = training_document.file_name
        self.temp_doc_url = training_document.temp_doc_url
        self.mime_type = training_document.mime_type
        self.annotations = training_document.annotations

        # Download the image from temp_doc_url and save it as a PIL image
        images = load_file_as_img(self.temp_doc_url, self.mime_type)

        if len(images) > 1:
            logging.warning(
                f"Found {len(images)} pages in document {self.document_id}. Multi-page documents are not supported. Using first page."
            )

        self.image = images[0]

        used_block_ids = set()

        # Filter out blocks that are not on the first page in the fields
        for field in self.annotations.fields:
            field.blocks = filter_blocks(field.blocks)
            used_block_ids.update([block.id for block in field.blocks])

        # Filter out blocks that are not on the first page in the tables
        for table in self.annotations.tables:
            for row in table.rows:
                for cell in row.cells:
                    cell.blocks = filter_blocks(cell.blocks)
                    used_block_ids.update([block.id for block in cell.blocks])

        # Filter out word blocks that are not on the first page in the document
        self.word_blocks = filter_blocks(training_document.word_blocks, banned_ids=used_block_ids)
