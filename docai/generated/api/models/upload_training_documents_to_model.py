from typing import Any, Dict

import httpx

from ...client import AuthenticatedClient
from ...models.upload_training_documents_to_model_multipart_data import UploadTrainingDocumentsToModelMultipartData
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: AuthenticatedClient,
    multipart_data: UploadTrainingDocumentsToModelMultipartData,
) -> Dict[str, Any]:
    url = "{}/api/internal/models/{id}/training_documents".format(client.base_url, id=id)

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


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    multipart_data: UploadTrainingDocumentsToModelMultipartData,
) -> Response[Any]:
    """Upload documents to the model for Training

    Args:
        id (str):
        multipart_data (UploadTrainingDocumentsToModelMultipartData):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        multipart_data=multipart_data,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    multipart_data: UploadTrainingDocumentsToModelMultipartData,
) -> Response[Any]:
    """Upload documents to the model for Training

    Args:
        id (str):
        multipart_data (UploadTrainingDocumentsToModelMultipartData):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        multipart_data=multipart_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
