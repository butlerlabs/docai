import json
import logging

from docai.common.base_client import BaseClient
from docai.common.http_utils import verify_response_or_raise
from docai.generated.api.models import create_custom_model, get_model
from docai.generated.models import CreateModelDto, ModelInfoDto
from docai.models.model_utils import modelFieldToFieldDto, modelTableToTableDto


class ModelClient(BaseClient):
    def clone_model_schema(self, model_id: str, model_name: str) -> ModelInfoDto:
        """
        Uses the given model as a base, and clones all fields and tables to a new model

        Limitations:
        1. Utilizes internal endpoints and is prone to breaking between package versions
        2. Only supports Models with Text type fields and tables
        """

        get_model_res: ModelInfoDto = verify_response_or_raise(get_model.sync_detailed(model_id, client=self._client))
        logging.info(f"Fetching model details for {model_id}")

        # Temporary work around instead of using verify_response_or_raise due
        # to an incorrectly documented openapi spec
        create_custom_model_raw_res = create_custom_model.sync_detailed(
            client=self._client,
            json_body=CreateModelDto(
                name=model_name,
                fields=[modelFieldToFieldDto(f) for f in get_model_res.fields],
                tables=[modelTableToTableDto(t) for t in get_model_res.tables],
            ),
        )
        create_custom_model_res = ModelInfoDto.from_dict(json.loads(create_custom_model_raw_res.content))

        logging.info(f"Created blank custom model {create_custom_model_res.id}")

        return create_custom_model_res
