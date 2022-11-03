from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.incorrect_document_sort_by import IncorrectDocumentSortBy
from ...models.incorrect_status import IncorrectStatus
from ...models.paginated_incorrect_documents_dto import PaginatedIncorrectDocumentsDto
from ...models.sort_order import SortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    after_id: Union[Unset, None, str] = UNSET,
    before_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    sort_order: Union[Unset, None, SortOrder] = UNSET,
    sort_by: Union[Unset, None, IncorrectDocumentSortBy] = UNSET,
    doc_type_id: Union[Unset, None, str] = UNSET,
    reviewer_user_id: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, IncorrectStatus] = UNSET,
    review_time_gte: Union[Unset, None, float] = UNSET,
    review_time_lte: Union[Unset, None, float] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/internal/incorrect_documents".format(client.base_url)

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

    params["docTypeId"] = doc_type_id

    params["reviewerUserId"] = reviewer_user_id

    json_status: Union[Unset, None, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value if status else None

    params["status"] = json_status

    params["reviewTimeGte"] = review_time_gte

    params["reviewTimeLte"] = review_time_lte

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedIncorrectDocumentsDto]:
    if response.status_code == 200:
        response_200 = PaginatedIncorrectDocumentsDto.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedIncorrectDocumentsDto]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    after_id: Union[Unset, None, str] = UNSET,
    before_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    sort_order: Union[Unset, None, SortOrder] = UNSET,
    sort_by: Union[Unset, None, IncorrectDocumentSortBy] = UNSET,
    doc_type_id: Union[Unset, None, str] = UNSET,
    reviewer_user_id: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, IncorrectStatus] = UNSET,
    review_time_gte: Union[Unset, None, float] = UNSET,
    review_time_lte: Union[Unset, None, float] = UNSET,
) -> Response[PaginatedIncorrectDocumentsDto]:
    """
    Args:
        after_id (Union[Unset, None, str]):
        before_id (Union[Unset, None, str]):
        limit (Union[Unset, None, float]):
        sort_order (Union[Unset, None, SortOrder]):
        sort_by (Union[Unset, None, IncorrectDocumentSortBy]):
        doc_type_id (Union[Unset, None, str]):
        reviewer_user_id (Union[Unset, None, str]):
        status (Union[Unset, None, IncorrectStatus]):
        review_time_gte (Union[Unset, None, float]):
        review_time_lte (Union[Unset, None, float]):

    Returns:
        Response[PaginatedIncorrectDocumentsDto]
    """

    kwargs = _get_kwargs(
        client=client,
        after_id=after_id,
        before_id=before_id,
        limit=limit,
        sort_order=sort_order,
        sort_by=sort_by,
        doc_type_id=doc_type_id,
        reviewer_user_id=reviewer_user_id,
        status=status,
        review_time_gte=review_time_gte,
        review_time_lte=review_time_lte,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    after_id: Union[Unset, None, str] = UNSET,
    before_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    sort_order: Union[Unset, None, SortOrder] = UNSET,
    sort_by: Union[Unset, None, IncorrectDocumentSortBy] = UNSET,
    doc_type_id: Union[Unset, None, str] = UNSET,
    reviewer_user_id: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, IncorrectStatus] = UNSET,
    review_time_gte: Union[Unset, None, float] = UNSET,
    review_time_lte: Union[Unset, None, float] = UNSET,
) -> Optional[PaginatedIncorrectDocumentsDto]:
    """
    Args:
        after_id (Union[Unset, None, str]):
        before_id (Union[Unset, None, str]):
        limit (Union[Unset, None, float]):
        sort_order (Union[Unset, None, SortOrder]):
        sort_by (Union[Unset, None, IncorrectDocumentSortBy]):
        doc_type_id (Union[Unset, None, str]):
        reviewer_user_id (Union[Unset, None, str]):
        status (Union[Unset, None, IncorrectStatus]):
        review_time_gte (Union[Unset, None, float]):
        review_time_lte (Union[Unset, None, float]):

    Returns:
        Response[PaginatedIncorrectDocumentsDto]
    """

    return sync_detailed(
        client=client,
        after_id=after_id,
        before_id=before_id,
        limit=limit,
        sort_order=sort_order,
        sort_by=sort_by,
        doc_type_id=doc_type_id,
        reviewer_user_id=reviewer_user_id,
        status=status,
        review_time_gte=review_time_gte,
        review_time_lte=review_time_lte,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    after_id: Union[Unset, None, str] = UNSET,
    before_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    sort_order: Union[Unset, None, SortOrder] = UNSET,
    sort_by: Union[Unset, None, IncorrectDocumentSortBy] = UNSET,
    doc_type_id: Union[Unset, None, str] = UNSET,
    reviewer_user_id: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, IncorrectStatus] = UNSET,
    review_time_gte: Union[Unset, None, float] = UNSET,
    review_time_lte: Union[Unset, None, float] = UNSET,
) -> Response[PaginatedIncorrectDocumentsDto]:
    """
    Args:
        after_id (Union[Unset, None, str]):
        before_id (Union[Unset, None, str]):
        limit (Union[Unset, None, float]):
        sort_order (Union[Unset, None, SortOrder]):
        sort_by (Union[Unset, None, IncorrectDocumentSortBy]):
        doc_type_id (Union[Unset, None, str]):
        reviewer_user_id (Union[Unset, None, str]):
        status (Union[Unset, None, IncorrectStatus]):
        review_time_gte (Union[Unset, None, float]):
        review_time_lte (Union[Unset, None, float]):

    Returns:
        Response[PaginatedIncorrectDocumentsDto]
    """

    kwargs = _get_kwargs(
        client=client,
        after_id=after_id,
        before_id=before_id,
        limit=limit,
        sort_order=sort_order,
        sort_by=sort_by,
        doc_type_id=doc_type_id,
        reviewer_user_id=reviewer_user_id,
        status=status,
        review_time_gte=review_time_gte,
        review_time_lte=review_time_lte,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    after_id: Union[Unset, None, str] = UNSET,
    before_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    sort_order: Union[Unset, None, SortOrder] = UNSET,
    sort_by: Union[Unset, None, IncorrectDocumentSortBy] = UNSET,
    doc_type_id: Union[Unset, None, str] = UNSET,
    reviewer_user_id: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, IncorrectStatus] = UNSET,
    review_time_gte: Union[Unset, None, float] = UNSET,
    review_time_lte: Union[Unset, None, float] = UNSET,
) -> Optional[PaginatedIncorrectDocumentsDto]:
    """
    Args:
        after_id (Union[Unset, None, str]):
        before_id (Union[Unset, None, str]):
        limit (Union[Unset, None, float]):
        sort_order (Union[Unset, None, SortOrder]):
        sort_by (Union[Unset, None, IncorrectDocumentSortBy]):
        doc_type_id (Union[Unset, None, str]):
        reviewer_user_id (Union[Unset, None, str]):
        status (Union[Unset, None, IncorrectStatus]):
        review_time_gte (Union[Unset, None, float]):
        review_time_lte (Union[Unset, None, float]):

    Returns:
        Response[PaginatedIncorrectDocumentsDto]
    """

    return (
        await asyncio_detailed(
            client=client,
            after_id=after_id,
            before_id=before_id,
            limit=limit,
            sort_order=sort_order,
            sort_by=sort_by,
            doc_type_id=doc_type_id,
            reviewer_user_id=reviewer_user_id,
            status=status,
            review_time_gte=review_time_gte,
            review_time_lte=review_time_lte,
        )
    ).parsed
