from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.industry_tag import IndustryTag
from ...models.library_model_sort_by import LibraryModelSortBy
from ...models.paginated_library_model_dto import PaginatedLibraryModelDto
from ...models.sort_order import SortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    after_id: Union[Unset, None, str] = UNSET,
    before_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    sort_order: Union[Unset, None, SortOrder] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    industry: Union[Unset, None, IndustryTag] = UNSET,
    sort_by: Union[Unset, None, LibraryModelSortBy] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/internal/model_library".format(client.base_url)

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

    params["name"] = name

    json_industry: Union[Unset, None, str] = UNSET
    if not isinstance(industry, Unset):
        json_industry = industry.value if industry else None

    params["industry"] = json_industry

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


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedLibraryModelDto]:
    if response.status_code == 200:
        response_200 = PaginatedLibraryModelDto.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedLibraryModelDto]:
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
    name: Union[Unset, None, str] = UNSET,
    industry: Union[Unset, None, IndustryTag] = UNSET,
    sort_by: Union[Unset, None, LibraryModelSortBy] = UNSET,
) -> Response[PaginatedLibraryModelDto]:
    """Get a page of library models

    Args:
        after_id (Union[Unset, None, str]):
        before_id (Union[Unset, None, str]):
        limit (Union[Unset, None, float]):
        sort_order (Union[Unset, None, SortOrder]):
        name (Union[Unset, None, str]):
        industry (Union[Unset, None, IndustryTag]):
        sort_by (Union[Unset, None, LibraryModelSortBy]):

    Returns:
        Response[PaginatedLibraryModelDto]
    """

    kwargs = _get_kwargs(
        client=client,
        after_id=after_id,
        before_id=before_id,
        limit=limit,
        sort_order=sort_order,
        name=name,
        industry=industry,
        sort_by=sort_by,
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
    name: Union[Unset, None, str] = UNSET,
    industry: Union[Unset, None, IndustryTag] = UNSET,
    sort_by: Union[Unset, None, LibraryModelSortBy] = UNSET,
) -> Optional[PaginatedLibraryModelDto]:
    """Get a page of library models

    Args:
        after_id (Union[Unset, None, str]):
        before_id (Union[Unset, None, str]):
        limit (Union[Unset, None, float]):
        sort_order (Union[Unset, None, SortOrder]):
        name (Union[Unset, None, str]):
        industry (Union[Unset, None, IndustryTag]):
        sort_by (Union[Unset, None, LibraryModelSortBy]):

    Returns:
        Response[PaginatedLibraryModelDto]
    """

    return sync_detailed(
        client=client,
        after_id=after_id,
        before_id=before_id,
        limit=limit,
        sort_order=sort_order,
        name=name,
        industry=industry,
        sort_by=sort_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    after_id: Union[Unset, None, str] = UNSET,
    before_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    sort_order: Union[Unset, None, SortOrder] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    industry: Union[Unset, None, IndustryTag] = UNSET,
    sort_by: Union[Unset, None, LibraryModelSortBy] = UNSET,
) -> Response[PaginatedLibraryModelDto]:
    """Get a page of library models

    Args:
        after_id (Union[Unset, None, str]):
        before_id (Union[Unset, None, str]):
        limit (Union[Unset, None, float]):
        sort_order (Union[Unset, None, SortOrder]):
        name (Union[Unset, None, str]):
        industry (Union[Unset, None, IndustryTag]):
        sort_by (Union[Unset, None, LibraryModelSortBy]):

    Returns:
        Response[PaginatedLibraryModelDto]
    """

    kwargs = _get_kwargs(
        client=client,
        after_id=after_id,
        before_id=before_id,
        limit=limit,
        sort_order=sort_order,
        name=name,
        industry=industry,
        sort_by=sort_by,
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
    name: Union[Unset, None, str] = UNSET,
    industry: Union[Unset, None, IndustryTag] = UNSET,
    sort_by: Union[Unset, None, LibraryModelSortBy] = UNSET,
) -> Optional[PaginatedLibraryModelDto]:
    """Get a page of library models

    Args:
        after_id (Union[Unset, None, str]):
        before_id (Union[Unset, None, str]):
        limit (Union[Unset, None, float]):
        sort_order (Union[Unset, None, SortOrder]):
        name (Union[Unset, None, str]):
        industry (Union[Unset, None, IndustryTag]):
        sort_by (Union[Unset, None, LibraryModelSortBy]):

    Returns:
        Response[PaginatedLibraryModelDto]
    """

    return (
        await asyncio_detailed(
            client=client,
            after_id=after_id,
            before_id=before_id,
            limit=limit,
            sort_order=sort_order,
            name=name,
            industry=industry,
            sort_by=sort_by,
        )
    ).parsed
