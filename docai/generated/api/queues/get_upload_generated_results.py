from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.upload_generated_results_dto import UploadGeneratedResultsDto
from ...types import Response


def _get_kwargs(
    queue_id: str,
    upload_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/internal/queues/{queueId}/uploads/{uploadId}/generated_results".format(
        client.base_url, queueId=queue_id, uploadId=upload_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[UploadGeneratedResultsDto]:
    if response.status_code == 200:
        response_200 = UploadGeneratedResultsDto.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[UploadGeneratedResultsDto]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    queue_id: str,
    upload_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[UploadGeneratedResultsDto]:
    """Get signed s3 urls for the various result formats we support.

    Args:
        queue_id (str):
        upload_id (str):

    Returns:
        Response[UploadGeneratedResultsDto]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
        upload_id=upload_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    queue_id: str,
    upload_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[UploadGeneratedResultsDto]:
    """Get signed s3 urls for the various result formats we support.

    Args:
        queue_id (str):
        upload_id (str):

    Returns:
        Response[UploadGeneratedResultsDto]
    """

    return sync_detailed(
        queue_id=queue_id,
        upload_id=upload_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    queue_id: str,
    upload_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[UploadGeneratedResultsDto]:
    """Get signed s3 urls for the various result formats we support.

    Args:
        queue_id (str):
        upload_id (str):

    Returns:
        Response[UploadGeneratedResultsDto]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
        upload_id=upload_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    queue_id: str,
    upload_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[UploadGeneratedResultsDto]:
    """Get signed s3 urls for the various result formats we support.

    Args:
        queue_id (str):
        upload_id (str):

    Returns:
        Response[UploadGeneratedResultsDto]
    """

    return (
        await asyncio_detailed(
            queue_id=queue_id,
            upload_id=upload_id,
            client=client,
        )
    ).parsed
