from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.base_model_type import BaseModelType
from ..models.industry_tag import IndustryTag

T = TypeVar("T", bound="LibraryModelDetailDto")


@attr.s(auto_attribs=True)
class LibraryModelDetailDto:
    """
    Attributes:
        model_type (BaseModelType):
        name (str): Name of the model.
        description (str): Short description of the model.
        image_url (str): url where the model image is stored.
        industry (List[IndustryTag]): Array of Industry tags that the model belongs to
        model_documentation (str): Stringified markdown file containing detailed information about this model
    """

    model_type: BaseModelType
    name: str
    description: str
    image_url: str
    industry: List[IndustryTag]
    model_documentation: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        model_type = self.model_type.value

        name = self.name
        description = self.description
        image_url = self.image_url
        industry = []
        for industry_item_data in self.industry:
            industry_item = industry_item_data.value

            industry.append(industry_item)

        model_documentation = self.model_documentation

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "modelType": model_type,
                "name": name,
                "description": description,
                "imageUrl": image_url,
                "industry": industry,
                "modelDocumentation": model_documentation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        model_type = BaseModelType(d.pop("modelType"))

        name = d.pop("name")

        description = d.pop("description")

        image_url = d.pop("imageUrl")

        industry = []
        _industry = d.pop("industry")
        for industry_item_data in _industry:
            industry_item = IndustryTag(industry_item_data)

            industry.append(industry_item)

        model_documentation = d.pop("modelDocumentation")

        library_model_detail_dto = cls(
            model_type=model_type,
            name=name,
            description=description,
            image_url=image_url,
            industry=industry,
            model_documentation=model_documentation,
        )

        library_model_detail_dto.additional_properties = d
        return library_model_detail_dto

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
