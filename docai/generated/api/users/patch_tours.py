from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.user_tour_dto import UserTourDto
from ...models.user_tour_patch_dto import UserTourPatchDto
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: UserTourPatchDto,
) -> Dict[str, Any]:
    url = "{}/api/internal/users/me/tours".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[UserTourDto]:
    if response.status_code == 200:
        response_200 = UserTourDto.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[UserTourDto]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: UserTourPatchDto,
) -> Response[UserTourDto]:
    """Update the active step for each tour.

    Args:
        json_body (UserTourPatchDto):

    Returns:
        Response[UserTourDto]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: UserTourPatchDto,
) -> Optional[UserTourDto]:
    """Update the active step for each tour.

    Args:
        json_body (UserTourPatchDto):

    Returns:
        Response[UserTourDto]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: UserTourPatchDto,
) -> Response[UserTourDto]:
    """Update the active step for each tour.

    Args:
        json_body (UserTourPatchDto):

    Returns:
        Response[UserTourDto]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: UserTourPatchDto,
) -> Optional[UserTourDto]:
    """Update the active step for each tour.

    Args:
        json_body (UserTourPatchDto):

    Returns:
        Response[UserTourDto]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
