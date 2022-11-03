from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.paginated_test_document_detail_dto import PaginatedTestDocumentDetailDto
from ...models.sort_order import SortOrder
from ...models.test_document_sort_by import TestDocumentSortBy
from ...models.test_document_status_filter import TestDocumentStatusFilter
from ...types import UNSET, Response, Unset


def _get_kwargs(
    doc_type_id: str,
    *,
    client: AuthenticatedClient,
    after_id: Union[Unset, None, str] = UNSET,
    before_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    sort_order: Union[Unset, None, SortOrder] = UNSET,
    sort_by: Union[Unset, None, TestDocumentSortBy] = UNSET,
    status: Union[Unset, None, TestDocumentStatusFilter] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/internal/document_types/{docTypeId}/test_documents".format(client.base_url, docTypeId=doc_type_id)

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

    json_status: Union[Unset, None, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value if status else None

    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedTestDocumentDetailDto]:
    if response.status_code == 200:
        response_200 = PaginatedTestDocumentDetailDto.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedTestDocumentDetailDto]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    doc_type_id: str,
    *,
    client: AuthenticatedClient,
    after_id: Union[Unset, None, str] = UNSET,
    before_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    sort_order: Union[Unset, None, SortOrder] = UNSET,
    sort_by: Union[Unset, None, TestDocumentSortBy] = UNSET,
    status: Union[Unset, None, TestDocumentStatusFilter] = UNSET,
) -> Response[PaginatedTestDocumentDetailDto]:
    """Get a paginated listing of Test documents for a document type by ID

    Args:
        doc_type_id (str):
        after_id (Union[Unset, None, str]):
        before_id (Union[Unset, None, str]):
        limit (Union[Unset, None, float]):
        sort_order (Union[Unset, None, SortOrder]):
        sort_by (Union[Unset, None, TestDocumentSortBy]):
        status (Union[Unset, None, TestDocumentStatusFilter]):

    Returns:
        Response[PaginatedTestDocumentDetailDto]
    """

    kwargs = _get_kwargs(
        doc_type_id=doc_type_id,
        client=client,
        after_id=after_id,
        before_id=before_id,
        limit=limit,
        sort_order=sort_order,
        sort_by=sort_by,
        status=status,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    doc_type_id: str,
    *,
    client: AuthenticatedClient,
    after_id: Union[Unset, None, str] = UNSET,
    before_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    sort_order: Union[Unset, None, SortOrder] = UNSET,
    sort_by: Union[Unset, None, TestDocumentSortBy] = UNSET,
    status: Union[Unset, None, TestDocumentStatusFilter] = UNSET,
) -> Optional[PaginatedTestDocumentDetailDto]:
    """Get a paginated listing of Test documents for a document type by ID

    Args:
        doc_type_id (str):
        after_id (Union[Unset, None, str]):
        before_id (Union[Unset, None, str]):
        limit (Union[Unset, None, float]):
        sort_order (Union[Unset, None, SortOrder]):
        sort_by (Union[Unset, None, TestDocumentSortBy]):
        status (Union[Unset, None, TestDocumentStatusFilter]):

    Returns:
        Response[PaginatedTestDocumentDetailDto]
    """

    return sync_detailed(
        doc_type_id=doc_type_id,
        client=client,
        after_id=after_id,
        before_id=before_id,
        limit=limit,
        sort_order=sort_order,
        sort_by=sort_by,
        status=status,
    ).parsed


async def asyncio_detailed(
    doc_type_id: str,
    *,
    client: AuthenticatedClient,
    after_id: Union[Unset, None, str] = UNSET,
    before_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    sort_order: Union[Unset, None, SortOrder] = UNSET,
    sort_by: Union[Unset, None, TestDocumentSortBy] = UNSET,
    status: Union[Unset, None, TestDocumentStatusFilter] = UNSET,
) -> Response[PaginatedTestDocumentDetailDto]:
    """Get a paginated listing of Test documents for a document type by ID

    Args:
        doc_type_id (str):
        after_id (Union[Unset, None, str]):
        before_id (Union[Unset, None, str]):
        limit (Union[Unset, None, float]):
        sort_order (Union[Unset, None, SortOrder]):
        sort_by (Union[Unset, None, TestDocumentSortBy]):
        status (Union[Unset, None, TestDocumentStatusFilter]):

    Returns:
        Response[PaginatedTestDocumentDetailDto]
    """

    kwargs = _get_kwargs(
        doc_type_id=doc_type_id,
        client=client,
        after_id=after_id,
        before_id=before_id,
        limit=limit,
        sort_order=sort_order,
        sort_by=sort_by,
        status=status,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    doc_type_id: str,
    *,
    client: AuthenticatedClient,
    after_id: Union[Unset, None, str] = UNSET,
    before_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    sort_order: Union[Unset, None, SortOrder] = UNSET,
    sort_by: Union[Unset, None, TestDocumentSortBy] = UNSET,
    status: Union[Unset, None, TestDocumentStatusFilter] = UNSET,
) -> Optional[PaginatedTestDocumentDetailDto]:
    """Get a paginated listing of Test documents for a document type by ID

    Args:
        doc_type_id (str):
        after_id (Union[Unset, None, str]):
        before_id (Union[Unset, None, str]):
        limit (Union[Unset, None, float]):
        sort_order (Union[Unset, None, SortOrder]):
        sort_by (Union[Unset, None, TestDocumentSortBy]):
        status (Union[Unset, None, TestDocumentStatusFilter]):

    Returns:
        Response[PaginatedTestDocumentDetailDto]
    """

    return (
        await asyncio_detailed(
            doc_type_id=doc_type_id,
            client=client,
            after_id=after_id,
            before_id=before_id,
            limit=limit,
            sort_order=sort_order,
            sort_by=sort_by,
            status=status,
        )
    ).parsed
