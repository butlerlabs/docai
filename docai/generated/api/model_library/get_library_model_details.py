from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.base_model_type import BaseModelType
from ...models.library_model_detail_dto import LibraryModelDetailDto
from ...types import Response


def _get_kwargs(
    model_type: BaseModelType,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/internal/model_library/{modelType}/details".format(client.base_url, modelType=model_type)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[LibraryModelDetailDto]:
    if response.status_code == 200:
        response_200 = LibraryModelDetailDto.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[LibraryModelDetailDto]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    model_type: BaseModelType,
    *,
    client: AuthenticatedClient,
) -> Response[LibraryModelDetailDto]:
    """Get details of a library model

    Args:
        model_type (BaseModelType):

    Returns:
        Response[LibraryModelDetailDto]
    """

    kwargs = _get_kwargs(
        model_type=model_type,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    model_type: BaseModelType,
    *,
    client: AuthenticatedClient,
) -> Optional[LibraryModelDetailDto]:
    """Get details of a library model

    Args:
        model_type (BaseModelType):

    Returns:
        Response[LibraryModelDetailDto]
    """

    return sync_detailed(
        model_type=model_type,
        client=client,
    ).parsed


async def asyncio_detailed(
    model_type: BaseModelType,
    *,
    client: AuthenticatedClient,
) -> Response[LibraryModelDetailDto]:
    """Get details of a library model

    Args:
        model_type (BaseModelType):

    Returns:
        Response[LibraryModelDetailDto]
    """

    kwargs = _get_kwargs(
        model_type=model_type,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    model_type: BaseModelType,
    *,
    client: AuthenticatedClient,
) -> Optional[LibraryModelDetailDto]:
    """Get details of a library model

    Args:
        model_type (BaseModelType):

    Returns:
        Response[LibraryModelDetailDto]
    """

    return (
        await asyncio_detailed(
            model_type=model_type,
            client=client,
        )
    ).parsed
