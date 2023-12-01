import json

from {{ project_name }}.main import views


def test_releases_view_includes_revision_details(settings, rf):
    settings.GIT_COMMIT_HASH = "HASH"
    settings.GIT_COMMIT_TIME = 1680476379
    settings.GIT_COMMIT_COUNT = 42

    view = views.Release.as_view()
    response = view(request=rf.get("/release.json"))

    assert response.status_code == 200
    payload = json.loads(response.content)
    assert payload == {"hash": "HASH", "timestamp": 1680476379, "revision": 42}
