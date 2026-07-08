"""
Custom django-waffle models that report each evaluation to Sentry.

Sentry attaches the reported flags to error and transaction events for the
current request, making it possible to see which feature toggles were active
when an error occurred.

See also: <https://docs.sentry.io/product/issues/issue-details/feature-flags/>
"""

from django.http import HttpRequest
from sentry_sdk.feature_flags import add_feature_flag
from waffle.models import (
    AbstractBaseSample,
    AbstractBaseSwitch,
    AbstractUserFlag,
)


class Flag(AbstractUserFlag):
    def is_active(
        self, request: HttpRequest, read_only: bool = False
    ) -> bool | None:
        result = super().is_active(request, read_only)
        if result is not None:
            add_feature_flag(self.name, result)
        return result


class Switch(AbstractBaseSwitch):
    def is_active(self) -> bool:
        result = super().is_active()
        add_feature_flag(self.name, result)
        return result


class Sample(AbstractBaseSample):
    def is_active(self) -> bool:
        result = super().is_active()
        add_feature_flag(self.name, result)
        return result
