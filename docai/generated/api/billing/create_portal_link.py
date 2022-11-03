from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.chargebee_portal_session_dto import ChargebeePortalSessionDto
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/internal/billing/hosted_page/portal_link".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[ChargebeePortalSessionDto]:
    if response.status_code == 201:
        response_201 = ChargebeePortalSessionDto.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[ChargebeePortalSessionDto]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ChargebeePortalSessionDto]:
    """
    Returns:
        Response[ChargebeePortalSessionDto]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[ChargebeePortalSessionDto]:
    """
    Returns:
        Response[ChargebeePortalSessionDto]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ChargebeePortalSessionDto]:
    """
    Returns:
        Response[ChargebeePortalSessionDto]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[ChargebeePortalSessionDto]:
    """
    Returns:
        Response[ChargebeePortalSessionDto]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
