from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.classify_image_multipart_data import ClassifyImageMultipartData
from ...models.image_classification_result_dto import ImageClassificationResultDto
from ...models.single_file_url_upload_dto import SingleFileUrlUploadDto
from ...types import Response


def _get_kwargs(
    model_id: str,
    *,
    client: AuthenticatedClient,
    multipart_data: ClassifyImageMultipartData,
    json_body: SingleFileUrlUploadDto,
) -> Dict[str, Any]:
    url = "{}/api/image_classification/{modelId}/predict".format(client.base_url, modelId=model_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_body.to_dict()

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
    }


def _parse_response(*, response: httpx.Response) -> Optional[ImageClassificationResultDto]:
    if response.status_code == 200:
        response_200 = ImageClassificationResultDto.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ImageClassificationResultDto]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    model_id: str,
    *,
    client: AuthenticatedClient,
    multipart_data: ClassifyImageMultipartData,
    json_body: SingleFileUrlUploadDto,
) -> Response[ImageClassificationResultDto]:
    """Upload images and trigger image classification

    Args:
        model_id (str):
        multipart_data (ClassifyImageMultipartData):
        json_body (SingleFileUrlUploadDto):

    Returns:
        Response[ImageClassificationResultDto]
    """

    kwargs = _get_kwargs(
        model_id=model_id,
        client=client,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    model_id: str,
    *,
    client: AuthenticatedClient,
    multipart_data: ClassifyImageMultipartData,
    json_body: SingleFileUrlUploadDto,
) -> Optional[ImageClassificationResultDto]:
    """Upload images and trigger image classification

    Args:
        model_id (str):
        multipart_data (ClassifyImageMultipartData):
        json_body (SingleFileUrlUploadDto):

    Returns:
        Response[ImageClassificationResultDto]
    """

    return sync_detailed(
        model_id=model_id,
        client=client,
        multipart_data=multipart_data,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    model_id: str,
    *,
    client: AuthenticatedClient,
    multipart_data: ClassifyImageMultipartData,
    json_body: SingleFileUrlUploadDto,
) -> Response[ImageClassificationResultDto]:
    """Upload images and trigger image classification

    Args:
        model_id (str):
        multipart_data (ClassifyImageMultipartData):
        json_body (SingleFileUrlUploadDto):

    Returns:
        Response[ImageClassificationResultDto]
    """

    kwargs = _get_kwargs(
        model_id=model_id,
        client=client,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    model_id: str,
    *,
    client: AuthenticatedClient,
    multipart_data: ClassifyImageMultipartData,
    json_body: SingleFileUrlUploadDto,
) -> Optional[ImageClassificationResultDto]:
    """Upload images and trigger image classification

    Args:
        model_id (str):
        multipart_data (ClassifyImageMultipartData):
        json_body (SingleFileUrlUploadDto):

    Returns:
        Response[ImageClassificationResultDto]
    """

    return (
        await asyncio_detailed(
            model_id=model_id,
            client=client,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed
