from typing import Any, Dict

import httpx

from ...client import AuthenticatedClient
from ...types import Response


def _get_kwargs(
    id: str,
    table_id: str,
    column_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/internal/models/{id}/table/{tableId}/column/{columnId}".format(
        client.base_url, id=id, tableId=table_id, columnId=column_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    id: str,
    table_id: str,
    column_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Deletes a column from a table

    Args:
        id (str):
        table_id (str):
        column_id (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        table_id=table_id,
        column_id=column_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    id: str,
    table_id: str,
    column_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Deletes a column from a table

    Args:
        id (str):
        table_id (str):
        column_id (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        table_id=table_id,
        column_id=column_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
