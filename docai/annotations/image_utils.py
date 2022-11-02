import mimetypes
from io import BytesIO
from typing import List, Optional

import httpx
from pdf2image import convert_from_bytes
from PIL import Image
from PIL.Image import Image as ImageType

SUPPORTED_IMG_MIME_TYPES = ["image/jpeg", "image/png"]


def get_mime_type_from_extension(extension: str) -> str:
    """
    Returns the mime type for a given file extension
    """
    return mimetypes.types_map[extension]


def load_file_as_img(file_url: str, mime_type: Optional[str] = None) -> List[ImageType]:
    """
    Loads a file from a URL and returns it as a PIL image

    Limitations & Notes:
    - Only supports JPG, PNG, and PDF files
    - If a multi-page PDF is passed, will return an array of images, one for each page
    """
    response = httpx.get(file_url)

    if mime_type is None:
        mime_type = get_mime_type_from_extension(
            mimetypes.guess_extension(response.headers.get("content-type", "").split(";")[0])
        )

    if mime_type in SUPPORTED_IMG_MIME_TYPES:
        return [Image.open(BytesIO(response.content))]
    elif mime_type == "application/pdf":
        return convert_from_bytes(response.content)
    else:
        raise ValueError(f"Unsupported mime type: {mime_type}")
