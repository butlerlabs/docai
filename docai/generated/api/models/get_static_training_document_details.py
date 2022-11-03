from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.static_training_document_details_dto import StaticTrainingDocumentDetailsDto
from ...types import Response


def _get_kwargs(
    id: str,
    document_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/internal/models/{id}/training_documents/{documentId}/static".format(
        client.base_url, id=id, documentId=document_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[StaticTrainingDocumentDetailsDto]:
    if response.status_code == 200:
        response_200 = StaticTrainingDocumentDetailsDto.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[StaticTrainingDocumentDetailsDto]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    document_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[StaticTrainingDocumentDetailsDto]:
    """Get static training document details

    Args:
        id (str):
        document_id (str):

    Returns:
        Response[StaticTrainingDocumentDetailsDto]
    """

    kwargs = _get_kwargs(
        id=id,
        document_id=document_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    document_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[StaticTrainingDocumentDetailsDto]:
    """Get static training document details

    Args:
        id (str):
        document_id (str):

    Returns:
        Response[StaticTrainingDocumentDetailsDto]
    """

    return sync_detailed(
        id=id,
        document_id=document_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    document_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[StaticTrainingDocumentDetailsDto]:
    """Get static training document details

    Args:
        id (str):
        document_id (str):

    Returns:
        Response[StaticTrainingDocumentDetailsDto]
    """

    kwargs = _get_kwargs(
        id=id,
        document_id=document_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    document_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[StaticTrainingDocumentDetailsDto]:
    """Get static training document details

    Args:
        id (str):
        document_id (str):

    Returns:
        Response[StaticTrainingDocumentDetailsDto]
    """

    return (
        await asyncio_detailed(
            id=id,
            document_id=document_id,
            client=client,
        )
    ).parsed
