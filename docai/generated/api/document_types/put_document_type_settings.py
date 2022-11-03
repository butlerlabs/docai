from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.document_type_settings_dto import DocumentTypeSettingsDto
from ...types import Response


def _get_kwargs(
    doc_type_id: str,
    *,
    client: AuthenticatedClient,
    json_body: DocumentTypeSettingsDto,
) -> Dict[str, Any]:
    url = "{}/api/internal/document_types/{docTypeId}/settings".format(client.base_url, docTypeId=doc_type_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[DocumentTypeSettingsDto]:
    if response.status_code == 201:
        response_201 = DocumentTypeSettingsDto.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[DocumentTypeSettingsDto]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    doc_type_id: str,
    *,
    client: AuthenticatedClient,
    json_body: DocumentTypeSettingsDto,
) -> Response[DocumentTypeSettingsDto]:
    """Put a document type's settings, by ID

    Args:
        doc_type_id (str):
        json_body (DocumentTypeSettingsDto):

    Returns:
        Response[DocumentTypeSettingsDto]
    """

    kwargs = _get_kwargs(
        doc_type_id=doc_type_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    doc_type_id: str,
    *,
    client: AuthenticatedClient,
    json_body: DocumentTypeSettingsDto,
) -> Optional[DocumentTypeSettingsDto]:
    """Put a document type's settings, by ID

    Args:
        doc_type_id (str):
        json_body (DocumentTypeSettingsDto):

    Returns:
        Response[DocumentTypeSettingsDto]
    """

    return sync_detailed(
        doc_type_id=doc_type_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    doc_type_id: str,
    *,
    client: AuthenticatedClient,
    json_body: DocumentTypeSettingsDto,
) -> Response[DocumentTypeSettingsDto]:
    """Put a document type's settings, by ID

    Args:
        doc_type_id (str):
        json_body (DocumentTypeSettingsDto):

    Returns:
        Response[DocumentTypeSettingsDto]
    """

    kwargs = _get_kwargs(
        doc_type_id=doc_type_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    doc_type_id: str,
    *,
    client: AuthenticatedClient,
    json_body: DocumentTypeSettingsDto,
) -> Optional[DocumentTypeSettingsDto]:
    """Put a document type's settings, by ID

    Args:
        doc_type_id (str):
        json_body (DocumentTypeSettingsDto):

    Returns:
        Response[DocumentTypeSettingsDto]
    """

    return (
        await asyncio_detailed(
            doc_type_id=doc_type_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
