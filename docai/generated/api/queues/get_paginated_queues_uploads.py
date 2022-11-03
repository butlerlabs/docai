from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.paginated_queue_upload_dto import PaginatedQueueUploadDto
from ...models.queue_upload_filter_by_status import QueueUploadFilterByStatus
from ...models.queue_upload_sort_by import QueueUploadSortBy
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
    sort_by: Union[Unset, None, QueueUploadSortBy] = UNSET,
    upload_status: Union[Unset, None, QueueUploadFilterByStatus] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/internal/queues/{queueId}/uploads".format(client.base_url, queueId=queue_id)

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

    json_sort_by: Union[Unset, None, str] = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value if sort_by else None

    params["sortBy"] = json_sort_by

    json_upload_status: Union[Unset, None, str] = UNSET
    if not isinstance(upload_status, Unset):
        json_upload_status = upload_status.value if upload_status else None

    params["uploadStatus"] = json_upload_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedQueueUploadDto]:
    if response.status_code == 200:
        response_200 = PaginatedQueueUploadDto.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedQueueUploadDto]:
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
    sort_by: Union[Unset, None, QueueUploadSortBy] = UNSET,
    upload_status: Union[Unset, None, QueueUploadFilterByStatus] = UNSET,
) -> Response[PaginatedQueueUploadDto]:
    """Get a paginated list of all uploads to a queue.

    Args:
        queue_id (str):
        after_id (Union[Unset, None, str]):
        before_id (Union[Unset, None, str]):
        limit (Union[Unset, None, float]):
        sort_order (Union[Unset, None, SortOrder]):
        sort_by (Union[Unset, None, QueueUploadSortBy]):
        upload_status (Union[Unset, None, QueueUploadFilterByStatus]):

    Returns:
        Response[PaginatedQueueUploadDto]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
        client=client,
        after_id=after_id,
        before_id=before_id,
        limit=limit,
        sort_order=sort_order,
        sort_by=sort_by,
        upload_status=upload_status,
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
    sort_by: Union[Unset, None, QueueUploadSortBy] = UNSET,
    upload_status: Union[Unset, None, QueueUploadFilterByStatus] = UNSET,
) -> Optional[PaginatedQueueUploadDto]:
    """Get a paginated list of all uploads to a queue.

    Args:
        queue_id (str):
        after_id (Union[Unset, None, str]):
        before_id (Union[Unset, None, str]):
        limit (Union[Unset, None, float]):
        sort_order (Union[Unset, None, SortOrder]):
        sort_by (Union[Unset, None, QueueUploadSortBy]):
        upload_status (Union[Unset, None, QueueUploadFilterByStatus]):

    Returns:
        Response[PaginatedQueueUploadDto]
    """

    return sync_detailed(
        queue_id=queue_id,
        client=client,
        after_id=after_id,
        before_id=before_id,
        limit=limit,
        sort_order=sort_order,
        sort_by=sort_by,
        upload_status=upload_status,
    ).parsed


async def asyncio_detailed(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    after_id: Union[Unset, None, str] = UNSET,
    before_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    sort_order: Union[Unset, None, SortOrder] = UNSET,
    sort_by: Union[Unset, None, QueueUploadSortBy] = UNSET,
    upload_status: Union[Unset, None, QueueUploadFilterByStatus] = UNSET,
) -> Response[PaginatedQueueUploadDto]:
    """Get a paginated list of all uploads to a queue.

    Args:
        queue_id (str):
        after_id (Union[Unset, None, str]):
        before_id (Union[Unset, None, str]):
        limit (Union[Unset, None, float]):
        sort_order (Union[Unset, None, SortOrder]):
        sort_by (Union[Unset, None, QueueUploadSortBy]):
        upload_status (Union[Unset, None, QueueUploadFilterByStatus]):

    Returns:
        Response[PaginatedQueueUploadDto]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
        client=client,
        after_id=after_id,
        before_id=before_id,
        limit=limit,
        sort_order=sort_order,
        sort_by=sort_by,
        upload_status=upload_status,
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
    sort_by: Union[Unset, None, QueueUploadSortBy] = UNSET,
    upload_status: Union[Unset, None, QueueUploadFilterByStatus] = UNSET,
) -> Optional[PaginatedQueueUploadDto]:
    """Get a paginated list of all uploads to a queue.

    Args:
        queue_id (str):
        after_id (Union[Unset, None, str]):
        before_id (Union[Unset, None, str]):
        limit (Union[Unset, None, float]):
        sort_order (Union[Unset, None, SortOrder]):
        sort_by (Union[Unset, None, QueueUploadSortBy]):
        upload_status (Union[Unset, None, QueueUploadFilterByStatus]):

    Returns:
        Response[PaginatedQueueUploadDto]
    """

    return (
        await asyncio_detailed(
            queue_id=queue_id,
            client=client,
            after_id=after_id,
            before_id=before_id,
            limit=limit,
            sort_order=sort_order,
            sort_by=sort_by,
            upload_status=upload_status,
        )
    ).parsed
