# 0006 Ruff Linting

- Date: 2025-05-20
- Author(s): [Jonathan Moss][jmoss]
- Status: `Active`

## Decision

Dropping [flake8] and related plugins in favour of [ruff]

## Context

We [previously][ruff-for-formatting] switched to `ruff` for code formatting and import
sorting. We have been experimenting with also using `ruff` for linting. We previously
held off on this as it supports a _lot_ of different linting rules which can lead to
[bike-shedding]. So for these experiments we choose to replicate the current `flake8`
based rules and nothing more. This provided fairly straight forward to achieve with
minimal configuration.

There is also value in reducing the number of tools and therefore moving parts within
our standard development environment. We already had `ruff` installed and by making this
change we were able to remove not only `flake8` but also [flake8-bandit],
[flake8-bugbear] and [flake8-builtins].

The use of [invoke] to wrap our common local development workflows, and re-use them in
our github action flows pay dividends here. The adoption of `ruff` for code formatting
and import sorting only required an update to the `lint` task for it to be the default
behaviour locally and for our Continuous Integration (CI) checks.

## Implications

Developers will need to ensure that any IDE's they use are re-configured to use `ruff`
instead of `flake8` for linting.

There is still a lot more possible linting rules that we could set up - and it is worth
checking what else is available as long as we are partical about it and don't go too far
down the hole and end up bike-shedding out configurations too often.

<!-- Links -->

[bike-shedding]: https://en.wikipedia.org/wiki/Law_of_triviality
[flake8]: https://flake8.pycqa.org/en/latest/
[flake8-bandit]: https://github.com/tylerwince/flake8-bandit
[flake8-bugbear]: https://github.com/PyCQA/flake8-bugbear
[flake8-builtins]: https://github.com/gforcada/flake8-builtins
[invoke]: https://www.pyinvoke.org/
[jmoss]: mailto:jonathan.moss@ackama.com
[ruff]: https://docs.astral.sh/ruff/
[ruff-for-formatting]: 0005-ruff-formatting.md
