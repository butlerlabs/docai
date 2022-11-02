from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.extract_document_extra_results_item import ExtractDocumentExtraResultsItem
from ...models.extract_document_multipart_data import ExtractDocumentMultipartData
from ...models.extraction_results_dto import ExtractionResultsDto
from ...models.single_file_url_upload_dto import SingleFileUrlUploadDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    multipart_data: ExtractDocumentMultipartData,
    json_body: SingleFileUrlUploadDto,
    extra_results: Union[Unset, None, List[ExtractDocumentExtraResultsItem]] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/queues/{queueId}/documents".format(client.base_url, queueId=queue_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[ExtractionResultsDto]:
    if response.status_code == 201:
        response_201 = ExtractionResultsDto.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[ExtractionResultsDto]:
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
    multipart_data: ExtractDocumentMultipartData,
    json_body: SingleFileUrlUploadDto,
    extra_results: Union[Unset, None, List[ExtractDocumentExtraResultsItem]] = UNSET,
) -> Response[ExtractionResultsDto]:
    """Upload a single document to the queue specified by <queueId> and returns the extracted results

    Args:
        queue_id (str):
        extra_results (Union[Unset, None, List[ExtractDocumentExtraResultsItem]]):
        multipart_data (ExtractDocumentMultipartData):
        json_body (SingleFileUrlUploadDto):

    Returns:
        Response[ExtractionResultsDto]
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
    multipart_data: ExtractDocumentMultipartData,
    json_body: SingleFileUrlUploadDto,
    extra_results: Union[Unset, None, List[ExtractDocumentExtraResultsItem]] = UNSET,
) -> Optional[ExtractionResultsDto]:
    """Upload a single document to the queue specified by <queueId> and returns the extracted results

    Args:
        queue_id (str):
        extra_results (Union[Unset, None, List[ExtractDocumentExtraResultsItem]]):
        multipart_data (ExtractDocumentMultipartData):
        json_body (SingleFileUrlUploadDto):

    Returns:
        Response[ExtractionResultsDto]
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
    multipart_data: ExtractDocumentMultipartData,
    json_body: SingleFileUrlUploadDto,
    extra_results: Union[Unset, None, List[ExtractDocumentExtraResultsItem]] = UNSET,
) -> Response[ExtractionResultsDto]:
    """Upload a single document to the queue specified by <queueId> and returns the extracted results

    Args:
        queue_id (str):
        extra_results (Union[Unset, None, List[ExtractDocumentExtraResultsItem]]):
        multipart_data (ExtractDocumentMultipartData):
        json_body (SingleFileUrlUploadDto):

    Returns:
        Response[ExtractionResultsDto]
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
    multipart_data: ExtractDocumentMultipartData,
    json_body: SingleFileUrlUploadDto,
    extra_results: Union[Unset, None, List[ExtractDocumentExtraResultsItem]] = UNSET,
) -> Optional[ExtractionResultsDto]:
    """Upload a single document to the queue specified by <queueId> and returns the extracted results

    Args:
        queue_id (str):
        extra_results (Union[Unset, None, List[ExtractDocumentExtraResultsItem]]):
        multipart_data (ExtractDocumentMultipartData):
        json_body (SingleFileUrlUploadDto):

    Returns:
        Response[ExtractionResultsDto]
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
