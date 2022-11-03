from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.document_lock_dto import DocumentLockDto
from ...types import Response


def _get_kwargs(
    document_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/internal/butler_ops/labeling/{documentId}/refresh_lock".format(
        client.base_url, documentId=document_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[DocumentLockDto]:
    if response.status_code == 200:
        response_200 = DocumentLockDto.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[DocumentLockDto]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    document_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[DocumentLockDto]:
    """Refresh an existing lock on a document

    Args:
        document_id (str):

    Returns:
        Response[DocumentLockDto]
    """

    kwargs = _get_kwargs(
        document_id=document_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    document_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[DocumentLockDto]:
    """Refresh an existing lock on a document

    Args:
        document_id (str):

    Returns:
        Response[DocumentLockDto]
    """

    return sync_detailed(
        document_id=document_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    document_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[DocumentLockDto]:
    """Refresh an existing lock on a document

    Args:
        document_id (str):

    Returns:
        Response[DocumentLockDto]
    """

    kwargs = _get_kwargs(
        document_id=document_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    document_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[DocumentLockDto]:
    """Refresh an existing lock on a document

    Args:
        document_id (str):

    Returns:
        Response[DocumentLockDto]
    """

    return (
        await asyncio_detailed(
            document_id=document_id,
            client=client,
        )
    ).parsed
