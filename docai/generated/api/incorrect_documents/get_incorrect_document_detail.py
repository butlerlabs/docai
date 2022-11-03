from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.incorrect_document_detail_dto import IncorrectDocumentDetailDto
from ...types import Response


def _get_kwargs(
    doc_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/internal/incorrect_documents/{docId}".format(client.base_url, docId=doc_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[IncorrectDocumentDetailDto]:
    if response.status_code == 200:
        response_200 = IncorrectDocumentDetailDto.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[IncorrectDocumentDetailDto]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    doc_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[IncorrectDocumentDetailDto]:
    """
    Args:
        doc_id (str):

    Returns:
        Response[IncorrectDocumentDetailDto]
    """

    kwargs = _get_kwargs(
        doc_id=doc_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    doc_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[IncorrectDocumentDetailDto]:
    """
    Args:
        doc_id (str):

    Returns:
        Response[IncorrectDocumentDetailDto]
    """

    return sync_detailed(
        doc_id=doc_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    doc_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[IncorrectDocumentDetailDto]:
    """
    Args:
        doc_id (str):

    Returns:
        Response[IncorrectDocumentDetailDto]
    """

    kwargs = _get_kwargs(
        doc_id=doc_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    doc_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[IncorrectDocumentDetailDto]:
    """
    Args:
        doc_id (str):

    Returns:
        Response[IncorrectDocumentDetailDto]
    """

    return (
        await asyncio_detailed(
            doc_id=doc_id,
            client=client,
        )
    ).parsed
