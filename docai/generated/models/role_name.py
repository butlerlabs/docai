from enum import Enum


class RoleName(str, Enum):
    ADMIN = "admin"
    REVIEWER = "reviewer"
    WAITLISTED = "waitlisted"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
