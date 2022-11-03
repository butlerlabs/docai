from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.extraction_results_with_blocks_dto import ExtractionResultsWithBlocksDto
from ...types import Response


def _get_kwargs(
    doc_type_id: str,
    document_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/internal/document_types/{docTypeId}/test_documents/{documentId}/extraction_results".format(
        client.base_url, docTypeId=doc_type_id, documentId=document_id
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


def _parse_response(*, response: httpx.Response) -> Optional[ExtractionResultsWithBlocksDto]:
    if response.status_code == 200:
        response_200 = ExtractionResultsWithBlocksDto.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ExtractionResultsWithBlocksDto]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    doc_type_id: str,
    document_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ExtractionResultsWithBlocksDto]:
    """Get the extraction results for a Test Document

    Args:
        doc_type_id (str):
        document_id (str):

    Returns:
        Response[ExtractionResultsWithBlocksDto]
    """

    kwargs = _get_kwargs(
        doc_type_id=doc_type_id,
        document_id=document_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    doc_type_id: str,
    document_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[ExtractionResultsWithBlocksDto]:
    """Get the extraction results for a Test Document

    Args:
        doc_type_id (str):
        document_id (str):

    Returns:
        Response[ExtractionResultsWithBlocksDto]
    """

    return sync_detailed(
        doc_type_id=doc_type_id,
        document_id=document_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    doc_type_id: str,
    document_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ExtractionResultsWithBlocksDto]:
    """Get the extraction results for a Test Document

    Args:
        doc_type_id (str):
        document_id (str):

    Returns:
        Response[ExtractionResultsWithBlocksDto]
    """

    kwargs = _get_kwargs(
        doc_type_id=doc_type_id,
        document_id=document_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    doc_type_id: str,
    document_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[ExtractionResultsWithBlocksDto]:
    """Get the extraction results for a Test Document

    Args:
        doc_type_id (str):
        document_id (str):

    Returns:
        Response[ExtractionResultsWithBlocksDto]
    """

    return (
        await asyncio_detailed(
            doc_type_id=doc_type_id,
            document_id=document_id,
            client=client,
        )
    ).parsed
