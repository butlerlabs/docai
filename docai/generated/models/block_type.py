from enum import Enum


class BlockType(str, Enum):
    WORD = "Word"
    CHECKBOX = "Checkbox"

    def __str__(self) -> str:
        return str(self.value)
