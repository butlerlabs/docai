import logging
import os

from docai import PredictionClient

# Run using 'python -m docai.test.test_extract_document'

logging.basicConfig(level=logging.INFO)


def test_extract_document():
    # Get API Key from https://docs.butlerlabs.ai/reference/uploading-documents-to-the-rest-api#get-your-api-key
    api_key = os.environ["BUTLER_API_KEY"]

    # Find your queue's uuid
    queue_id = os.environ["QUEUE_ID"]

    # Get a local test file
    local_file = "./docai/test/test.pdf"

    extraction_results = PredictionClient(api_key).extract_document(queue_id, local_file)

    assert extraction_results is not None
