from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.billing_subscription_v2_dto import BillingSubscriptionV2Dto
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/internal/billing/subscription_v2".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[BillingSubscriptionV2Dto]:
    if response.status_code == 200:
        response_200 = BillingSubscriptionV2Dto.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[BillingSubscriptionV2Dto]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[BillingSubscriptionV2Dto]:
    """
    Returns:
        Response[BillingSubscriptionV2Dto]
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
) -> Optional[BillingSubscriptionV2Dto]:
    """
    Returns:
        Response[BillingSubscriptionV2Dto]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[BillingSubscriptionV2Dto]:
    """
    Returns:
        Response[BillingSubscriptionV2Dto]
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
) -> Optional[BillingSubscriptionV2Dto]:
    """
    Returns:
        Response[BillingSubscriptionV2Dto]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
