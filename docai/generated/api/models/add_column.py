from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.add_or_edit_column_dto import AddOrEditColumnDto
from ...models.column_id_response_dto import ColumnIdResponseDto
from ...types import Response


def _get_kwargs(
    id: str,
    table_id: str,
    *,
    client: AuthenticatedClient,
    json_body: AddOrEditColumnDto,
) -> Dict[str, Any]:
    url = "{}/api/internal/models/{id}/table/{tableId}/column".format(client.base_url, id=id, tableId=table_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[ColumnIdResponseDto]:
    if response.status_code == 201:
        response_201 = ColumnIdResponseDto.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[ColumnIdResponseDto]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    table_id: str,
    *,
    client: AuthenticatedClient,
    json_body: AddOrEditColumnDto,
) -> Response[ColumnIdResponseDto]:
    """Adds a column to a table

    Args:
        id (str):
        table_id (str):
        json_body (AddOrEditColumnDto):

    Returns:
        Response[ColumnIdResponseDto]
    """

    kwargs = _get_kwargs(
        id=id,
        table_id=table_id,
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
    table_id: str,
    *,
    client: AuthenticatedClient,
    json_body: AddOrEditColumnDto,
) -> Optional[ColumnIdResponseDto]:
    """Adds a column to a table

    Args:
        id (str):
        table_id (str):
        json_body (AddOrEditColumnDto):

    Returns:
        Response[ColumnIdResponseDto]
    """

    return sync_detailed(
        id=id,
        table_id=table_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    id: str,
    table_id: str,
    *,
    client: AuthenticatedClient,
    json_body: AddOrEditColumnDto,
) -> Response[ColumnIdResponseDto]:
    """Adds a column to a table

    Args:
        id (str):
        table_id (str):
        json_body (AddOrEditColumnDto):

    Returns:
        Response[ColumnIdResponseDto]
    """

    kwargs = _get_kwargs(
        id=id,
        table_id=table_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    table_id: str,
    *,
    client: AuthenticatedClient,
    json_body: AddOrEditColumnDto,
) -> Optional[ColumnIdResponseDto]:
    """Adds a column to a table

    Args:
        id (str):
        table_id (str):
        json_body (AddOrEditColumnDto):

    Returns:
        Response[ColumnIdResponseDto]
    """

    return (
        await asyncio_detailed(
            id=id,
            table_id=table_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
