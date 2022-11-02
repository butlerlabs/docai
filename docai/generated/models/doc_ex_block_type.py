from enum import Enum


class DocExBlockType(str, Enum):
    FORMLABEL = "FormLabel"
    FORMVALUE = "FormValue"
    TABLECELL = "TableCell"
    TABLEHEADER = "TableHeader"
    WORD = "Word"
    LINE = "Line"
    CHECKBOX = "Checkbox"

    def __str__(self) -> str:
        return str(self.value)
