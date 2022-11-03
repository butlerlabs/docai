from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.enhanced_extraction_results_dto import EnhancedExtractionResultsDto
from ...models.enhanced_extraction_results_field_status import EnhancedExtractionResultsFieldStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    document_id: str,
    *,
    client: AuthenticatedClient,
    status: Union[Unset, None, EnhancedExtractionResultsFieldStatus] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/internal/butler_ops/labeling/{documentId}/enhanced_extraction_results".format(
        client.base_url, documentId=document_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_status: Union[Unset, None, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value if status else None

    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[EnhancedExtractionResultsDto]:
    if response.status_code == 200:
        response_200 = EnhancedExtractionResultsDto.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[EnhancedExtractionResultsDto]:
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
    status: Union[Unset, None, EnhancedExtractionResultsFieldStatus] = UNSET,
) -> Response[EnhancedExtractionResultsDto]:
    """Retrieve enhanced extraction results for the specified documentId

    Args:
        document_id (str):
        status (Union[Unset, None, EnhancedExtractionResultsFieldStatus]):

    Returns:
        Response[EnhancedExtractionResultsDto]
    """

    kwargs = _get_kwargs(
        document_id=document_id,
        client=client,
        status=status,
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
    status: Union[Unset, None, EnhancedExtractionResultsFieldStatus] = UNSET,
) -> Optional[EnhancedExtractionResultsDto]:
    """Retrieve enhanced extraction results for the specified documentId

    Args:
        document_id (str):
        status (Union[Unset, None, EnhancedExtractionResultsFieldStatus]):

    Returns:
        Response[EnhancedExtractionResultsDto]
    """

    return sync_detailed(
        document_id=document_id,
        client=client,
        status=status,
    ).parsed


async def asyncio_detailed(
    document_id: str,
    *,
    client: AuthenticatedClient,
    status: Union[Unset, None, EnhancedExtractionResultsFieldStatus] = UNSET,
) -> Response[EnhancedExtractionResultsDto]:
    """Retrieve enhanced extraction results for the specified documentId

    Args:
        document_id (str):
        status (Union[Unset, None, EnhancedExtractionResultsFieldStatus]):

    Returns:
        Response[EnhancedExtractionResultsDto]
    """

    kwargs = _get_kwargs(
        document_id=document_id,
        client=client,
        status=status,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    document_id: str,
    *,
    client: AuthenticatedClient,
    status: Union[Unset, None, EnhancedExtractionResultsFieldStatus] = UNSET,
) -> Optional[EnhancedExtractionResultsDto]:
    """Retrieve enhanced extraction results for the specified documentId

    Args:
        document_id (str):
        status (Union[Unset, None, EnhancedExtractionResultsFieldStatus]):

    Returns:
        Response[EnhancedExtractionResultsDto]
    """

    return (
        await asyncio_detailed(
            document_id=document_id,
            client=client,
            status=status,
        )
    ).parsed
