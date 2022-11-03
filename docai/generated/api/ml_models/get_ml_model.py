from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.ml_model_dto import MlModelDto
from ...types import Response


def _get_kwargs(
    model_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/internal/ml_models/{modelId}".format(client.base_url, modelId=model_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[MlModelDto]:
    if response.status_code == 200:
        response_200 = MlModelDto.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[MlModelDto]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    model_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[MlModelDto]:
    """Get details of a ml model

    Args:
        model_id (str):

    Returns:
        Response[MlModelDto]
    """

    kwargs = _get_kwargs(
        model_id=model_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    model_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[MlModelDto]:
    """Get details of a ml model

    Args:
        model_id (str):

    Returns:
        Response[MlModelDto]
    """

    return sync_detailed(
        model_id=model_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    model_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[MlModelDto]:
    """Get details of a ml model

    Args:
        model_id (str):

    Returns:
        Response[MlModelDto]
    """

    kwargs = _get_kwargs(
        model_id=model_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    model_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[MlModelDto]:
    """Get details of a ml model

    Args:
        model_id (str):

    Returns:
        Response[MlModelDto]
    """

    return (
        await asyncio_detailed(
            model_id=model_id,
            client=client,
        )
    ).parsed
