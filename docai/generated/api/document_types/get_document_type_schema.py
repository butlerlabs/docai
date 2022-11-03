from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.document_type_schema_dto import DocumentTypeSchemaDto
from ...types import Response


def _get_kwargs(
    doc_type_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/internal/document_types/{docTypeId}/schema".format(client.base_url, docTypeId=doc_type_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, DocumentTypeSchemaDto]]:
    if response.status_code == 200:
        response_200 = DocumentTypeSchemaDto.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, DocumentTypeSchemaDto]]:
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
) -> Response[Union[Any, DocumentTypeSchemaDto]]:
    """Get a document type schema by ID

    Args:
        doc_type_id (str):

    Returns:
        Response[Union[Any, DocumentTypeSchemaDto]]
    """

    kwargs = _get_kwargs(
        doc_type_id=doc_type_id,
        client=client,
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
) -> Optional[Union[Any, DocumentTypeSchemaDto]]:
    """Get a document type schema by ID

    Args:
        doc_type_id (str):

    Returns:
        Response[Union[Any, DocumentTypeSchemaDto]]
    """

    return sync_detailed(
        doc_type_id=doc_type_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    doc_type_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, DocumentTypeSchemaDto]]:
    """Get a document type schema by ID

    Args:
        doc_type_id (str):

    Returns:
        Response[Union[Any, DocumentTypeSchemaDto]]
    """

    kwargs = _get_kwargs(
        doc_type_id=doc_type_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    doc_type_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, DocumentTypeSchemaDto]]:
    """Get a document type schema by ID

    Args:
        doc_type_id (str):

    Returns:
        Response[Union[Any, DocumentTypeSchemaDto]]
    """

    return (
        await asyncio_detailed(
            doc_type_id=doc_type_id,
            client=client,
        )
    ).parsed
