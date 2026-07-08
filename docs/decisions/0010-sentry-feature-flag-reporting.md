# 0010 Report Feature Flag Evaluations to Sentry

- Date: 2026-06-10
- Author(s): [Bardi Harborow][bardi]
- Status: `Active`

## Decision

When `use_feature_toggles` is enabled, generated projects replace django-waffle's
built-in `Flag`, `Switch`, and `Sample` models with custom models in a
`<project_module>.flags` app. The custom models override `is_active()` to report
each evaluation to Sentry via [`sentry_sdk.feature_flags.add_feature_flag`][api],
after delegating to waffle's own logic.

## Context

Sentry attaches evaluated feature flags to error and transaction events, making
it possible to see which toggles were active for the request in which an error
occurred. Sentry's Python SDK ships integrations for LaunchDarkly, OpenFeature,
Statsig, and Unleash, but [not for django-waffle][docs]; unsupported providers
are expected to use the generic `add_feature_flag` API.

django-waffle has no "flag evaluated" signal, but its models are
[swappable][swappable] (`WAFFLE_FLAG_MODEL`, `WAFFLE_SWITCH_MODEL`,
`WAFFLE_SAMPLE_MODEL`). Overriding `is_active()` on custom models catches every
evaluation path — `flag_is_active()`, decorators, template tags, and middleware
— because they all funnel through the models.

`add_feature_flag` records evaluations on Sentry's per-request isolation scope
and is safe to call when no Sentry DSN is configured, so the reporting needs no
configuration of its own.

## Implications

The flags app vendors an initial migration that mirrors django-waffle's abstract
models. A future django-waffle release that adds or alters fields would make the
migration incomplete; the template CI's `check-migrations` task
(`makemigrations --dry-run --check`) surfaces this, and a follow-up migration
fixes it — the same trade-off the custom user model accepts for Django's auth
fields.

Waffle's admin module registers its default models, which are swapped out in
generated projects; Django silently ignores registrations of swapped-out
models. The flags app registers the custom models with waffle's own
`ModelAdmin` classes instead, so the admin experience is unchanged.

Only boolean results are reported. A missing flag evaluates to
`WAFFLE_FLAG_DEFAULT` (`False`) and is reported as such; in the rare case a
flag evaluation returns `None`, nothing is reported.

<!-- Links -->
[bardi]: mailto:bardi@bardiharborow.com
[api]: https://docs.sentry.io/platforms/python/feature-flags/#generic-api
[docs]: https://docs.sentry.io/platforms/python/feature-flags/
[swappable]: https://waffle.readthedocs.io/en/stable/types/index.html
