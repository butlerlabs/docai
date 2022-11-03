from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.extraction_result_status_dto import ExtractionResultStatusDto
from ...models.labeling_results_with_blocks_dto import LabelingResultsWithBlocksDto
from ...types import Response


def _get_kwargs(
    doc_type_id: str,
    document_id: str,
    *,
    client: AuthenticatedClient,
    json_body: LabelingResultsWithBlocksDto,
) -> Dict[str, Any]:
    url = "{}/api/internal/document_types/{docTypeId}/documents/{documentId}/labeling_result".format(
        client.base_url, docTypeId=doc_type_id, documentId=document_id
    )

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


def _parse_response(*, response: httpx.Response) -> Optional[ExtractionResultStatusDto]:
    if response.status_code == 201:
        response_201 = ExtractionResultStatusDto.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[ExtractionResultStatusDto]:
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
    json_body: LabelingResultsWithBlocksDto,
) -> Response[ExtractionResultStatusDto]:
    """Add or update the labels of a Training Document.

    Args:
        doc_type_id (str):
        document_id (str):
        json_body (LabelingResultsWithBlocksDto):

    Returns:
        Response[ExtractionResultStatusDto]
    """

    kwargs = _get_kwargs(
        doc_type_id=doc_type_id,
        document_id=document_id,
        client=client,
        json_body=json_body,
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
    json_body: LabelingResultsWithBlocksDto,
) -> Optional[ExtractionResultStatusDto]:
    """Add or update the labels of a Training Document.

    Args:
        doc_type_id (str):
        document_id (str):
        json_body (LabelingResultsWithBlocksDto):

    Returns:
        Response[ExtractionResultStatusDto]
    """

    return sync_detailed(
        doc_type_id=doc_type_id,
        document_id=document_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    doc_type_id: str,
    document_id: str,
    *,
    client: AuthenticatedClient,
    json_body: LabelingResultsWithBlocksDto,
) -> Response[ExtractionResultStatusDto]:
    """Add or update the labels of a Training Document.

    Args:
        doc_type_id (str):
        document_id (str):
        json_body (LabelingResultsWithBlocksDto):

    Returns:
        Response[ExtractionResultStatusDto]
    """

    kwargs = _get_kwargs(
        doc_type_id=doc_type_id,
        document_id=document_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    doc_type_id: str,
    document_id: str,
    *,
    client: AuthenticatedClient,
    json_body: LabelingResultsWithBlocksDto,
) -> Optional[ExtractionResultStatusDto]:
    """Add or update the labels of a Training Document.

    Args:
        doc_type_id (str):
        document_id (str):
        json_body (LabelingResultsWithBlocksDto):

    Returns:
        Response[ExtractionResultStatusDto]
    """

    return (
        await asyncio_detailed(
            doc_type_id=doc_type_id,
            document_id=document_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
