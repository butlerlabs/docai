from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.base_model_type import BaseModelType
from ...models.create_model_response_dto import CreateModelResponseDto
from ...types import Response


def _get_kwargs(
    model_type: BaseModelType,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/internal/model_library/{modelType}/create".format(client.base_url, modelType=model_type)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[CreateModelResponseDto]:
    if response.status_code == 201:
        response_201 = CreateModelResponseDto.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[CreateModelResponseDto]:
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
) -> Response[CreateModelResponseDto]:
    """Creates a new instance of the model_type model

    Args:
        model_type (BaseModelType):

    Returns:
        Response[CreateModelResponseDto]
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
) -> Optional[CreateModelResponseDto]:
    """Creates a new instance of the model_type model

    Args:
        model_type (BaseModelType):

    Returns:
        Response[CreateModelResponseDto]
    """

    return sync_detailed(
        model_type=model_type,
        client=client,
    ).parsed


async def asyncio_detailed(
    model_type: BaseModelType,
    *,
    client: AuthenticatedClient,
) -> Response[CreateModelResponseDto]:
    """Creates a new instance of the model_type model

    Args:
        model_type (BaseModelType):

    Returns:
        Response[CreateModelResponseDto]
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
) -> Optional[CreateModelResponseDto]:
    """Creates a new instance of the model_type model

    Args:
        model_type (BaseModelType):

    Returns:
        Response[CreateModelResponseDto]
    """

    return (
        await asyncio_detailed(
            model_type=model_type,
            client=client,
        )
    ).parsed
