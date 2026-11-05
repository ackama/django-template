---
tags:
    - Configuration
---
# Monitor and trace the application

## Report errors with Sentry

Set `SENTRY_DSN` to the DSN for your Sentry project and set `SENTRY_ENV` to a
meaningful environment name. The Django integration reports uncaught request errors,
and release information comes from `GIT_COMMIT_HASH`. The DSN is unset by default,
so no events are sent until it is configured. Errors before initialization, in other
processes, or lost during shutdown or network failure may not be reported.

For a local verification, set `DEBUG=True`, configure the DSN, start the application,
and request `/sentry-debug/`. The endpoint raises an exception and is unavailable when
`DEBUG=False`. Confirm that the event appears in Sentry. Avoid enabling debug mode in
production. Sentry tracing can be enabled using `SENTRY_TRACES_SAMPLE_RATE`; profiling
uses `SENTRY_PROFILES_SAMPLE_RATE` as a fraction of sampled transactions. Both default
to zero. Choose rates appropriate for your traffic, privacy requirements, and budget.

For a project-specific event, use the existing SDK directly:

```python
import sentry_sdk

sentry_sdk.capture_message("Import completed")
```

## Send traces and metrics with OpenTelemetry

For the Docker web server, set `OTEL_ENABLED=true`, `OTEL_SERVICE_NAME` to a stable
service name, and `OTEL_EXPORTER_OTLP_ENDPOINT` to your collector or compatible backend.
The Docker entrypoint defaults to OTLP over HTTP/protobuf, the installed exporter.
Supply credentials via
`OTEL_EXPORTER_OTLP_HEADERS` as required by your backend and use TLS in production.
Using another OTLP protocol requires installing its corresponding exporter.
For example, with a local collector receiving OTLP/HTTP:

```shell
OTEL_ENABLED=true
OTEL_SERVICE_NAME=my-service
OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318
```

The endpoint must be reachable from the application container; `localhost` inside a
container refers to that container. Provision a collector or backend separately. The
web server is not instrumented when `OTEL_ENABLED` is unset or anything other than
`true`. The entrypoint disables OpenTelemetry log export by default; explicitly set
`OTEL_LOGS_EXPORTER` to change that. Django instrumentation produces request traces and
metrics. OpenTelemetry sampling can be configured with `OTEL_TRACES_SAMPLER` and
`OTEL_TRACES_SAMPLER_ARG`. See the [OpenTelemetry configuration reference][otel-config].

To verify without a collector, set `OTEL_TRACES_EXPORTER=console` and
`OTEL_METRICS_EXPORTER=console`, send a request, and inspect the server output. Metrics
are exported periodically. For other processes, including management commands and
non-Docker servers, launch them with `opentelemetry-instrument` and configure the same
OpenTelemetry variables. Set `DJANGO_SETTINGS_MODULE` to your project's settings module
before launching, so Django can be instrumented during startup. Set
`OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf` to use the installed OTLP exporter, and set
`OTEL_LOGS_EXPORTER=none` there as well unless log export
is intended. Do not apply the instrumentation wrapper twice.

The SDK API supports project-specific spans, span events, and metrics:

```python
from opentelemetry import metrics, trace

tracer = trace.get_tracer(__name__)
meter = metrics.get_meter(__name__)
imports = meter.create_counter("imports.completed")

def record_import():
    with tracer.start_as_current_span("import") as span:
        span.add_event("import completed")
        imports.add(1)
```

With no configured OpenTelemetry SDK, these APIs are no-ops. Avoid placing secrets,
personal information, or high-cardinality values in telemetry attributes. Sentry and
OpenTelemetry tracing are independent: enabling both can generate separate traces and
additional volume and cost. Leave Sentry tracing at its default zero when using
OpenTelemetry unless both are deliberately needed. Sentry error reporting remains active
when its DSN is configured.

[otel-config]: https://opentelemetry.io/docs/zero-code/python/configuration/
