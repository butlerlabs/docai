from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.incorrect_field_dto import IncorrectFieldDto
from ...models.incorrect_field_update_dto import IncorrectFieldUpdateDto
from ...types import Response


def _get_kwargs(
    doc_id: str,
    field_id: str,
    *,
    client: AuthenticatedClient,
    json_body: IncorrectFieldUpdateDto,
) -> Dict[str, Any]:
    url = "{}/api/internal/incorrect_documents/{docId}/fields/{fieldId}".format(
        client.base_url, docId=doc_id, fieldId=field_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[IncorrectFieldDto]:
    if response.status_code == 200:
        response_200 = IncorrectFieldDto.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[IncorrectFieldDto]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    doc_id: str,
    field_id: str,
    *,
    client: AuthenticatedClient,
    json_body: IncorrectFieldUpdateDto,
) -> Response[IncorrectFieldDto]:
    """
    Args:
        doc_id (str):
        field_id (str):
        json_body (IncorrectFieldUpdateDto):

    Returns:
        Response[IncorrectFieldDto]
    """

    kwargs = _get_kwargs(
        doc_id=doc_id,
        field_id=field_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    doc_id: str,
    field_id: str,
    *,
    client: AuthenticatedClient,
    json_body: IncorrectFieldUpdateDto,
) -> Optional[IncorrectFieldDto]:
    """
    Args:
        doc_id (str):
        field_id (str):
        json_body (IncorrectFieldUpdateDto):

    Returns:
        Response[IncorrectFieldDto]
    """

    return sync_detailed(
        doc_id=doc_id,
        field_id=field_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    doc_id: str,
    field_id: str,
    *,
    client: AuthenticatedClient,
    json_body: IncorrectFieldUpdateDto,
) -> Response[IncorrectFieldDto]:
    """
    Args:
        doc_id (str):
        field_id (str):
        json_body (IncorrectFieldUpdateDto):

    Returns:
        Response[IncorrectFieldDto]
    """

    kwargs = _get_kwargs(
        doc_id=doc_id,
        field_id=field_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    doc_id: str,
    field_id: str,
    *,
    client: AuthenticatedClient,
    json_body: IncorrectFieldUpdateDto,
) -> Optional[IncorrectFieldDto]:
    """
    Args:
        doc_id (str):
        field_id (str):
        json_body (IncorrectFieldUpdateDto):

    Returns:
        Response[IncorrectFieldDto]
    """

    return (
        await asyncio_detailed(
            doc_id=doc_id,
            field_id=field_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
