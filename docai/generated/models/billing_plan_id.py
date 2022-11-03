from enum import Enum


class BillingPlanId(str, Enum):
    BUTLER_LITE_ANNUAL = "butler-lite-annual"
    BUTLER_LITE_MONTHLY = "butler-lite-monthly"
    BUTLER_PRO_ANNUAL = "butler-pro-annual"
    BUTLER_PRO_MONTHLY = "butler-pro-monthly"
    BUTLER_PRO_USAGE = "butler-pro-usage"
    BUTLER_MONTHLY_99 = "butler-monthly-99"
    BUTLER_MONTHLY_499 = "butler-monthly-499"
    BUTLER_DEV_15 = "butler-dev-15"

    def __str__(self) -> str:
        return str(self.value)
