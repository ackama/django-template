from typing import Any

from django import http
from django.conf import settings
from django.views import generic


class HumansTxt(generic.TemplateView):
    """
    Render the humans.txt template

    See <https://humanstxt.org/> for details of what this actually is.
    """

    content_type = "text/plain"
    template_name = "pages/humans.txt"


class Release(generic.View):
    """
    Provides a simple endpoint for release specifications
    """

    def get(
        self, request: http.HttpRequest, *args: Any, **kwargs: Any
    ) -> http.HttpResponse:
        return http.JsonResponse(
            data={
                "hash": settings.GIT_COMMIT_HASH,
                "timestamp": settings.GIT_COMMIT_TIME,
                "revision": settings.GIT_COMMIT_COUNT,
            }
        )


class SentryDebug(generic.View):
    """
    Raise an error to test Sentry error reporting
    """

    def get(
        self, request: http.HttpRequest, *args: Any, **kwargs: Any
    ) -> http.HttpResponse:
        raise ValueError("This is a test error for Sentry")
