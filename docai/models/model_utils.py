from docai.generated.models.column_dto import ColumnDto
from docai.generated.models.document_type_field_dto import DocumentTypeFieldDto
from docai.generated.models.document_type_table_dto import DocumentTypeTableDto
from docai.generated.models.field_dto import FieldDto
from docai.generated.models.model_field_type import ModelFieldType
from docai.generated.models.table_dto import TableDto


def modelFieldToFieldDto(modelFieldDto: DocumentTypeFieldDto) -> FieldDto:
    # DocumentTypeFieldDto doesn't support field types, assume everything is a text for now
    return FieldDto(name=modelFieldDto.name, type=ModelFieldType.TEXT)


def modelTableToTableDto(modelTableDto: DocumentTypeTableDto) -> TableDto:
    columns = [ColumnDto(name=c.name) for c in modelTableDto.columns]
    return TableDto(name=modelTableDto.name, columns=columns)
