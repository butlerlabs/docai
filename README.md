# Butler Doc AI

Welcome to [Butler Doc AI](https://butlerlabs.ai)

## Requirements

Python >= 3.7

## Installation & Usage

### pip install

```sh
pip install docai-py
```

### Misc packages that might be needed to be installed on your environment
- Poppler

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

from docai import PredictionClient

# Get API Key from https://docs.butlerlabs.ai/reference/uploading-documents-to-the-rest-api#get-your-api-key
api_key = '<api-key>'
# Get Queue ID from https://docs.butlerlabs.ai/reference/uploading-documents-to-the-rest-api#go-to-the-model-details-page
queue_id = '<queue_id>'
# Path to a local JPEG, PNG, or PDF file
local_file_path = 'example.pdf'

extraction_results = PredictionClient(api_key).extract_document(queue_id, local_file_path)
print(extraction_results)
```

## Maintain

```sh
PIPENV_VENV_IN_PROJECT=1 pipenv install -d
```

To regenerate code updates to REST API:

```sh
openapi-python-client update --url https://app.butlerlabs.ai/api/docs-json --config codegen.yaml
```

and make manual updates to `docai/__init.py__` if needed

To publish a new version:

Update `setup.py` to have a new version number

```sh
# build packages
python -m build

# upload to test pypi
python -m twine upload --repository testpypi --skip-existing dist/* --verbose

# test install from test pypi
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple docai-py

# Upload to real pypi if things checkout
python -m twine upload --skip-existing dist/* --verbose
```
