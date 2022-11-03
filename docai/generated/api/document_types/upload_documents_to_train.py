from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.document_id_list_dto import DocumentIdListDto
from ...models.upload_documents_to_train_multipart_data import UploadDocumentsToTrainMultipartData
from ...types import Response


def _get_kwargs(
    doc_type_id: str,
    *,
    client: AuthenticatedClient,
    multipart_data: UploadDocumentsToTrainMultipartData,
) -> Dict[str, Any]:
    url = "{}/api/internal/document_types/{docTypeId}/upload".format(client.base_url, docTypeId=doc_type_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
    }


def _parse_response(*, response: httpx.Response) -> Optional[DocumentIdListDto]:
    if response.status_code == 200:
        response_200 = DocumentIdListDto.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[DocumentIdListDto]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    doc_type_id: str,
    *,
    client: AuthenticatedClient,
    multipart_data: UploadDocumentsToTrainMultipartData,
) -> Response[DocumentIdListDto]:
    """Upload documents to the document type for Training

    Args:
        doc_type_id (str):
        multipart_data (UploadDocumentsToTrainMultipartData):

    Returns:
        Response[DocumentIdListDto]
    """

    kwargs = _get_kwargs(
        doc_type_id=doc_type_id,
        client=client,
        multipart_data=multipart_data,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    doc_type_id: str,
    *,
    client: AuthenticatedClient,
    multipart_data: UploadDocumentsToTrainMultipartData,
) -> Optional[DocumentIdListDto]:
    """Upload documents to the document type for Training

    Args:
        doc_type_id (str):
        multipart_data (UploadDocumentsToTrainMultipartData):

    Returns:
        Response[DocumentIdListDto]
    """

    return sync_detailed(
        doc_type_id=doc_type_id,
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    doc_type_id: str,
    *,
    client: AuthenticatedClient,
    multipart_data: UploadDocumentsToTrainMultipartData,
) -> Response[DocumentIdListDto]:
    """Upload documents to the document type for Training

    Args:
        doc_type_id (str):
        multipart_data (UploadDocumentsToTrainMultipartData):

    Returns:
        Response[DocumentIdListDto]
    """

    kwargs = _get_kwargs(
        doc_type_id=doc_type_id,
        client=client,
        multipart_data=multipart_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    doc_type_id: str,
    *,
    client: AuthenticatedClient,
    multipart_data: UploadDocumentsToTrainMultipartData,
) -> Optional[DocumentIdListDto]:
    """Upload documents to the document type for Training

    Args:
        doc_type_id (str):
        multipart_data (UploadDocumentsToTrainMultipartData):

    Returns:
        Response[DocumentIdListDto]
    """

    return (
        await asyncio_detailed(
            doc_type_id=doc_type_id,
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
