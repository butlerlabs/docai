from typing import Any, Dict

import httpx

from ...client import AuthenticatedClient
from ...models.butler_ops_field_notes_update_dto import ButlerOpsFieldNotesUpdateDto
from ...types import Response


def _get_kwargs(
    document_type_id: str,
    field_id: str,
    *,
    client: AuthenticatedClient,
    json_body: ButlerOpsFieldNotesUpdateDto,
) -> Dict[str, Any]:
    url = "{}/api/internal/butler_ops/management/{documentTypeId}/notes/{fieldId}".format(
        client.base_url, documentTypeId=document_type_id, fieldId=field_id
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
    document_type_id: str,
    field_id: str,
    *,
    client: AuthenticatedClient,
    json_body: ButlerOpsFieldNotesUpdateDto,
) -> Response[Any]:
    """Updates the notes for a specific field on a doc type

    Args:
        document_type_id (str):
        field_id (str):
        json_body (ButlerOpsFieldNotesUpdateDto):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        document_type_id=document_type_id,
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
    document_type_id: str,
    field_id: str,
    *,
    client: AuthenticatedClient,
    json_body: ButlerOpsFieldNotesUpdateDto,
) -> Response[Any]:
    """Updates the notes for a specific field on a doc type

    Args:
        document_type_id (str):
        field_id (str):
        json_body (ButlerOpsFieldNotesUpdateDto):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        document_type_id=document_type_id,
        field_id=field_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
