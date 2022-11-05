# Butler Doc AI
Welcome to [Butler Doc AI](https://butlerlabs.ai)

## Requirements
Python >= 3.7

## Installation & Usage
To install Doc AI with pip:
```sh
pip install docai-py
```

### System Dependencies
#### Mac
- Install [poppler](http://macappstore.org/poppler/)

#### Linux
- Install poppler-utils via your package manager

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
### Install Packages for Development
Install [poetry](https://python-poetry.org/docs/#installation) on your host machine
```sh
poetry install
```

### Butler REST API Codegen
To regenerate code updates to REST API:
```sh
openapi-python-client update --url https://app.butlerlabs.ai/api/docs-json --config codegen.yaml
```

### Running Unit Tests
To run unit tests:
```sh
poetry run pytest
```

### Adding a New Dependency
To add a new pip package dependency, see [poetry add](https://python-poetry.org/docs/cli/#add).
For versioning, it is best to use the minimum version that works, combined with `^`, `~`, or `>=` and `<` checks.
For example:
- `poetry add my-package@^1.2.3` is a shorthand for `>=1.2.3,<2.0.0`
- `poetry add my-package@~1.2.3` is a shorthand for `>=1.2.3,<1.3.0`
- `poetry add "my-package>=1.2.3,<4.5.6"`

For development only dependencies, make sure to include the `--dev` flag.

### Build and Publish

#### Build and Publish Setup
```sh
# setup for testpypi
poetry config repositories.testpypi https://test.pypi.org/legacy/
poetry config pypi-token.testpypi <testpypi token>

# setup for pypi
poetry config repositories.pypi https://pypi.org/legacy/
poetry config pypi-token.pypi <pypi token>
```

#### Build and Publish Procedure
Update `pyproject.toml` and `docai/__init__.py` to have a new version number

```sh
# build packages
poetry build

# upload to test pypi
poetry publish -r testpypi

# test install from test pypi
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple docai-py

# upload to real pypi
poetry publish -r pypi
```
