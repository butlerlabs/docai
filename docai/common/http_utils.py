import json
from typing import TypeVar

from docai.generated.types import Response


# Basic error handling for HTTP failure statuses
class HttpException(Exception):
    def __init__(self, status_code: int, message: str):
        super().__init__(f"status code {status_code}, {message}")


T = TypeVar("T")


def verify_response_or_raise(response: Response[T]) -> T:
    if response.status_code >= 200 and response.status_code < 400:
        return response.parsed
    else:
        message = None
        try:
            e = json.loads(response.content)
            message = e.get("message") if isinstance(e, dict) else None
        finally:
            raise HttpException(response.status_code, message or "unknown error")
