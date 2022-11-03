from typing import Any, Dict

import httpx

from ...client import AuthenticatedClient
from ...models.training_document_details_dto import TrainingDocumentDetailsDto
from ...types import Response


def _get_kwargs(
    id: str,
    document_id: str,
    *,
    client: AuthenticatedClient,
    json_body: TrainingDocumentDetailsDto,
) -> Dict[str, Any]:
    url = "{}/api/internal/models/{id}/training_documents/{documentId}/labels".format(
        client.base_url, id=id, documentId=document_id
    )

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


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    id: str,
    document_id: str,
    *,
    client: AuthenticatedClient,
    json_body: TrainingDocumentDetailsDto,
) -> Response[Any]:
    """Update labels for a specific document

    Args:
        id (str):
        document_id (str):
        json_body (TrainingDocumentDetailsDto):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        document_id=document_id,
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
    document_id: str,
    *,
    client: AuthenticatedClient,
    json_body: TrainingDocumentDetailsDto,
) -> Response[Any]:
    """Update labels for a specific document

    Args:
        id (str):
        document_id (str):
        json_body (TrainingDocumentDetailsDto):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        document_id=document_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
