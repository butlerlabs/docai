from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.queue_settings_dto import QueueSettingsDto
from ...models.queue_settings_update_dto import QueueSettingsUpdateDto
from ...types import Response


def _get_kwargs(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    json_body: QueueSettingsUpdateDto,
) -> Dict[str, Any]:
    url = "{}/api/internal/queues/{queueId}/settings".format(client.base_url, queueId=queue_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[QueueSettingsDto]:
    if response.status_code == 200:
        response_200 = QueueSettingsDto.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[QueueSettingsDto]:
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
    json_body: QueueSettingsUpdateDto,
) -> Response[QueueSettingsDto]:
    """
    Args:
        queue_id (str):
        json_body (QueueSettingsUpdateDto):

    Returns:
        Response[QueueSettingsDto]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
        client=client,
        json_body=json_body,
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
    json_body: QueueSettingsUpdateDto,
) -> Optional[QueueSettingsDto]:
    """
    Args:
        queue_id (str):
        json_body (QueueSettingsUpdateDto):

    Returns:
        Response[QueueSettingsDto]
    """

    return sync_detailed(
        queue_id=queue_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    json_body: QueueSettingsUpdateDto,
) -> Response[QueueSettingsDto]:
    """
    Args:
        queue_id (str):
        json_body (QueueSettingsUpdateDto):

    Returns:
        Response[QueueSettingsDto]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    json_body: QueueSettingsUpdateDto,
) -> Optional[QueueSettingsDto]:
    """
    Args:
        queue_id (str):
        json_body (QueueSettingsUpdateDto):

    Returns:
        Response[QueueSettingsDto]
    """

    return (
        await asyncio_detailed(
            queue_id=queue_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
