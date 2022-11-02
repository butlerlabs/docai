from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.app_run_status_dto import AppRunStatusDto
from ...types import Response


def _get_kwargs(
    app_run_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/apps/app_runs/{appRunId}/status".format(client.base_url, appRunId=app_run_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[AppRunStatusDto]:
    if response.status_code == 200:
        response_200 = AppRunStatusDto.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[AppRunStatusDto]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    app_run_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[AppRunStatusDto]:
    """Get the status of an extraction job started by the upload_documents endpoint

    Args:
        app_run_id (str):

    Returns:
        Response[AppRunStatusDto]
    """

    kwargs = _get_kwargs(
        app_run_id=app_run_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    app_run_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[AppRunStatusDto]:
    """Get the status of an extraction job started by the upload_documents endpoint

    Args:
        app_run_id (str):

    Returns:
        Response[AppRunStatusDto]
    """

    return sync_detailed(
        app_run_id=app_run_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    app_run_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[AppRunStatusDto]:
    """Get the status of an extraction job started by the upload_documents endpoint

    Args:
        app_run_id (str):

    Returns:
        Response[AppRunStatusDto]
    """

    kwargs = _get_kwargs(
        app_run_id=app_run_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    app_run_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[AppRunStatusDto]:
    """Get the status of an extraction job started by the upload_documents endpoint

    Args:
        app_run_id (str):

    Returns:
        Response[AppRunStatusDto]
    """

    return (
        await asyncio_detailed(
            app_run_id=app_run_id,
            client=client,
        )
    ).parsed
