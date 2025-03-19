# 0005 Ruff Formatting

- Date: 2023-11-09
- Author(s): [Jonathan Moss][jmoss]
- Status: `Active`

## Decision

Dropping [black][black] and [isort][isort] in favour of [ruff][ruff]

## Context

We have run a series of experiments to assess the benefits and drawbacks of adopting
the tool `ruff` in order to replace `black` and `isort`. Whislt we do not have any major
issues with the 2 existing tools, they do tend to get a little slower on large code
bases. Ruff does have a _slightly_ different position on some formatting choices which
can impact existing code bases. This is similar to the impact that adding `black` to an
existing product can have. For new code bases the impact is minimal.

There is also value in reducing the number of tools and therefore moving parts within
our standard development environment. Here we are able to remove: `isort`, `black`,
`flake8-black`, and `flake8-isort` from our list of dependencies in return for adding
the single new dependency `ruff`. Ultimately this results in less dependencies to keep
on top of.

The use of [invoke][invoke] to wrap our common local development workflows, and re-use
them in our github action flows pay dividends here. The adoption of `ruff` for code
formatting and import sorting only required an update to the `format` task for it to be
the default behaviour locally and for our Continuous Integration (CI) checks.

## Implications

Developers will need to ensure that any IDE's they use are re-configured to use `ruff`
instead of `black` and `isort`.

Ruff is primarily a linting tool. We have not chosen to switch away from
[flake8][flake8] for linting yet as this requires a lot more configuration to match our
current setup. However, the opportunity to reduce our development tooling further by
doing this is a future possibility.

<!-- Links -->
[jmoss]: mailto:jonathan.moss@ackama.com
[black]: https://black.readthedocs.io/en/stable/
[isort]: https://pycqa.github.io/isort/
[ruff]: https://docs.astral.sh/ruff/
[invoke]: https://www.pyinvoke.org/
[flake8]: https://flake8.pycqa.org/en/latest/
