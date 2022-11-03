from typing import Any, Dict

import httpx

from ...client import AuthenticatedClient
from ...models.edit_ml_model_name_dto import EditMlModelNameDto
from ...types import Response


def _get_kwargs(
    model_id: str,
    *,
    client: AuthenticatedClient,
    json_body: EditMlModelNameDto,
) -> Dict[str, Any]:
    url = "{}/api/internal/ml_models/{modelId}".format(client.base_url, modelId=model_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    model_id: str,
    *,
    client: AuthenticatedClient,
    json_body: EditMlModelNameDto,
) -> Response[Any]:
    """Updates the name of a ml model

    Args:
        model_id (str):
        json_body (EditMlModelNameDto):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        model_id=model_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    model_id: str,
    *,
    client: AuthenticatedClient,
    json_body: EditMlModelNameDto,
) -> Response[Any]:
    """Updates the name of a ml model

    Args:
        model_id (str):
        json_body (EditMlModelNameDto):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        model_id=model_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
