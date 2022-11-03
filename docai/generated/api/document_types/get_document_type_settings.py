from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.document_type_settings_dto import DocumentTypeSettingsDto
from ...types import Response


def _get_kwargs(
    doc_type_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/internal/document_types/{docTypeId}/settings".format(client.base_url, docTypeId=doc_type_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[DocumentTypeSettingsDto]:
    if response.status_code == 200:
        response_200 = DocumentTypeSettingsDto.from_dict(response.json())

        return response_200
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
) -> Response[DocumentTypeSettingsDto]:
    """Get a document type's settings, by ID

    Args:
        doc_type_id (str):

    Returns:
        Response[DocumentTypeSettingsDto]
    """

    kwargs = _get_kwargs(
        doc_type_id=doc_type_id,
        client=client,
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
) -> Optional[DocumentTypeSettingsDto]:
    """Get a document type's settings, by ID

    Args:
        doc_type_id (str):

    Returns:
        Response[DocumentTypeSettingsDto]
    """

    return sync_detailed(
        doc_type_id=doc_type_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    doc_type_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[DocumentTypeSettingsDto]:
    """Get a document type's settings, by ID

    Args:
        doc_type_id (str):

    Returns:
        Response[DocumentTypeSettingsDto]
    """

    kwargs = _get_kwargs(
        doc_type_id=doc_type_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    doc_type_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[DocumentTypeSettingsDto]:
    """Get a document type's settings, by ID

    Args:
        doc_type_id (str):

    Returns:
        Response[DocumentTypeSettingsDto]
    """

    return (
        await asyncio_detailed(
            doc_type_id=doc_type_id,
            client=client,
        )
    ).parsed
