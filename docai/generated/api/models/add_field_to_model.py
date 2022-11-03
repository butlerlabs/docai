from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.add_or_edit_field_dto import AddOrEditFieldDto
from ...models.field_id_response_dto import FieldIdResponseDto
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: AuthenticatedClient,
    json_body: AddOrEditFieldDto,
) -> Dict[str, Any]:
    url = "{}/api/internal/models/{id}/field".format(client.base_url, id=id)

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


def _parse_response(*, response: httpx.Response) -> Optional[FieldIdResponseDto]:
    if response.status_code == 201:
        response_201 = FieldIdResponseDto.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[FieldIdResponseDto]:
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
    json_body: AddOrEditFieldDto,
) -> Response[FieldIdResponseDto]:
    """Adds a new field to a model

    Args:
        id (str):
        json_body (AddOrEditFieldDto):

    Returns:
        Response[FieldIdResponseDto]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
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
    json_body: AddOrEditFieldDto,
) -> Optional[FieldIdResponseDto]:
    """Adds a new field to a model

    Args:
        id (str):
        json_body (AddOrEditFieldDto):

    Returns:
        Response[FieldIdResponseDto]
    """

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    json_body: AddOrEditFieldDto,
) -> Response[FieldIdResponseDto]:
    """Adds a new field to a model

    Args:
        id (str):
        json_body (AddOrEditFieldDto):

    Returns:
        Response[FieldIdResponseDto]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    json_body: AddOrEditFieldDto,
) -> Optional[FieldIdResponseDto]:
    """Adds a new field to a model

    Args:
        id (str):
        json_body (AddOrEditFieldDto):

    Returns:
        Response[FieldIdResponseDto]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
