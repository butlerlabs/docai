from docai.generated.models import ColumnDto, FieldDto, ModelFieldDto, ModelTableDto, TableDto


def modelFieldToFieldDto(modelFieldDto: ModelFieldDto) -> FieldDto:
    return FieldDto(name=modelFieldDto.name, type=modelFieldDto.type)


def modelTableToTableDto(modelTableDto: ModelTableDto) -> TableDto:
    columns = [ColumnDto(name=c.name) for c in modelTableDto.columns]
    return TableDto(name=modelTableDto.name, columns=columns)
