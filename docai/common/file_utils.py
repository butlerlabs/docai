import mimetypes
import os
from io import FileIO


# Utils for inferring file name and mime type for a local file
def infer_file_name(f: FileIO) -> str:
    return os.path.basename(f.name)


def infer_mime_type(file_name: str) -> str:
    mime_type = mimetypes.guess_type(file_name)[0]
    if mime_type is None:
        raise RuntimeError(f"could not infer mime type for file {file_name}, please specify mime type manually")
    return mime_type
