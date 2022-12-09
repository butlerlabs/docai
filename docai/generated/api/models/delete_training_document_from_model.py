from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.model_and_document_id_param_dto import ModelAndDocumentIdParamDto
from ...types import Response


def _get_kwargs(
    id: str,
    document_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/internal/models/{id}/training_documents/{documentId}".format(
        client.base_url, id=id, documentId=document_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[ModelAndDocumentIdParamDto]:
    if response.status_code == 200:
        response_200 = ModelAndDocumentIdParamDto.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ModelAndDocumentIdParamDto]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    document_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ModelAndDocumentIdParamDto]:
    """Deletes a training document, by ID from a model.

    Args:
        id (str):
        document_id (str):

    Returns:
        Response[ModelAndDocumentIdParamDto]
    """

    kwargs = _get_kwargs(
        id=id,
        document_id=document_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    document_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[ModelAndDocumentIdParamDto]:
    """Deletes a training document, by ID from a model.

    Args:
        id (str):
        document_id (str):

    Returns:
        Response[ModelAndDocumentIdParamDto]
    """

    return sync_detailed(
        id=id,
        document_id=document_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    document_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ModelAndDocumentIdParamDto]:
    """Deletes a training document, by ID from a model.

    Args:
        id (str):
        document_id (str):

    Returns:
        Response[ModelAndDocumentIdParamDto]
    """

    kwargs = _get_kwargs(
        id=id,
        document_id=document_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    document_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[ModelAndDocumentIdParamDto]:
    """Deletes a training document, by ID from a model.

    Args:
        id (str):
        document_id (str):

    Returns:
        Response[ModelAndDocumentIdParamDto]
    """

    return (
        await asyncio_detailed(
            id=id,
            document_id=document_id,
            client=client,
        )
    ).parsed
