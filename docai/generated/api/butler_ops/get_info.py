from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.b_ops_doc_type_management_info_dto import BOpsDocTypeManagementInfoDto
from ...types import Response


def _get_kwargs(
    document_type_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/internal/butler_ops/management/{documentTypeId}/info".format(
        client.base_url, documentTypeId=document_type_id
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


def _parse_response(*, response: httpx.Response) -> Optional[BOpsDocTypeManagementInfoDto]:
    if response.status_code == 200:
        response_200 = BOpsDocTypeManagementInfoDto.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[BOpsDocTypeManagementInfoDto]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    document_type_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[BOpsDocTypeManagementInfoDto]:
    """Retrieves the management info for a specific document type

    Args:
        document_type_id (str):

    Returns:
        Response[BOpsDocTypeManagementInfoDto]
    """

    kwargs = _get_kwargs(
        document_type_id=document_type_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    document_type_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[BOpsDocTypeManagementInfoDto]:
    """Retrieves the management info for a specific document type

    Args:
        document_type_id (str):

    Returns:
        Response[BOpsDocTypeManagementInfoDto]
    """

    return sync_detailed(
        document_type_id=document_type_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    document_type_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[BOpsDocTypeManagementInfoDto]:
    """Retrieves the management info for a specific document type

    Args:
        document_type_id (str):

    Returns:
        Response[BOpsDocTypeManagementInfoDto]
    """

    kwargs = _get_kwargs(
        document_type_id=document_type_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    document_type_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[BOpsDocTypeManagementInfoDto]:
    """Retrieves the management info for a specific document type

    Args:
        document_type_id (str):

    Returns:
        Response[BOpsDocTypeManagementInfoDto]
    """

    return (
        await asyncio_detailed(
            document_type_id=document_type_id,
            client=client,
        )
    ).parsed
