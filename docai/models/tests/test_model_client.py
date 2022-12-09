import json
import logging
from contextlib import ExitStack
from unittest.mock import patch

import pytest

from docai import ModelClient
from docai.generated.models import ModelInfoDto
from docai.generated.types import Response

logging.basicConfig(level=logging.INFO)

SAMPLE_CREATE_CUSTOM_MODEL_RESPONSE_DICT = {
    "id": "7c8dec4d-83cf-4708-a691-5bde1f0bc384",
    "name": "Cloned Bank Statement Model",
    "status": "NeedsTraining",
    "modelType": "Custom",
    "fields": [
        {"id": "64ca8f44-81f7-42c6-9b67-3daab91a3201", "name": "Account Number", "type": "Text"},
        {"id": "a584fb96-5099-49fa-b7b7-ff2b86287f9d", "name": "Account Type", "type": "Text"},
        {"id": "f0912a70-5037-4237-bfd0-480fa928a627", "name": "Bank Address", "type": "Text"},
        {"id": "fa022542-814d-473a-976c-aa12bf1872a5", "name": "Bank Name", "type": "Text"},
        {"id": "9a64e544-81da-4cf7-a16c-8ff417c81fb5", "name": "Client Address", "type": "Text"},
        {"id": "4b40cd5d-43e9-471c-8af2-ac7f746e2c16", "name": "Client Name", "type": "Text"},
        {"id": "8c4a9d96-b2ae-4757-b956-7129fa13077d", "name": "Ending Balance", "type": "Text"},
        {"id": "19e36a4d-22e2-40e4-8a84-3257f1570d55", "name": "Starting Balance", "type": "Text"},
        {"id": "b672103c-10fb-45a5-8ab6-38fa730a24d9", "name": "Statement Date", "type": "Text"},
        {"id": "fd139968-b44e-4ce9-bf1d-1b2af40b5ca2", "name": "Statement End Date", "type": "Text"},
        {"id": "0b253fec-bd4e-4a10-9c72-7d070e51c7da", "name": "Statement Start Date", "type": "Text"},
    ],
    "tables": [
        {
            "id": "5bc06e88-b80d-4320-bcf9-6a512d410394",
            "name": "Transactions",
            "columns": [
                {"id": "90033ea9-b86b-4091-b163-dc81410c95ef", "name": "Deposit Amount"},
                {"id": "c24584f1-1831-493d-a7f6-eb839c3514a5", "name": "Deposit Date"},
                {"id": "922ab603-4959-4038-8372-ce422ceaae5b", "name": "Deposit Description"},
                {"id": "e2acb160-194e-4ee7-8238-15a6e998e06f", "name": "Withdrawal Amount"},
                {"id": "ffe81436-2f41-404b-b0d9-9974cd7abc4c", "name": "Withdrawal Date"},
                {"id": "700d768a-6981-4900-93e9-133d90e5d997", "name": "Withdrawal Description"},
            ],
            "type": "Table",
        }
    ],
    "trainingFailureReason": None,
    "trainingDisabledReason": "NotEnoughDocumentsLabeled",
    "queueId": "9baa9e67-07d4-4027-9f03-5ca6f5915587",
    "numTrainingDocuments": 0,
}

SAMPLE_GET_MODEL_INFO_DICT = {
    "id": "ef6a3ae7-a285-4aa6-9f4c-45829c1350f0",
    "name": "Bank Statements",
    "status": "Active",
    "modelType": "Pretrained",
    "fields": [
        {"id": "5ba85135-4b98-4129-a9bb-15fd91c1d13b", "name": "Account Number", "type": "Text"},
        {"id": "b499b7b3-5b90-402a-ad25-be76b5946eff", "name": "Account Type", "type": "Text"},
        {"id": "8a5a8ee1-89f1-4107-a9ce-aeb8b3f3417c", "name": "Bank Address", "type": "Text"},
        {"id": "e96c8ec1-c025-4c96-8c28-d1fbc3aeab57", "name": "Bank Name", "type": "Text"},
        {"id": "6cbb4f44-b6f6-49c8-8dd9-6d2b3bac633f", "name": "Client Address", "type": "Text"},
        {"id": "7a8e0080-bdd0-4fdb-a37e-080047b426e3", "name": "Client Name", "type": "Text"},
        {"id": "51f90cb8-5adf-4b74-8956-201f241f23ba", "name": "Ending Balance", "type": "Text"},
        {"id": "e6982958-7581-4411-9fb2-c7b898fe6f6c", "name": "Starting Balance", "type": "Text"},
        {"id": "c97ac86d-a063-436d-964c-f84b5b4c8ef0", "name": "Statement Date", "type": "Text"},
        {"id": "0e45087a-207c-48c7-a3ff-f04421f24c2b", "name": "Statement End Date", "type": "Text"},
        {"id": "5906e15f-b346-40c1-b394-3adf4da1620e", "name": "Statement Start Date", "type": "Text"},
    ],
    "tables": [
        {
            "id": "a703aefb-f16f-40ee-bd90-08f048e97205",
            "name": "Transactions",
            "columns": [
                {"id": "b2adff10-a67d-4cb4-b8b7-ae2a7a91e86d", "name": "Deposit Amount"},
                {"id": "914b0414-a3a9-48c6-80e4-fad5bf4e1397", "name": "Deposit Date"},
                {"id": "9b6c2f94-bfbd-494a-b899-850216231f46", "name": "Deposit Description"},
                {"id": "289a56c1-c828-475e-bca4-c046b8c61afe", "name": "Withdrawal Amount"},
                {"id": "8fa40caf-17d9-4490-8b06-ea32e1a3d3fd", "name": "Withdrawal Date"},
                {"id": "2b16a52d-61fd-418d-9a5d-7a91b05c1bb4", "name": "Withdrawal Description"},
            ],
            "type": "Table",
        }
    ],
    "trainingFailureReason": None,
    "trainingDisabledReason": "NotSupported",
    "queueId": "9baa9e67-07d4-4027-9f03-5ca6f5915587",
    "numTrainingDocuments": 0,
}


@pytest.mark.unit_tests
class TestModelClient:
    @pytest.fixture(scope="function", autouse=True)
    def before_each_and_after_each(self):
        with ExitStack() as stack:

            def patch_fn(fn: str):
                return stack.enter_context(patch(fn))

            self.get_model_info_patch = patch_fn("docai.models.model_client.get_model.sync_detailed")
            self.create_custom_model_patch = patch_fn("docai.models.model_client.create_custom_model.sync_detailed")

            yield

    def test_clone_model_schema(self):
        dr = Response(
            status_code=200,
            content=json.dumps(SAMPLE_GET_MODEL_INFO_DICT).encode("utf-8"),
            headers={},
            parsed=ModelInfoDto.from_dict(SAMPLE_GET_MODEL_INFO_DICT),
        )
        mi = Response(
            status_code=201,
            content=json.dumps(SAMPLE_CREATE_CUSTOM_MODEL_RESPONSE_DICT).encode("utf-8"),
            parsed=None,
            headers={},
        )
        self.get_model_info_patch.return_value = dr
        self.create_custom_model_patch.return_value = mi

        clone_res = ModelClient("api-key").clone_model_schema(model_id="model-id", model_name="cloned model name")
        assert clone_res.id == SAMPLE_CREATE_CUSTOM_MODEL_RESPONSE_DICT["id"]
