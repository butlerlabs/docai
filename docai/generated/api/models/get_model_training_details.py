from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.model_training_details_dto import ModelTrainingDetailsDto
from ...models.sort_order import SortOrder
from ...models.training_details_sort_by import TrainingDetailsSortBy
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: AuthenticatedClient,
    after_id: Union[Unset, None, str] = UNSET,
    before_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    sort_order: Union[Unset, None, SortOrder] = UNSET,
    sort_by: Union[Unset, None, TrainingDetailsSortBy] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/internal/models/{id}/training_details".format(client.base_url, id=id)

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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[ModelTrainingDetailsDto]:
    if response.status_code == 200:
        response_200 = ModelTrainingDetailsDto.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ModelTrainingDetailsDto]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    after_id: Union[Unset, None, str] = UNSET,
    before_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    sort_order: Union[Unset, None, SortOrder] = UNSET,
    sort_by: Union[Unset, None, TrainingDetailsSortBy] = UNSET,
) -> Response[ModelTrainingDetailsDto]:
    """Get training details of a model

    Args:
        id (str):
        after_id (Union[Unset, None, str]):
        before_id (Union[Unset, None, str]):
        limit (Union[Unset, None, float]):
        sort_order (Union[Unset, None, SortOrder]):
        sort_by (Union[Unset, None, TrainingDetailsSortBy]):

    Returns:
        Response[ModelTrainingDetailsDto]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        after_id=after_id,
        before_id=before_id,
        limit=limit,
        sort_order=sort_order,
        sort_by=sort_by,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    after_id: Union[Unset, None, str] = UNSET,
    before_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    sort_order: Union[Unset, None, SortOrder] = UNSET,
    sort_by: Union[Unset, None, TrainingDetailsSortBy] = UNSET,
) -> Optional[ModelTrainingDetailsDto]:
    """Get training details of a model

    Args:
        id (str):
        after_id (Union[Unset, None, str]):
        before_id (Union[Unset, None, str]):
        limit (Union[Unset, None, float]):
        sort_order (Union[Unset, None, SortOrder]):
        sort_by (Union[Unset, None, TrainingDetailsSortBy]):

    Returns:
        Response[ModelTrainingDetailsDto]
    """

    return sync_detailed(
        id=id,
        client=client,
        after_id=after_id,
        before_id=before_id,
        limit=limit,
        sort_order=sort_order,
        sort_by=sort_by,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    after_id: Union[Unset, None, str] = UNSET,
    before_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    sort_order: Union[Unset, None, SortOrder] = UNSET,
    sort_by: Union[Unset, None, TrainingDetailsSortBy] = UNSET,
) -> Response[ModelTrainingDetailsDto]:
    """Get training details of a model

    Args:
        id (str):
        after_id (Union[Unset, None, str]):
        before_id (Union[Unset, None, str]):
        limit (Union[Unset, None, float]):
        sort_order (Union[Unset, None, SortOrder]):
        sort_by (Union[Unset, None, TrainingDetailsSortBy]):

    Returns:
        Response[ModelTrainingDetailsDto]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        after_id=after_id,
        before_id=before_id,
        limit=limit,
        sort_order=sort_order,
        sort_by=sort_by,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    after_id: Union[Unset, None, str] = UNSET,
    before_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, float] = UNSET,
    sort_order: Union[Unset, None, SortOrder] = UNSET,
    sort_by: Union[Unset, None, TrainingDetailsSortBy] = UNSET,
) -> Optional[ModelTrainingDetailsDto]:
    """Get training details of a model

    Args:
        id (str):
        after_id (Union[Unset, None, str]):
        before_id (Union[Unset, None, str]):
        limit (Union[Unset, None, float]):
        sort_order (Union[Unset, None, SortOrder]):
        sort_by (Union[Unset, None, TrainingDetailsSortBy]):

    Returns:
        Response[ModelTrainingDetailsDto]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            after_id=after_id,
            before_id=before_id,
            limit=limit,
            sort_order=sort_order,
            sort_by=sort_by,
        )
    ).parsed
