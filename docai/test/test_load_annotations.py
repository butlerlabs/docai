import logging
import os

import pytest

from docai import AnnotationClient
from docai.annotations.layoutlm_utils import normalize_ner_annotation_for_layoutlm

logging.basicConfig(level=logging.INFO)


@pytest.mark.e2e_tests
class TestAnnotationClient:
    # Get API Key from https://docs.butlerlabs.ai/reference/uploading-documents-to-the-rest-api#get-your-api-key
    def test_annotations(self):
        api_key = os.environ["BUTLER_API_KEY"]

        # Find your model's uuid
        model_id = os.environ["MODEL_ID"]

        annotations = AnnotationClient(api_key).load_annotations(
            model_id,
            load_all_pages=True,
        )

        annotations_as_ner = annotations.as_ner(as_iob2=True)

        # Normalize NER annotations by 1000 to match LayoutLM expected bounding box format
        annotations_as_ner = list(map(normalize_ner_annotation_for_layoutlm, annotations_as_ner))

        assert annotations_as_ner is not None
