import sys
from typing import Dict, List, Set

from PIL.Image import Image

from docai.annotations.bbx_utils import butler_bbx_to_min_max
from docai.annotations.document_annotation_with_image import DocumentAnnotationWithImage
from docai.generated.models import ModelColumnDto, ModelFieldDto, ModelInfoDto, SimpleFieldLabeledResultDto
from docai.generated.models.block_result_dto import BlockResultDto

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


def get_ner_tags_for_field(field: ModelFieldDto, as_iob=True) -> List[str]:
    """
    Gets the NER tags for a Butler field annotation.

    Parameters
    ----------
    field: List[SimpleFieldLabeledResultDto]
        The field annotation to get the NER tags for.
    as_iob: bool
        Whether to return the tags in Inside-Outside-Beginning format or not.
    """
    formatted_field_name = field.name.replace(" ", "_")

    if as_iob:
        return ["B-" + formatted_field_name, "I-" + formatted_field_name]
    else:
        return [formatted_field_name]


def get_ner_tags_for_column(column: ModelColumnDto, table_name: str, as_iob=True) -> List[str]:
    """
    Gets the NER tags for a Butler column annotation.

    Parameters
    ----------
    column: List[SimpleFieldLabeledResultDto]
        The column annotation to get the NER tags for.
    table_name: str
        The name of the table that the column belongs to.
    as_iob: bool
        Whether to return the tags in Inside-Outside-Beginning format or not.
    """
    formatted_table_name = table_name.replace(" ", "_")
    formatted_column_name = formatted_table_name + "." + column.name.replace(" ", "_")

    if as_iob:
        return ["B-" + formatted_column_name, "I-" + formatted_column_name]
    else:
        return [formatted_column_name]


class ModelNerTags(TypedDict):
    fields: Dict[str, List[str]]
    tables: Dict[str, Dict[str, List[str]]]

    tags: List[str]


def assert_unique_tags(tags: List[str], tag_set: Set[str]):
    """
    Asserts that the tags are unique.

    Parameters
    ----------
    tags: List[str]
        The tags to check.
    tag_set: Set[str]
        The set of tags that have already been checked.
    """
    for tag in tags:
        if tag in tag_set:
            raise ValueError(f"Duplicate NER tag found: {tag}")


def get_ner_tags_for_model(model_details: ModelInfoDto, as_iob: bool = True) -> ModelNerTags:
    """
    Returns a lookup for the NER tags for the fields and tables in a Butler model.

    Parameters
    ----------
    model_details: ModelInfoDto
        The model details to get the NER tags for.
    """
    ner_tags = {"fields": {}, "tables": {}}
    tags_set: Set[str] = set()

    # Add each fields ner tags
    for field in model_details.fields:
        field_name = field.name
        tags = get_ner_tags_for_field(field, as_iob)
        assert_unique_tags(tags, tags_set)
        ner_tags["fields"][field_name] = tags
        tags_set.update(tags)

    # Add each tables ner tags
    for table in model_details.tables:
        table_name = table.name
        table_columns = {}

        for column in table.columns:
            column_name = column.name
            tags = get_ner_tags_for_column(column, table_name, as_iob)
            assert_unique_tags(tags, tags_set)
            table_columns[column_name] = tags
            tags_set.update(tags)

        ner_tags["tables"][table_name] = table_columns

    tag_list = list(tags_set)
    tag_list.sort()
    # Add the Other tag for the Word Blocks
    tag_list.insert(0, "O")
    ner_tags["tags"] = tag_list

    return ner_tags


class NerAnnotation(TypedDict):
    tokens: List[str]
    bboxes: List[List[int]]
    ner_tags: List[str]


