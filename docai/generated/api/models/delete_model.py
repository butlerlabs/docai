from typing import Any, Dict

import httpx

from ...client import AuthenticatedClient
from ...models.model_summary_task_type import ModelSummaryTaskType
from ...types import UNSET, Response


def _get_kwargs(
    model_id: str,
    *,
    client: AuthenticatedClient,
    model_type: ModelSummaryTaskType,
) -> Dict[str, Any]:
    url = "{}/api/internal/models/{modelId}".format(client.base_url, modelId=model_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_model_type = model_type.value

    params["modelType"] = json_model_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
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
    model_type: ModelSummaryTaskType,
) -> Response[Any]:
    """Delete a ml model

    Args:
        model_id (str):
        model_type (ModelSummaryTaskType):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        model_id=model_id,
        client=client,
        model_type=model_type,
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
    model_type: ModelSummaryTaskType,
) -> Response[Any]:
    """Delete a ml model

    Args:
        model_id (str):
        model_type (ModelSummaryTaskType):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        model_id=model_id,
        client=client,
        model_type=model_type,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
