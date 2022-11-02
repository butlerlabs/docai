from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.upload_documents_app_run_response_dto import UploadDocumentsAppRunResponseDto
from ...models.upload_documents_extra_results_item import UploadDocumentsExtraResultsItem
from ...models.upload_documents_multipart_data import UploadDocumentsMultipartData
from ...types import UNSET, Response, Unset


def _get_kwargs(
    app_id: str,
    *,
    client: AuthenticatedClient,
    multipart_data: UploadDocumentsMultipartData,
    extra_results: Union[Unset, None, List[UploadDocumentsExtraResultsItem]] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/apps/{appId}/upload_documents".format(client.base_url, appId=app_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[UploadDocumentsAppRunResponseDto]:
    if response.status_code == 201:
        response_201 = UploadDocumentsAppRunResponseDto.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[UploadDocumentsAppRunResponseDto]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    app_id: str,
    *,
    client: AuthenticatedClient,
    multipart_data: UploadDocumentsMultipartData,
    extra_results: Union[Unset, None, List[UploadDocumentsExtraResultsItem]] = UNSET,
) -> Response[UploadDocumentsAppRunResponseDto]:
    """Upload documents (PDFs, and image formats) to your app to start an extraction job. Returns an
    appRunId that can be used to check the status of the extraction job, and get its results

    Args:
        app_id (str):
        extra_results (Union[Unset, None, List[UploadDocumentsExtraResultsItem]]):
        multipart_data (UploadDocumentsMultipartData):

    Returns:
        Response[UploadDocumentsAppRunResponseDto]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        client=client,
        multipart_data=multipart_data,
        extra_results=extra_results,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    app_id: str,
    *,
    client: AuthenticatedClient,
    multipart_data: UploadDocumentsMultipartData,
    extra_results: Union[Unset, None, List[UploadDocumentsExtraResultsItem]] = UNSET,
) -> Optional[UploadDocumentsAppRunResponseDto]:
    """Upload documents (PDFs, and image formats) to your app to start an extraction job. Returns an
    appRunId that can be used to check the status of the extraction job, and get its results

    Args:
        app_id (str):
        extra_results (Union[Unset, None, List[UploadDocumentsExtraResultsItem]]):
        multipart_data (UploadDocumentsMultipartData):

    Returns:
        Response[UploadDocumentsAppRunResponseDto]
    """

    return sync_detailed(
        app_id=app_id,
        client=client,
        multipart_data=multipart_data,
        extra_results=extra_results,
    ).parsed


async def asyncio_detailed(
    app_id: str,
    *,
    client: AuthenticatedClient,
    multipart_data: UploadDocumentsMultipartData,
    extra_results: Union[Unset, None, List[UploadDocumentsExtraResultsItem]] = UNSET,
) -> Response[UploadDocumentsAppRunResponseDto]:
    """Upload documents (PDFs, and image formats) to your app to start an extraction job. Returns an
    appRunId that can be used to check the status of the extraction job, and get its results

    Args:
        app_id (str):
        extra_results (Union[Unset, None, List[UploadDocumentsExtraResultsItem]]):
        multipart_data (UploadDocumentsMultipartData):

    Returns:
        Response[UploadDocumentsAppRunResponseDto]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        client=client,
        multipart_data=multipart_data,
        extra_results=extra_results,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    app_id: str,
    *,
    client: AuthenticatedClient,
    multipart_data: UploadDocumentsMultipartData,
    extra_results: Union[Unset, None, List[UploadDocumentsExtraResultsItem]] = UNSET,
) -> Optional[UploadDocumentsAppRunResponseDto]:
    """Upload documents (PDFs, and image formats) to your app to start an extraction job. Returns an
    appRunId that can be used to check the status of the extraction job, and get its results

    Args:
        app_id (str):
        extra_results (Union[Unset, None, List[UploadDocumentsExtraResultsItem]]):
        multipart_data (UploadDocumentsMultipartData):

    Returns:
        Response[UploadDocumentsAppRunResponseDto]
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            client=client,
            multipart_data=multipart_data,
            extra_results=extra_results,
        )
    ).parsed
