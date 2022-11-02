from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.model_info_dto import ModelInfoDto
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/models/{id}".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[ModelInfoDto]:
    if response.status_code == 200:
        response_200 = ModelInfoDto.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ModelInfoDto]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ModelInfoDto]:
    """Get details of a model

    Args:
        id (str):

    Returns:
        Response[ModelInfoDto]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[ModelInfoDto]:
    """Get details of a model

    Args:
        id (str):

    Returns:
        Response[ModelInfoDto]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ModelInfoDto]:
    """Get details of a model

    Args:
        id (str):

    Returns:
        Response[ModelInfoDto]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[ModelInfoDto]:
    """Get details of a model

    Args:
        id (str):

    Returns:
        Response[ModelInfoDto]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
