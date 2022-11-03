from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.paginated_b_ops_management_doc_type_list_dto import PaginatedBOpsManagementDocTypeListDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    after_id: Union[Unset, None, str] = UNSET,
    before_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    doc_type_name_search_string: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/internal/butler_ops/management/document_types".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["afterId"] = after_id

    params["beforeId"] = before_id

    params["limit"] = limit

    params["docTypeNameSearchString"] = doc_type_name_search_string

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedBOpsManagementDocTypeListDto]:
    if response.status_code == 200:
        response_200 = PaginatedBOpsManagementDocTypeListDto.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedBOpsManagementDocTypeListDto]:
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
    doc_type_name_search_string: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedBOpsManagementDocTypeListDto]:
    """Get a list of all document types for use on the Butler Ops Management page

    Args:
        after_id (Union[Unset, None, str]):
        before_id (Union[Unset, None, str]):
        limit (Union[Unset, None, float]):
        doc_type_name_search_string (Union[Unset, None, str]):

    Returns:
        Response[PaginatedBOpsManagementDocTypeListDto]
    """

    kwargs = _get_kwargs(
        client=client,
        after_id=after_id,
        before_id=before_id,
        limit=limit,
        doc_type_name_search_string=doc_type_name_search_string,
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
    doc_type_name_search_string: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedBOpsManagementDocTypeListDto]:
    """Get a list of all document types for use on the Butler Ops Management page

    Args:
        after_id (Union[Unset, None, str]):
        before_id (Union[Unset, None, str]):
        limit (Union[Unset, None, float]):
        doc_type_name_search_string (Union[Unset, None, str]):

    Returns:
        Response[PaginatedBOpsManagementDocTypeListDto]
    """

    return sync_detailed(
        client=client,
        after_id=after_id,
        before_id=before_id,
        limit=limit,
        doc_type_name_search_string=doc_type_name_search_string,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    after_id: Union[Unset, None, str] = UNSET,
    before_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    doc_type_name_search_string: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedBOpsManagementDocTypeListDto]:
    """Get a list of all document types for use on the Butler Ops Management page

    Args:
        after_id (Union[Unset, None, str]):
        before_id (Union[Unset, None, str]):
        limit (Union[Unset, None, float]):
        doc_type_name_search_string (Union[Unset, None, str]):

    Returns:
        Response[PaginatedBOpsManagementDocTypeListDto]
    """

    kwargs = _get_kwargs(
        client=client,
        after_id=after_id,
        before_id=before_id,
        limit=limit,
        doc_type_name_search_string=doc_type_name_search_string,
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
    doc_type_name_search_string: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedBOpsManagementDocTypeListDto]:
    """Get a list of all document types for use on the Butler Ops Management page

    Args:
        after_id (Union[Unset, None, str]):
        before_id (Union[Unset, None, str]):
        limit (Union[Unset, None, float]):
        doc_type_name_search_string (Union[Unset, None, str]):

    Returns:
        Response[PaginatedBOpsManagementDocTypeListDto]
    """

    return (
        await asyncio_detailed(
            client=client,
            after_id=after_id,
            before_id=before_id,
            limit=limit,
            doc_type_name_search_string=doc_type_name_search_string,
        )
    ).parsed
