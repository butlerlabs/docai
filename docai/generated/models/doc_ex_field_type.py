from enum import Enum


class DocExFieldType(str, Enum):
    FORMFIELDLABEL = "FormFieldLabel"
    FORMFIELDVALUE = "FormFieldValue"
    TABLEFIELDCOLUMNLABEL = "TableFieldColumnLabel"
    TABLEFIELDCELLVALUE = "TableFieldCellValue"

    def __str__(self) -> str:
        return str(self.value)
