from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.extraction_results_sort_by import ExtractionResultsSortBy
from ...models.get_extraction_results_extra_results_item import GetExtractionResultsExtraResultsItem
from ...models.paginated_extraction_results_dto import PaginatedExtractionResultsDto
from ...models.sort_order import SortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    after_id: Union[Unset, None, str] = UNSET,
    before_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    sort_order: Union[Unset, None, SortOrder] = UNSET,
    upload_id: str,
    extra_results: Union[Unset, None, List[GetExtractionResultsExtraResultsItem]] = UNSET,
    sort_by: Union[Unset, None, ExtractionResultsSortBy] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/queues/{queueId}/extraction_results".format(client.base_url, queueId=queue_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["afterId"] = after_id

    params["beforeId"] = before_id

    params["limit"] = limit

    json_sort_order: Union[Unset, None, str] = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value if sort_order else None

    params["sortOrder"] = json_sort_order

    params["uploadId"] = upload_id

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

    json_sort_by: Union[Unset, None, str] = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value if sort_by else None

    params["sortBy"] = json_sort_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedExtractionResultsDto]:
    if response.status_code == 200:
        response_200 = PaginatedExtractionResultsDto.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedExtractionResultsDto]:
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
    after_id: Union[Unset, None, str] = UNSET,
    before_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    sort_order: Union[Unset, None, SortOrder] = UNSET,
    upload_id: str,
    extra_results: Union[Unset, None, List[GetExtractionResultsExtraResultsItem]] = UNSET,
    sort_by: Union[Unset, None, ExtractionResultsSortBy] = UNSET,
) -> Response[PaginatedExtractionResultsDto]:
    """Get paginated list of extraction results for documents matching the query params

    Args:
        queue_id (str):
        after_id (Union[Unset, None, str]):
        before_id (Union[Unset, None, str]):
        limit (Union[Unset, None, float]):
        sort_order (Union[Unset, None, SortOrder]):
        upload_id (str):
        extra_results (Union[Unset, None, List[GetExtractionResultsExtraResultsItem]]):
        sort_by (Union[Unset, None, ExtractionResultsSortBy]):

    Returns:
        Response[PaginatedExtractionResultsDto]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
        client=client,
        after_id=after_id,
        before_id=before_id,
        limit=limit,
        sort_order=sort_order,
        upload_id=upload_id,
        extra_results=extra_results,
        sort_by=sort_by,
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
    after_id: Union[Unset, None, str] = UNSET,
    before_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    sort_order: Union[Unset, None, SortOrder] = UNSET,
    upload_id: str,
    extra_results: Union[Unset, None, List[GetExtractionResultsExtraResultsItem]] = UNSET,
    sort_by: Union[Unset, None, ExtractionResultsSortBy] = UNSET,
) -> Optional[PaginatedExtractionResultsDto]:
    """Get paginated list of extraction results for documents matching the query params

    Args:
        queue_id (str):
        after_id (Union[Unset, None, str]):
        before_id (Union[Unset, None, str]):
        limit (Union[Unset, None, float]):
        sort_order (Union[Unset, None, SortOrder]):
        upload_id (str):
        extra_results (Union[Unset, None, List[GetExtractionResultsExtraResultsItem]]):
        sort_by (Union[Unset, None, ExtractionResultsSortBy]):

    Returns:
        Response[PaginatedExtractionResultsDto]
    """

    return sync_detailed(
        queue_id=queue_id,
        client=client,
        after_id=after_id,
        before_id=before_id,
        limit=limit,
        sort_order=sort_order,
        upload_id=upload_id,
        extra_results=extra_results,
        sort_by=sort_by,
    ).parsed


async def asyncio_detailed(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    after_id: Union[Unset, None, str] = UNSET,
    before_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    sort_order: Union[Unset, None, SortOrder] = UNSET,
    upload_id: str,
    extra_results: Union[Unset, None, List[GetExtractionResultsExtraResultsItem]] = UNSET,
    sort_by: Union[Unset, None, ExtractionResultsSortBy] = UNSET,
) -> Response[PaginatedExtractionResultsDto]:
    """Get paginated list of extraction results for documents matching the query params

    Args:
        queue_id (str):
        after_id (Union[Unset, None, str]):
        before_id (Union[Unset, None, str]):
        limit (Union[Unset, None, float]):
        sort_order (Union[Unset, None, SortOrder]):
        upload_id (str):
        extra_results (Union[Unset, None, List[GetExtractionResultsExtraResultsItem]]):
        sort_by (Union[Unset, None, ExtractionResultsSortBy]):

    Returns:
        Response[PaginatedExtractionResultsDto]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
        client=client,
        after_id=after_id,
        before_id=before_id,
        limit=limit,
        sort_order=sort_order,
        upload_id=upload_id,
        extra_results=extra_results,
        sort_by=sort_by,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    after_id: Union[Unset, None, str] = UNSET,
    before_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    sort_order: Union[Unset, None, SortOrder] = UNSET,
    upload_id: str,
    extra_results: Union[Unset, None, List[GetExtractionResultsExtraResultsItem]] = UNSET,
    sort_by: Union[Unset, None, ExtractionResultsSortBy] = UNSET,
) -> Optional[PaginatedExtractionResultsDto]:
    """Get paginated list of extraction results for documents matching the query params

    Args:
        queue_id (str):
        after_id (Union[Unset, None, str]):
        before_id (Union[Unset, None, str]):
        limit (Union[Unset, None, float]):
        sort_order (Union[Unset, None, SortOrder]):
        upload_id (str):
        extra_results (Union[Unset, None, List[GetExtractionResultsExtraResultsItem]]):
        sort_by (Union[Unset, None, ExtractionResultsSortBy]):

    Returns:
        Response[PaginatedExtractionResultsDto]
    """

    return (
        await asyncio_detailed(
            queue_id=queue_id,
            client=client,
            after_id=after_id,
            before_id=before_id,
            limit=limit,
            sort_order=sort_order,
            upload_id=upload_id,
            extra_results=extra_results,
            sort_by=sort_by,
        )
    ).parsed
