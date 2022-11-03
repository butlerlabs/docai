from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.ml_endpoint_metadata_dto import MlEndpointMetadataDto
from ...types import Response


def _get_kwargs(
    model_id: str,
    endpoint_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/internal/ml_models/{modelId}/endpoints/{endpointId}/metadata".format(
        client.base_url, modelId=model_id, endpointId=endpoint_id
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


def _parse_response(*, response: httpx.Response) -> Optional[MlEndpointMetadataDto]:
    if response.status_code == 200:
        response_200 = MlEndpointMetadataDto.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[MlEndpointMetadataDto]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    model_id: str,
    endpoint_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[MlEndpointMetadataDto]:
    """Get metadata of a ml endpoint

    Args:
        model_id (str):
        endpoint_id (str):

    Returns:
        Response[MlEndpointMetadataDto]
    """

    kwargs = _get_kwargs(
        model_id=model_id,
        endpoint_id=endpoint_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    model_id: str,
    endpoint_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[MlEndpointMetadataDto]:
    """Get metadata of a ml endpoint

    Args:
        model_id (str):
        endpoint_id (str):

    Returns:
        Response[MlEndpointMetadataDto]
    """

    return sync_detailed(
        model_id=model_id,
        endpoint_id=endpoint_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    model_id: str,
    endpoint_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[MlEndpointMetadataDto]:
    """Get metadata of a ml endpoint

    Args:
        model_id (str):
        endpoint_id (str):

    Returns:
        Response[MlEndpointMetadataDto]
    """

    kwargs = _get_kwargs(
        model_id=model_id,
        endpoint_id=endpoint_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    model_id: str,
    endpoint_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[MlEndpointMetadataDto]:
    """Get metadata of a ml endpoint

    Args:
        model_id (str):
        endpoint_id (str):

    Returns:
        Response[MlEndpointMetadataDto]
    """

    return (
        await asyncio_detailed(
            model_id=model_id,
            endpoint_id=endpoint_id,
            client=client,
        )
    ).parsed
