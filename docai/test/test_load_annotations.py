import logging
import os

from docai import AnnotationsClient
from docai.annotations.layoutlm_utils import normalize_ner_annotation_for_layoutlm

# Run using 'python -m docai.test.test_load_annotations'

logging.basicConfig(level=logging.INFO)

# Get API Key from https://docs.butlerlabs.ai/reference/uploading-documents-to-the-rest-api#get-your-api-key
api_key = os.environ["BUTLER_API_KEY"]

# Find your model's uuid
model_id = "00000000-0000-0000-0000-000000000000"

annotations = AnnotationsClient(api_key).load_annotations(
    model_id,
    load_all_pages=True,
)

annotations_as_ner = annotations.as_ner(as_iob=True)

# Normalize NER annotations by 1000 to match LayoutLM expected bounding box format
annotations_as_ner = list(map(normalize_ner_annotation_for_layoutlm, annotations_as_ner))

print(annotations_as_ner[0])
