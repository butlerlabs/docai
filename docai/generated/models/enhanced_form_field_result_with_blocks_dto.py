from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.category_field_option_dto import CategoryFieldOptionDto
from ..models.entity_type import EntityType
from ..models.example_form_field_keys_and_values import ExampleFormFieldKeysAndValues
from ..models.extracted_field_results_dto import ExtractedFieldResultsDto
from ..types import UNSET, Unset

T = TypeVar("T", bound="EnhancedFormFieldResultWithBlocksDto")


@attr.s(auto_attribs=True)
class EnhancedFormFieldResultWithBlocksDto:
    """
    Attributes:
        id (str): Id of the form field
        form_field_name (str): Name of the form field
        form_field_type (EntityType):
        label_field (ExtractedFieldResultsDto):
        value_field (ExtractedFieldResultsDto):
        examples (ExampleFormFieldKeysAndValues):
        notes (str): Free text notes associated with this Form Field
        category_field_options (Union[Unset, List[CategoryFieldOptionDto]]): Field options if this is a category field
    """

    id: str
    form_field_name: str
    form_field_type: EntityType
    label_field: ExtractedFieldResultsDto
    value_field: ExtractedFieldResultsDto
    examples: ExampleFormFieldKeysAndValues
    notes: str
    category_field_options: Union[Unset, List[CategoryFieldOptionDto]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        form_field_name = self.form_field_name
        form_field_type = self.form_field_type.value

        label_field = self.label_field.to_dict()

        value_field = self.value_field.to_dict()

        examples = self.examples.to_dict()

        notes = self.notes
        category_field_options: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.category_field_options, Unset):
            category_field_options = []
            for category_field_options_item_data in self.category_field_options:
                category_field_options_item = category_field_options_item_data.to_dict()

                category_field_options.append(category_field_options_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "formFieldName": form_field_name,
                "formFieldType": form_field_type,
                "labelField": label_field,
                "valueField": value_field,
                "examples": examples,
                "notes": notes,
            }
        )
        if category_field_options is not UNSET:
            field_dict["categoryFieldOptions"] = category_field_options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        form_field_name = d.pop("formFieldName")

        form_field_type = EntityType(d.pop("formFieldType"))

        label_field = ExtractedFieldResultsDto.from_dict(d.pop("labelField"))

        value_field = ExtractedFieldResultsDto.from_dict(d.pop("valueField"))

        examples = ExampleFormFieldKeysAndValues.from_dict(d.pop("examples"))

        notes = d.pop("notes")

        category_field_options = []
        _category_field_options = d.pop("categoryFieldOptions", UNSET)
        for category_field_options_item_data in _category_field_options or []:
            category_field_options_item = CategoryFieldOptionDto.from_dict(category_field_options_item_data)

            category_field_options.append(category_field_options_item)

        enhanced_form_field_result_with_blocks_dto = cls(
            id=id,
            form_field_name=form_field_name,
            form_field_type=form_field_type,
            label_field=label_field,
            value_field=value_field,
            examples=examples,
            notes=notes,
            category_field_options=category_field_options,
        )

        enhanced_form_field_result_with_blocks_dto.additional_properties = d
        return enhanced_form_field_result_with_blocks_dto

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
