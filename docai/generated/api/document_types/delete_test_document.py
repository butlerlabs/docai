from typing import Any, Dict

import httpx

from ...client import AuthenticatedClient
from ...types import Response


def _get_kwargs(
    doc_type_id: str,
    document_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/internal/document_types/{docTypeId}/test_documents/{documentId}".format(
        client.base_url, docTypeId=doc_type_id, documentId=document_id
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
    doc_type_id: str,
    document_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Soft deletes a test document, by ID.

    Args:
        doc_type_id (str):
        document_id (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        doc_type_id=doc_type_id,
        document_id=document_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    doc_type_id: str,
    document_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Soft deletes a test document, by ID.

    Args:
        doc_type_id (str):
        document_id (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        doc_type_id=doc_type_id,
        document_id=document_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
