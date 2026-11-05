---
tags:
    - Configuration
---
# Environment Variables

See the [observability how-to](../how-tos/observability.md) for setup, sampling,
verification, and examples. See the [OpenTelemetry SDK configuration][otel-config]
for additional settings and protocol-specific endpoint defaults.

## `ALLOWED_HOSTS`

A list of hosts that are permitted to make requests. See the
[Django ALLOWED_HOSTS][allows-hosts] documentation for more details of its purpose and
options.

- default: `"*"`

## `DATABASE_URL`

The database connection string for the default database.

- default: `"postgres://dev:dev_password@localhost:5432/dev"`

## `DEBUG`

- default: `False`

## `GIT_COMMIT_COUNT`

The number of commits on the main branch that forms this release.

- default: `None`

## `GIT_COMMIT_DATE`

The date of the last Git commit on the main branch that forms this release.

- default: `None`

## `GIT_COMMIT_HASH`

The hash of the last Git commit on the main branch that forms this release.

- default: `None`

## `OTEL_ENABLED`

Set to `true` to instrument the Docker web server.

- default: `false`

## `OTEL_EXPORTER_OTLP_ENDPOINT`

The OTLP collector or backend endpoint.

- default: OpenTelemetry SDK default

## `OTEL_EXPORTER_OTLP_HEADERS`

Authentication headers for the OTLP endpoint.

- default: unset

## `OTEL_EXPORTER_OTLP_PROTOCOL`

The OTLP transport protocol for the Docker entrypoint.

- default: `http/protobuf`

## `OTEL_LOGS_EXPORTER`

The OpenTelemetry log exporter when using the Docker entrypoint.

- default: `none`

## `OTEL_METRICS_EXPORTER`

The OpenTelemetry metrics exporter.

- default: `otlp`

## `OTEL_SERVICE_NAME`

The service name attached to OpenTelemetry data.

- default: OpenTelemetry SDK default

## `OTEL_TRACES_EXPORTER`

The OpenTelemetry trace exporter.

- default: `otlp`

## `SECRET_KEY`

The Django secret key to use. See the [Django SECRET_KEY][secret-key] documentation for
more details on what this is actually used for, and suitable values.

- default: `None`

## `SENTRY_DSN`

The Sentry project DSN. When unset, events are not sent.

- default: unset

## `SENTRY_ENV`

The Sentry environment name.

- default: `production`

## `SENTRY_PROFILES_SAMPLE_RATE`

The fraction of sampled Sentry transactions to profile, from 0 to 1.

- default: `0.0`

## `SENTRY_TRACES_SAMPLE_RATE`

The fraction of Sentry transactions to trace, from 0 to 1.

- default: `0.0`

<!-- Links -->
[allows-hosts]: https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-ALLOWED_HOSTS
[secret-key]: https://docs.djangoproject.com/en/5.0/ref/settings/#secret-key
[otel-config]: https://opentelemetry.io/docs/languages/sdk-configuration/general/
