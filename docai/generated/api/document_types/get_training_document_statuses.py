from typing import Any, Dict, List, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.training_document_status_list_dto import TrainingDocumentStatusListDto
from ...types import UNSET, Response


def _get_kwargs(
    doc_type_id: str,
    *,
    client: AuthenticatedClient,
    document_ids: List[str],
) -> Dict[str, Any]:
    url = "{}/api/internal/document_types/{docTypeId}/status".format(client.base_url, docTypeId=doc_type_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_document_ids = document_ids

    params["documentIds"] = json_document_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[TrainingDocumentStatusListDto]:
    if response.status_code == 200:
        response_200 = TrainingDocumentStatusListDto.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[TrainingDocumentStatusListDto]:
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
    document_ids: List[str],
) -> Response[TrainingDocumentStatusListDto]:
    """Get a list of Training Document Statuses, queried by Id

    Args:
        doc_type_id (str):
        document_ids (List[str]):

    Returns:
        Response[TrainingDocumentStatusListDto]
    """

    kwargs = _get_kwargs(
        doc_type_id=doc_type_id,
        client=client,
        document_ids=document_ids,
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
    document_ids: List[str],
) -> Optional[TrainingDocumentStatusListDto]:
    """Get a list of Training Document Statuses, queried by Id

    Args:
        doc_type_id (str):
        document_ids (List[str]):

    Returns:
        Response[TrainingDocumentStatusListDto]
    """

    return sync_detailed(
        doc_type_id=doc_type_id,
        client=client,
        document_ids=document_ids,
    ).parsed


async def asyncio_detailed(
    doc_type_id: str,
    *,
    client: AuthenticatedClient,
    document_ids: List[str],
) -> Response[TrainingDocumentStatusListDto]:
    """Get a list of Training Document Statuses, queried by Id

    Args:
        doc_type_id (str):
        document_ids (List[str]):

    Returns:
        Response[TrainingDocumentStatusListDto]
    """

    kwargs = _get_kwargs(
        doc_type_id=doc_type_id,
        client=client,
        document_ids=document_ids,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    doc_type_id: str,
    *,
    client: AuthenticatedClient,
    document_ids: List[str],
) -> Optional[TrainingDocumentStatusListDto]:
    """Get a list of Training Document Statuses, queried by Id

    Args:
        doc_type_id (str):
        document_ids (List[str]):

    Returns:
        Response[TrainingDocumentStatusListDto]
    """

    return (
        await asyncio_detailed(
            doc_type_id=doc_type_id,
            client=client,
            document_ids=document_ids,
        )
    ).parsed
