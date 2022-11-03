from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.chargebee_linked_customer_dto import ChargebeeLinkedCustomerDto
from ..types import UNSET, Unset

T = TypeVar("T", bound="ChargebeePortalSessionDto")


@attr.s(auto_attribs=True)
class ChargebeePortalSessionDto:
    """
    Attributes:
        id (str): Unique identifier for the portal session
        token (str): Unique pre-authenticated portal session token to access customer portal directly
        access_url (str): Unique URL for accessing the customer portal. Once accessed, this cannot be reused
        status (str): Indicates the current status of the portal session
        created_at (float): Timestamp indicating when this portal session was generated
        customer_id (str): Identifier of the customer
        redirect_url (Union[Unset, str]): URL to redirect when the user logs out from the portal
        expires_at (Union[Unset, float]): Timestamp indicating when the access URL will expire. Once expired, the URL
            cannot be used to login into the portal
        login_at (Union[Unset, float]): Timestamp indicating when this portal session URL was accessed by the user
        logout_at (Union[Unset, float]): Timestamp indicating when this portal session was logged out either by user or
            via API
        login_ipaddress (Union[Unset, str]): IP Address from which the portal session URL was accessed
        logout_ipaddress (Union[Unset, str]): IP Address from which the portal session was logged out either by user or
            via API
        linked_customers (Union[Unset, List[ChargebeeLinkedCustomerDto]]): Identifier of the customer
    """

    id: str
    token: str
    access_url: str
    status: str
    created_at: float
    customer_id: str
    redirect_url: Union[Unset, str] = UNSET
    expires_at: Union[Unset, float] = UNSET
    login_at: Union[Unset, float] = UNSET
    logout_at: Union[Unset, float] = UNSET
    login_ipaddress: Union[Unset, str] = UNSET
    logout_ipaddress: Union[Unset, str] = UNSET
    linked_customers: Union[Unset, List[ChargebeeLinkedCustomerDto]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        token = self.token
        access_url = self.access_url
        status = self.status
        created_at = self.created_at
        customer_id = self.customer_id
        redirect_url = self.redirect_url
        expires_at = self.expires_at
        login_at = self.login_at
        logout_at = self.logout_at
        login_ipaddress = self.login_ipaddress
        logout_ipaddress = self.logout_ipaddress
        linked_customers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.linked_customers, Unset):
            linked_customers = []
            for linked_customers_item_data in self.linked_customers:
                linked_customers_item = linked_customers_item_data.to_dict()

                linked_customers.append(linked_customers_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "token": token,
                "access_url": access_url,
                "status": status,
                "created_at": created_at,
                "customer_id": customer_id,
            }
        )
        if redirect_url is not UNSET:
            field_dict["redirect_url"] = redirect_url
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if login_at is not UNSET:
            field_dict["login_at"] = login_at
        if logout_at is not UNSET:
            field_dict["logout_at"] = logout_at
        if login_ipaddress is not UNSET:
            field_dict["login_ipaddress"] = login_ipaddress
        if logout_ipaddress is not UNSET:
            field_dict["logout_ipaddress"] = logout_ipaddress
        if linked_customers is not UNSET:
            field_dict["linked_customers"] = linked_customers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        token = d.pop("token")

        access_url = d.pop("access_url")

        status = d.pop("status")

        created_at = d.pop("created_at")

        customer_id = d.pop("customer_id")

        redirect_url = d.pop("redirect_url", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        login_at = d.pop("login_at", UNSET)

        logout_at = d.pop("logout_at", UNSET)

        login_ipaddress = d.pop("login_ipaddress", UNSET)

        logout_ipaddress = d.pop("logout_ipaddress", UNSET)

        linked_customers = []
        _linked_customers = d.pop("linked_customers", UNSET)
        for linked_customers_item_data in _linked_customers or []:
            linked_customers_item = ChargebeeLinkedCustomerDto.from_dict(linked_customers_item_data)

            linked_customers.append(linked_customers_item)

        chargebee_portal_session_dto = cls(
            id=id,
            token=token,
            access_url=access_url,
            status=status,
            created_at=created_at,
            customer_id=customer_id,
            redirect_url=redirect_url,
            expires_at=expires_at,
            login_at=login_at,
            logout_at=logout_at,
            login_ipaddress=login_ipaddress,
            logout_ipaddress=logout_ipaddress,
            linked_customers=linked_customers,
        )

        chargebee_portal_session_dto.additional_properties = d
        return chargebee_portal_session_dto

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