def butler_entity_to_ner(blocks: List[BlockResultDto], ner_tag_list: List[str]) -> NerAnnotation:
    """
    Converts a Butler entity (field or table) into NER annotation format.

    Parameters
    ----------
    blocks: List[BlockResultDto]
        The annotated blocks that make up the entity.
    ner_tag_list: List[str]
        The NER tags for the entity.
    """
    tokens = []
    bboxes = []
    ner_tags = []
    for idx, block in enumerate(blocks):
        tokens.append(block.text)
        bboxes.append(butler_bbx_to_min_max(block.bounding_box))

        # If it is the first piece of text for the field and the ner_tag_list is in IOB format or
        # if the ner_tag_list is not in IOB format, then use the first ner tag in the list
        if idx == 0 or len(ner_tag_list) == 1:
            ner_tags.append(ner_tag_list[0])
        # Otherwise use the second ner tag in the list
        else:
            ner_tags.append(ner_tag_list[1])

    return {"tokens": tokens, "bboxes": bboxes, "ner_tags": ner_tags}


def butler_field_to_ner(field: SimpleFieldLabeledResultDto, model_ner_tags: Dict) -> NerAnnotation:
    """
    Converts a Butler field annotation into NER annotation format.

    Parameters
    ----------
    field: SimpleFieldLabeledResultDto
        The field annotation to convert.
    model_ner_tags: Dict
        The NER tags for the model that the field belongs to.
    """
    field_name = field.name
    field_ner_tag_list = model_ner_tags["fields"][field_name]

    field_blocks = field.blocks

    return butler_entity_to_ner(field_blocks, field_ner_tag_list)


def butler_cell_to_ner(
    column_name: str, blocks: List[BlockResultDto], table_name: str, model_ner_tags: Dict
) -> NerAnnotation:
    """
    Converts a Butler cell annotation into NER annotation format.

    Parameters
    ----------
    cell: SimpleFieldLabeledResultDto
        The cell annotation to convert.
    blocks: List[BlockResultDto]
        The blocks that make up the cell.
    table_name: str
        The name of the table that the cell belongs to.
    model_ner_tags: Dict
        The NER tags for the model that the cell belongs to.
    """
    cell_ner_tag_lists = model_ner_tags["tables"][table_name][column_name]

    return butler_entity_to_ner(blocks, cell_ner_tag_lists)


class DocumentNerAnnotation(TypedDict):
    id: str
    tokens: List[str]
    bboxes: List[List[int]]
    ner_tags: List[List[str]]
    image: Image


def document_annotation_to_ner(
    model_details: ModelInfoDto, document_annotation: DocumentAnnotationWithImage, as_iob: bool = True
) -> DocumentNerAnnotation:
    """
    Converts a Butler document annotation into NER annotation format.

    Parameters
    ----------
    model_details: ModelInfoDto
        The model details for the document.
    document: DocumentAnnotationWithImage
        The document annotation to convert.
    """
    model_ner_tags = get_ner_tags_for_model(model_details, as_iob)
    image = document_annotation.image

    ner_annotations = {
        "id": document_annotation.document_id,
        "tokens": [],
        "bboxes": [],
        "ner_tags": [],
        "image": image,
    }

    # Add each fields ner tags
    for field in document_annotation.annotations.fields:
        field_ner_annotations = butler_field_to_ner(field, model_ner_tags)
        ner_annotations["tokens"].extend(field_ner_annotations["tokens"])
        ner_annotations["bboxes"].extend(field_ner_annotations["bboxes"])
        ner_annotations["ner_tags"].extend(field_ner_annotations["ner_tags"])

    # Add each tables ner tags
    for table in document_annotation.annotations.tables:
        table_name = table.name

        for row in table.rows:
            for colIdx, cell in enumerate(row.cells):
                column_name = table.columns[colIdx].name
                cell_blocks = cell.blocks

                cell_ner_annotations = butler_cell_to_ner(column_name, cell_blocks, table_name, model_ner_tags)
                ner_annotations["tokens"].extend(cell_ner_annotations["tokens"])
                ner_annotations["bboxes"].extend(cell_ner_annotations["bboxes"])
                ner_annotations["ner_tags"].extend(cell_ner_annotations["ner_tags"])

    # Add remaining word blocks as the other tag ('O')
    word_ner_annotations = butler_entity_to_ner(document_annotation.word_blocks, ["O"])
    ner_annotations["tokens"].extend(word_ner_annotations["tokens"])
    ner_annotations["bboxes"].extend(word_ner_annotations["bboxes"])
    ner_annotations["ner_tags"].extend(word_ner_annotations["ner_tags"])

    return ner_annotations
