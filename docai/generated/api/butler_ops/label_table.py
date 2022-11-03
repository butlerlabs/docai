from typing import Any, Dict

import httpx

from ...client import AuthenticatedClient
from ...models.butler_ops_label_table_dto import ButlerOpsLabelTableDto
from ...types import Response


def _get_kwargs(
    document_id: str,
    table_id: str,
    *,
    client: AuthenticatedClient,
    json_body: ButlerOpsLabelTableDto,
) -> Dict[str, Any]:
    url = "{}/api/internal/butler_ops/labeling/{documentId}/table/{tableId}/label_result".format(
        client.base_url, documentId=document_id, tableId=table_id
    )

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


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    document_id: str,
    table_id: str,
    *,
    client: AuthenticatedClient,
    json_body: ButlerOpsLabelTableDto,
) -> Response[Any]:
    """Provide Butler Ops labels for a table for a specific document

    Args:
        document_id (str):
        table_id (str):
        json_body (ButlerOpsLabelTableDto):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        document_id=document_id,
        table_id=table_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    document_id: str,
    table_id: str,
    *,
    client: AuthenticatedClient,
    json_body: ButlerOpsLabelTableDto,
) -> Response[Any]:
    """Provide Butler Ops labels for a table for a specific document

    Args:
        document_id (str):
        table_id (str):
        json_body (ButlerOpsLabelTableDto):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        document_id=document_id,
        table_id=table_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
