---
tags:
    - Configuration
---
# Environment Variables

## Observability

| Variable | Purpose | Default |
| --- | --- | --- |
| `SENTRY_DSN` | Sentry project DSN; unset disables sending events. | unset |
| `SENTRY_ENV` | Sentry environment name. | `production` |
| `SENTRY_TRACES_SAMPLE_RATE` | Fraction of Sentry transactions to trace, from 0 to 1. | `0.0` |
| `SENTRY_PROFILES_SAMPLE_RATE` | Fraction of sampled Sentry transactions to profile, from 0 to 1. | `0.0` |
| `OTEL_ENABLED` | Set to `true` to instrument the Docker web server. | `false` |
| `OTEL_SERVICE_NAME` | Service name attached to OpenTelemetry data. | OpenTelemetry SDK default |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | OTLP collector or backend endpoint. | OpenTelemetry SDK default |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | OTLP transport protocol for the Docker entrypoint. | `http/protobuf` |
| `OTEL_EXPORTER_OTLP_HEADERS` | Authentication headers for the OTLP endpoint. | unset |
| `OTEL_TRACES_EXPORTER` | OpenTelemetry trace exporter. | `otlp` |
| `OTEL_METRICS_EXPORTER` | OpenTelemetry metrics exporter. | `otlp` |
| `OTEL_LOGS_EXPORTER` | OpenTelemetry log exporter when using the Docker entrypoint. | `none` |

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

## `SECRET_KEY`

The Django secret key to use. See the [Django SECRET_KEY][secret-key] documentation for
more details on what this is actually used for, and suitable values.

- default: `None`

<!-- Links -->
[allows-hosts]: https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-ALLOWED_HOSTS
[secret-key]: https://docs.djangoproject.com/en/5.0/ref/settings/#secret-key
[otel-config]: https://opentelemetry.io/docs/languages/sdk-configuration/general/
