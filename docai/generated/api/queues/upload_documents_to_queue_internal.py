from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.upload_documents_to_queue_internal_multipart_data import UploadDocumentsToQueueInternalMultipartData
from ...models.upload_documents_upload_response_dto import UploadDocumentsUploadResponseDto
from ...types import Response


def _get_kwargs(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    multipart_data: UploadDocumentsToQueueInternalMultipartData,
) -> Dict[str, Any]:
    url = "{}/api/internal/queues/{queueId}/uploads".format(client.base_url, queueId=queue_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
    }


def _parse_response(*, response: httpx.Response) -> Optional[UploadDocumentsUploadResponseDto]:
    if response.status_code == 200:
        response_200 = UploadDocumentsUploadResponseDto.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[UploadDocumentsUploadResponseDto]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    multipart_data: UploadDocumentsToQueueInternalMultipartData,
) -> Response[UploadDocumentsUploadResponseDto]:
    """Upload documents to the queue specified by <queueId> for processing

    Args:
        queue_id (str):
        multipart_data (UploadDocumentsToQueueInternalMultipartData):

    Returns:
        Response[UploadDocumentsUploadResponseDto]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
        client=client,
        multipart_data=multipart_data,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    multipart_data: UploadDocumentsToQueueInternalMultipartData,
) -> Optional[UploadDocumentsUploadResponseDto]:
    """Upload documents to the queue specified by <queueId> for processing

    Args:
        queue_id (str):
        multipart_data (UploadDocumentsToQueueInternalMultipartData):

    Returns:
        Response[UploadDocumentsUploadResponseDto]
    """

    return sync_detailed(
        queue_id=queue_id,
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    multipart_data: UploadDocumentsToQueueInternalMultipartData,
) -> Response[UploadDocumentsUploadResponseDto]:
    """Upload documents to the queue specified by <queueId> for processing

    Args:
        queue_id (str):
        multipart_data (UploadDocumentsToQueueInternalMultipartData):

    Returns:
        Response[UploadDocumentsUploadResponseDto]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
        client=client,
        multipart_data=multipart_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    multipart_data: UploadDocumentsToQueueInternalMultipartData,
) -> Optional[UploadDocumentsUploadResponseDto]:
    """Upload documents to the queue specified by <queueId> for processing

    Args:
        queue_id (str):
        multipart_data (UploadDocumentsToQueueInternalMultipartData):

    Returns:
        Response[UploadDocumentsUploadResponseDto]
    """

    return (
        await asyncio_detailed(
            queue_id=queue_id,
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
