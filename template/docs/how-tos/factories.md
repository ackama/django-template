# Factories

[factory_boy](https://factoryboy.readthedocs.io/en/stable/) is a library for
building test data. It replaces verbose `Model.objects.create(...)` calls with
concise, declarative factory classes that produce valid model instances with
sensible defaults. This keeps tests focused on the behaviour under test rather
than on boilerplate data setup.

## Defining a factory

A factory is a class that knows how to build instances of a Django model. At a
minimum it needs a `Meta.model` and enough attribute defaults to satisfy the
model's database constraints.

```python
import factory

from myapp.accounts.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user-{n}")
    email = factory.Sequence(lambda n: f"user-{n}@example.com")
```

`Sequence` is useful for fields with unique constraints. It produces a
different value on every call, avoiding `IntegrityError`s when creating multiple
instances in the same test.

## Organisation

Organise factories into **one module per Django app** inside the
`tests/factories/` package:

```text
tests/
  factories/
    __init__.py       # re-exports from all app modules
    accounts.py       # factories for the accounts app
    blog.py           # factories for the blog app
    ...
```

The top-level `__init__.py` re-exports every factory so that consumers can
import from a single place:

```python
# tests/factories/__init__.py
from tests.factories.accounts import AdminUserFactory, UserFactory
from tests.factories.blog import PostFactory
```

This means tests can always write:

```python
from tests.factories import UserFactory
```

### Multiple factories per model

In most cases, one factory per model is enough. However, some models have
meaningfully distinct archetypes that warrant their own factory class. A common
example is users:

```python
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user-{n}")
    email = factory.Sequence(lambda n: f"user-{n}@example.com")
    is_staff = False
    is_superuser = False


class AdminUserFactory(UserFactory):
    is_staff = True
    is_superuser = True
```

If the variation is small (a single flag, for example), a
[Trait](#traits) on the base factory may be more appropriate. Reach for a
separate factory when the setup differs significantly or the archetype is used
frequently enough to deserve its own name.

## Using factories in tests

factory_boy provides several strategies for building instances:

| Method           | Saves to DB? | Use when…                                 |
| ---------------- | ------------ | ----------------------------------------- |
| `build()`        | No           | You don't need the object in the database |
| `create()`       | Yes          | The test or code under test queries the DB |
| `build_batch(n)` | No           | You need multiple unsaved instances        |
| `create_batch(n)`| Yes          | You need multiple persisted instances      |

Prefer `build()` over `create()` whenever possible. It is significantly faster
because it skips the database entirely.

```python
import pytest

from tests.factories import UserFactory


@pytest.mark.django_db
def test_user_full_name():
    user = UserFactory.build(first_name="Kiri", last_name="Te Kanawa")

    assert user.get_full_name() == "Kiri Te Kanawa"
```

!!! warning "Always specify the attributes your test depends on"

    Even if the factory default happens to be the value you need today, **pass
    it explicitly** in the test. This protects the test from breaking if the
    factory default changes later and makes the test's intent clear to readers.

    ```python
    # Good - the test is explicit about what matters
    user = UserFactory.create(is_active=True)

    # Bad - relies on the factory default for is_active
    user = UserFactory.create()
    ```

## Related objects

### Foreign keys with `SubFactory`

When a model has a `ForeignKey`, use `SubFactory` to automatically create the
related object:

```python
class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Sequence(lambda n: f"Post {n}")
    author = factory.SubFactory(UserFactory)
```

Calling `PostFactory.create()` will create both a `User` and a `Post`. You can
override the related object or any of its fields:

```python
# Provide an existing user
PostFactory.create(author=some_user)

# Override a field on the auto-created user
PostFactory.create(author__username="custom-author")
```

### Many-to-many with `post_generation`

Many-to-many relationships require the object to be saved before the
relationship can be set. Use `@factory.post_generation` for this:

```python
class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article

    title = factory.Sequence(lambda n: f"Article {n}")

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        self.tags.add(*extracted)
```

Usage:

```python
tag_a = TagFactory.create(name="python")
tag_b = TagFactory.create(name="django")
article = ArticleFactory.create(tags=[tag_a, tag_b])
```

## Traits

Traits let you define named variations on a factory without creating a whole new
class. They are useful for toggling a small number of fields:

```python
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user-{n}")
    is_staff = False
    is_superuser = False

    class Params:
        admin = factory.Trait(
            is_staff=True,
            is_superuser=True,
        )
```

```python
regular_user = UserFactory.create()
admin_user = UserFactory.create(admin=True)
```

## `LazyAttribute`

Use `LazyAttribute` when a field's value should be derived from other fields on
the same factory:

```python
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = "Jane"
    last_name = "Doe"
    email = factory.LazyAttribute(
        lambda obj: f"{obj.first_name}.{obj.last_name}@example.com".lower()
    )
```

```python
user = UserFactory.build(first_name="Kiri", last_name="Te Kanawa")
assert user.email == "kiri.te kanawa@example.com"
```

## Gotchas

### `auto_now` and `auto_now_add` fields

Django fields that use `auto_now=True` or `auto_now_add=True` are **populated
automatically by the ORM** when the object is saved. factory_boy cannot override
these values. Any value you pass will be silently ignored.

If a test needs a specific timestamp on one of these fields, you have two
options:

1. **Freeze time** using a library like
   [time-machine](https://github.com/adamchainz/time-machine):

    ```python
    import time_machine

    @time_machine.travel("2025-06-15 12:00:00T10:00:00", tick=False)
    def test_recent_posts(self):
        post = PostFactory.create()
        assert post.created_at.year == 2025
    ```

2. **Update the row directly** after creation:

    ```python
    from django.utils import timezone

    post = PostFactory.create()
    Post.objects.filter(pk=post.pk).update(
        created_at=timezone.now() - timedelta(days=30)
    )
    post.refresh_from_db()
    ```

You are probably better off building business logic around other fields. Keep the
`auto_now` and `auto_now_add` fields purely for auditing. For example, if you are
recording events in the database, consider adding both a `created_at` field which uses
`auto_now_add` and an `event_published_at` which does not. The `event_published_at` can
still use a default like `timezone.now` but it is now possible to control the value it
holds both during tests, and in code should you need to back-fill that table for
some reason.

### `FileField` and `ImageField`

Use the factory_boy helpers rather than trying to construct file objects
manually:

```python
class DocumentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Document

    attachment = factory.django.FileField(filename="report.pdf")
    thumbnail = factory.django.ImageField(width=100, height=100)
```

## Conventions

### No fuzzy or random attributes

Do **not** use `FuzzyText`, `FuzzyInteger`, `Faker`, or any other source of
randomness in factories. Random values make tests non-deterministic — a test
that passes on one run may fail on the next because the generated data happened
to hit an edge case or constraint violation. These failures are difficult to
reproduce and debug.

Use static values or `Sequence` instead:

```python
# Bad - random value may collide, exceed a max length, or trigger
# unexpected validation
username = factory.Faker("user_name")

# Good - deterministic and predictable
username = factory.Sequence(lambda n: f"user-{n}")
```

### Minimal defaults

Only define defaults that are required to satisfy database constraints (non-null
fields, unique constraints, foreign keys). Leave optional fields unset so that
tests are not coupled to values they don't care about.

### Explicit over implicit

Tests should **always pass the attribute values they rely on**, even when the
factory default happens to match. This makes tests self-documenting and resilient
to factory changes.

```python
# Good - the reader knows exactly what state the test requires
order = OrderFactory.create(status="shipped", total=150)
assert order.is_eligible_for_return()

# Bad - which defaults matter here? What breaks if they change?
order = OrderFactory.create()
assert order.is_eligible_for_return()
```

## Tips

- **Wrap complex setup in a pytest fixture** - if several tests need the same
  object graph, a fixture that calls the factories keeps each test body clean.
- **Keep factories simple** - if a factory becomes complicated, it may be a sign
  that the model itself is doing too much.
