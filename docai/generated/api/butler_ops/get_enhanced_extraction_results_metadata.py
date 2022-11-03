from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.enhanced_extraction_results_metadata_dto import EnhancedExtractionResultsMetadataDto
from ...types import Response


def _get_kwargs(
    document_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/internal/butler_ops/labeling/{documentId}/enhanced_extraction_results/metadata".format(
        client.base_url, documentId=document_id
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


def _parse_response(*, response: httpx.Response) -> Optional[EnhancedExtractionResultsMetadataDto]:
    if response.status_code == 200:
        response_200 = EnhancedExtractionResultsMetadataDto.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[EnhancedExtractionResultsMetadataDto]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    document_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[EnhancedExtractionResultsMetadataDto]:
    """Retrieve the metadata related to the enhanced extraction results for the specified documentId

    Args:
        document_id (str):

    Returns:
        Response[EnhancedExtractionResultsMetadataDto]
    """

    kwargs = _get_kwargs(
        document_id=document_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    document_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[EnhancedExtractionResultsMetadataDto]:
    """Retrieve the metadata related to the enhanced extraction results for the specified documentId

    Args:
        document_id (str):

    Returns:
        Response[EnhancedExtractionResultsMetadataDto]
    """

    return sync_detailed(
        document_id=document_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    document_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[EnhancedExtractionResultsMetadataDto]:
    """Retrieve the metadata related to the enhanced extraction results for the specified documentId

    Args:
        document_id (str):

    Returns:
        Response[EnhancedExtractionResultsMetadataDto]
    """

    kwargs = _get_kwargs(
        document_id=document_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    document_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[EnhancedExtractionResultsMetadataDto]:
    """Retrieve the metadata related to the enhanced extraction results for the specified documentId

    Args:
        document_id (str):

    Returns:
        Response[EnhancedExtractionResultsMetadataDto]
    """

    return (
        await asyncio_detailed(
            document_id=document_id,
            client=client,
        )
    ).parsed
