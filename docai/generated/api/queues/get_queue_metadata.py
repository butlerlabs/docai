from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.queue_metadata_dto import QueueMetadataDto
from ...types import Response


def _get_kwargs(
    queue_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/internal/queues/{queueId}/metadata".format(client.base_url, queueId=queue_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[QueueMetadataDto]:
    if response.status_code == 200:
        response_200 = QueueMetadataDto.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[QueueMetadataDto]:
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
) -> Response[QueueMetadataDto]:
    """Get metadata about a queue.

    Args:
        queue_id (str):

    Returns:
        Response[QueueMetadataDto]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
        client=client,
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
) -> Optional[QueueMetadataDto]:
    """Get metadata about a queue.

    Args:
        queue_id (str):

    Returns:
        Response[QueueMetadataDto]
    """

    return sync_detailed(
        queue_id=queue_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    queue_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[QueueMetadataDto]:
    """Get metadata about a queue.

    Args:
        queue_id (str):

    Returns:
        Response[QueueMetadataDto]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    queue_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[QueueMetadataDto]:
    """Get metadata about a queue.

    Args:
        queue_id (str):

    Returns:
        Response[QueueMetadataDto]
    """

    return (
        await asyncio_detailed(
            queue_id=queue_id,
            client=client,
        )
    ).parsed
