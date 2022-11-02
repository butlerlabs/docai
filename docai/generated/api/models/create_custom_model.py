from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.create_model_dto import CreateModelDto
from ...models.model_info_dto import ModelInfoDto
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: CreateModelDto,
) -> Dict[str, Any]:
    url = "{}/api/models".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
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
    *,
    client: AuthenticatedClient,
    json_body: CreateModelDto,
) -> Response[ModelInfoDto]:
    """Create a new custom model

    Args:
        json_body (CreateModelDto):

    Returns:
        Response[ModelInfoDto]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: CreateModelDto,
) -> Optional[ModelInfoDto]:
    """Create a new custom model

    Args:
        json_body (CreateModelDto):

    Returns:
        Response[ModelInfoDto]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: CreateModelDto,
) -> Response[ModelInfoDto]:
    """Create a new custom model

    Args:
        json_body (CreateModelDto):

    Returns:
        Response[ModelInfoDto]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: CreateModelDto,
) -> Optional[ModelInfoDto]:
    """Create a new custom model

    Args:
        json_body (CreateModelDto):

    Returns:
        Response[ModelInfoDto]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
