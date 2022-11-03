from typing import List

from docai.annotations.ner_utils import DocumentNerAnnotation


def normalize_bounding_box(bbx: List[int]) -> List[int]:
    normalize_bounding_box = list(map(lambda point: int(point * 1000), bbx))
    return normalize_bounding_box


def normalize_ner_annotation_for_layoutlm(annotation: DocumentNerAnnotation) -> DocumentNerAnnotation:
    """
    Normalize the bounding boxes by 1000 to match LayoutLM expected bounding box format
    """
    normalized_bbxs = list(map(normalize_bounding_box, annotation["bboxes"]))
    return {
        "id": annotation["id"],
        "tokens": annotation["tokens"],
        # Normalize NER bounding boxes by 1000 as LayoutLM expects
        "bboxes": normalized_bbxs,
        "ner_tags": annotation["ner_tags"],
        "image": annotation["image"],
    }
