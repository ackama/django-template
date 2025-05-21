import pytest
from django.contrib.auth import get_user_model

from {{ project_name }}.accounts import models


@pytest.mark.django_db
def test_create_user() -> None:
    User = get_user_model()
    user = User.objects.create_user(username="test", password="123")  # noqa: S106

    assert User is models.User
    assert user.username == "test"
    assert user.is_active
    assert not user.is_staff
    assert not user.is_superuser
    assert user.email == ""


@pytest.mark.django_db
def test_create_superuser() -> None:
    User = get_user_model()
    admin_user = User.objects.create_superuser(
        username="superuser", password="123"  # noqa: S106
    )

    assert User is models.User
    assert admin_user.username == "superuser"
    assert admin_user.is_active
    assert admin_user.is_staff
    assert admin_user.is_superuser
    assert admin_user.email == ""
