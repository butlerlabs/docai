from typing import Any, Dict

import httpx

from ...client import AuthenticatedClient
from ...models.delete_field_dto import DeleteFieldDto
from ...types import Response


def _get_kwargs(
    id: str,
    field_id: str,
    *,
    client: AuthenticatedClient,
    json_body: DeleteFieldDto,
) -> Dict[str, Any]:
    url = "{}/api/internal/models/{id}/field/{fieldId}".format(client.base_url, id=id, fieldId=field_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "delete",
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
    id: str,
    field_id: str,
    *,
    client: AuthenticatedClient,
    json_body: DeleteFieldDto,
) -> Response[Any]:
    """Deletes a field from a model

    Args:
        id (str):
        field_id (str):
        json_body (DeleteFieldDto):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        field_id=field_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    id: str,
    field_id: str,
    *,
    client: AuthenticatedClient,
    json_body: DeleteFieldDto,
) -> Response[Any]:
    """Deletes a field from a model

    Args:
        id (str):
        field_id (str):
        json_body (DeleteFieldDto):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        field_id=field_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
