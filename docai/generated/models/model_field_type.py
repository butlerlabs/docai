from enum import Enum


class ModelFieldType(str, Enum):
    TEXT = "Text"
    CHECKBOX = "Checkbox"
    SIGNATURE = "Signature"
    TABLE = "Table"

    def __str__(self) -> str:
        return str(self.value)
