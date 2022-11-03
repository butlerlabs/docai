from enum import Enum


class BillingSubscriptionNameV2(str, Enum):
    DEVELOPER = "Developer"
    INACTIVE = "Inactive"
    DEV15 = "Dev15"
    ENTERPRISE = "Enterprise"
    LITE = "Lite"
    PRO = "Pro"
    USAGE = "Usage"
    MONTHLY99 = "Monthly99"
    MONTHLY499 = "Monthly499"
    TRIAL = "Trial"

    def __str__(self) -> str:
        return str(self.value)
