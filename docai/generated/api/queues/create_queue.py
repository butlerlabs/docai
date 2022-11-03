from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.create_queue_response_dto import CreateQueueResponseDto
from ...models.queue_body_dto import QueueBodyDto
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: QueueBodyDto,
) -> Dict[str, Any]:
    url = "{}/api/internal/queues".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[CreateQueueResponseDto]:
    if response.status_code == 201:
        response_201 = CreateQueueResponseDto.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[CreateQueueResponseDto]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: QueueBodyDto,
) -> Response[CreateQueueResponseDto]:
    """Create a new queue. Takes in the document type id that the queue is used to process, the settings
    for the queue, and the name for the new queue. Returns the newly generated queue id.

    Args:
        json_body (QueueBodyDto):

    Returns:
        Response[CreateQueueResponseDto]
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
    json_body: QueueBodyDto,
) -> Optional[CreateQueueResponseDto]:
    """Create a new queue. Takes in the document type id that the queue is used to process, the settings
    for the queue, and the name for the new queue. Returns the newly generated queue id.

    Args:
        json_body (QueueBodyDto):

    Returns:
        Response[CreateQueueResponseDto]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: QueueBodyDto,
) -> Response[CreateQueueResponseDto]:
    """Create a new queue. Takes in the document type id that the queue is used to process, the settings
    for the queue, and the name for the new queue. Returns the newly generated queue id.

    Args:
        json_body (QueueBodyDto):

    Returns:
        Response[CreateQueueResponseDto]
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
    json_body: QueueBodyDto,
) -> Optional[CreateQueueResponseDto]:
    """Create a new queue. Takes in the document type id that the queue is used to process, the settings
    for the queue, and the name for the new queue. Returns the newly generated queue id.

    Args:
        json_body (QueueBodyDto):

    Returns:
        Response[CreateQueueResponseDto]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
