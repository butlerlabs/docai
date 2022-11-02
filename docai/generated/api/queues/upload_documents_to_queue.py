from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.multiple_file_url_upload_dto import MultipleFileUrlUploadDto
from ...models.upload_documents_to_queue_extra_results_item import UploadDocumentsToQueueExtraResultsItem
from ...models.upload_documents_to_queue_multipart_data import UploadDocumentsToQueueMultipartData
from ...models.upload_documents_upload_response_dto import UploadDocumentsUploadResponseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    multipart_data: UploadDocumentsToQueueMultipartData,
    json_body: MultipleFileUrlUploadDto,
    extra_results: Union[Unset, None, List[UploadDocumentsToQueueExtraResultsItem]] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/queues/{queueId}/uploads".format(client.base_url, queueId=queue_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_extra_results: Union[Unset, None, List[str]] = UNSET
    if not isinstance(extra_results, Unset):
        if extra_results is None:
            json_extra_results = None
        else:
            json_extra_results = []
            for extra_results_item_data in extra_results:
                extra_results_item = extra_results_item_data.value

                json_extra_results.append(extra_results_item)

    params["extraResults"] = json_extra_results

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_body.to_dict()

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[UploadDocumentsUploadResponseDto]:
    if response.status_code == 201:
        response_201 = UploadDocumentsUploadResponseDto.from_dict(response.json())

        return response_201
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
    multipart_data: UploadDocumentsToQueueMultipartData,
    json_body: MultipleFileUrlUploadDto,
    extra_results: Union[Unset, None, List[UploadDocumentsToQueueExtraResultsItem]] = UNSET,
) -> Response[UploadDocumentsUploadResponseDto]:
    """Upload documents to the queue specified by <queueId> for processing

    Args:
        queue_id (str):
        extra_results (Union[Unset, None, List[UploadDocumentsToQueueExtraResultsItem]]):
        multipart_data (UploadDocumentsToQueueMultipartData):
        json_body (MultipleFileUrlUploadDto):

    Returns:
        Response[UploadDocumentsUploadResponseDto]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
        client=client,
        multipart_data=multipart_data,
        json_body=json_body,
        extra_results=extra_results,
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
    multipart_data: UploadDocumentsToQueueMultipartData,
    json_body: MultipleFileUrlUploadDto,
    extra_results: Union[Unset, None, List[UploadDocumentsToQueueExtraResultsItem]] = UNSET,
) -> Optional[UploadDocumentsUploadResponseDto]:
    """Upload documents to the queue specified by <queueId> for processing

    Args:
        queue_id (str):
        extra_results (Union[Unset, None, List[UploadDocumentsToQueueExtraResultsItem]]):
        multipart_data (UploadDocumentsToQueueMultipartData):
        json_body (MultipleFileUrlUploadDto):

    Returns:
        Response[UploadDocumentsUploadResponseDto]
    """

    return sync_detailed(
        queue_id=queue_id,
        client=client,
        multipart_data=multipart_data,
        json_body=json_body,
        extra_results=extra_results,
    ).parsed


async def asyncio_detailed(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    multipart_data: UploadDocumentsToQueueMultipartData,
    json_body: MultipleFileUrlUploadDto,
    extra_results: Union[Unset, None, List[UploadDocumentsToQueueExtraResultsItem]] = UNSET,
) -> Response[UploadDocumentsUploadResponseDto]:
    """Upload documents to the queue specified by <queueId> for processing

    Args:
        queue_id (str):
        extra_results (Union[Unset, None, List[UploadDocumentsToQueueExtraResultsItem]]):
        multipart_data (UploadDocumentsToQueueMultipartData):
        json_body (MultipleFileUrlUploadDto):

    Returns:
        Response[UploadDocumentsUploadResponseDto]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
        client=client,
        multipart_data=multipart_data,
        json_body=json_body,
        extra_results=extra_results,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    multipart_data: UploadDocumentsToQueueMultipartData,
    json_body: MultipleFileUrlUploadDto,
    extra_results: Union[Unset, None, List[UploadDocumentsToQueueExtraResultsItem]] = UNSET,
) -> Optional[UploadDocumentsUploadResponseDto]:
    """Upload documents to the queue specified by <queueId> for processing

    Args:
        queue_id (str):
        extra_results (Union[Unset, None, List[UploadDocumentsToQueueExtraResultsItem]]):
        multipart_data (UploadDocumentsToQueueMultipartData):
        json_body (MultipleFileUrlUploadDto):

    Returns:
        Response[UploadDocumentsUploadResponseDto]
    """

    return (
        await asyncio_detailed(
            queue_id=queue_id,
            client=client,
            multipart_data=multipart_data,
            json_body=json_body,
            extra_results=extra_results,
        )
    ).parsed
