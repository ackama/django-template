---
tags:
    - Configuration
---
# Environmental Variables

## `ALLOWED_HOSTS`

A list of host that are permitted to make requests. See the
[Django ALLOWED_HOSTS][allows-hosts] documentation for more details of it purpose and
options.

- default: `"*"`

## DATABASE_URL

The database connection string from the default database.

- default: `"postgres://dev:dev_password@localhost:5432/dev"`

## `DEBUG`

- default: `False`

## `GIT_COMMIT_COUNT`

The number of commits on the main branch that form this release.

- default: `None`

## `GIT_COMMIT_DATE`

The date of the last GIT commit on the main branch that form this release.

- default: `None`

## `GIT_COMMIT_HASH`

The hash of the last GIT commit on the main branch that form this release.

- default: `None`

## `SECRET_KEY`

The Django secret key to use. See the [Django SECRET_KEY][secret-key] documentation for
more details what this is actually used for and suitable values.

- default `None`

<!-- Links -->
[allows-hosts]: https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-ALLOWED_HOSTS
[secret-key]: https://docs.djangoproject.com/en/4.1/ref/settings/#secret-key
