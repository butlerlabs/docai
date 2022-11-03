from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.labeling_results_with_blocks_dto import LabelingResultsWithBlocksDto
from ...models.update_document_labels_response_dto import UpdateDocumentLabelsResponseDto
from ...types import Response


def _get_kwargs(
    queue_id: str,
    document_id: str,
    *,
    client: AuthenticatedClient,
    json_body: LabelingResultsWithBlocksDto,
) -> Dict[str, Any]:
    url = "{}/api/internal/queues/{queueId}/documents/{documentId}/labeling_result".format(
        client.base_url, queueId=queue_id, documentId=document_id
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


def _parse_response(*, response: httpx.Response) -> Optional[UpdateDocumentLabelsResponseDto]:
    if response.status_code == 201:
        response_201 = UpdateDocumentLabelsResponseDto.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[UpdateDocumentLabelsResponseDto]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    queue_id: str,
    document_id: str,
    *,
    client: AuthenticatedClient,
    json_body: LabelingResultsWithBlocksDto,
) -> Response[UpdateDocumentLabelsResponseDto]:
    """Add or update the labels of a document.

    Args:
        queue_id (str):
        document_id (str):
        json_body (LabelingResultsWithBlocksDto):

    Returns:
        Response[UpdateDocumentLabelsResponseDto]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
        document_id=document_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    queue_id: str,
    document_id: str,
    *,
    client: AuthenticatedClient,
    json_body: LabelingResultsWithBlocksDto,
) -> Optional[UpdateDocumentLabelsResponseDto]:
    """Add or update the labels of a document.

    Args:
        queue_id (str):
        document_id (str):
        json_body (LabelingResultsWithBlocksDto):

    Returns:
        Response[UpdateDocumentLabelsResponseDto]
    """

    return sync_detailed(
        queue_id=queue_id,
        document_id=document_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    queue_id: str,
    document_id: str,
    *,
    client: AuthenticatedClient,
    json_body: LabelingResultsWithBlocksDto,
) -> Response[UpdateDocumentLabelsResponseDto]:
    """Add or update the labels of a document.

    Args:
        queue_id (str):
        document_id (str):
        json_body (LabelingResultsWithBlocksDto):

    Returns:
        Response[UpdateDocumentLabelsResponseDto]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
        document_id=document_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    queue_id: str,
    document_id: str,
    *,
    client: AuthenticatedClient,
    json_body: LabelingResultsWithBlocksDto,
) -> Optional[UpdateDocumentLabelsResponseDto]:
    """Add or update the labels of a document.

    Args:
        queue_id (str):
        document_id (str):
        json_body (LabelingResultsWithBlocksDto):

    Returns:
        Response[UpdateDocumentLabelsResponseDto]
    """

    return (
        await asyncio_detailed(
            queue_id=queue_id,
            document_id=document_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
