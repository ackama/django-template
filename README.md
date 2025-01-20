# Django Template Project

Expected Python Version: 3.12.x

## Purpose

This project is intended as:

- a kick-off point for projects
- an evolving codebase which implements our best practices at the time
- a place where we can document decisions that have been made about practices
    - e.g.: why X was picked, why Y was avoided (+ pros & cons)

## Usage

To create a new Django project using this template, you have two options:

### Option 1: Build the Package and Run the Installed booster Command (WIP)

1. Build the package:

```bash
python -m build
```

2. Install it with `pipx`:

```bash
pipx install dist/booster-<version>.whl
```

1. Run the booster command:

```bash 
booster --config path_to_config.yml
```

### Option 2: Run Directly Without Building

If you don't want to build the package, you can run the script directly from the source:

```bash
python src/booster.py fire --config sample_config.yml
```

Both options allow you to generate a new project dynamically based on your configuration file.

> [!NOTE]
> The config file should specify details such as the project name. Refer to `sample_config.yml` for an example. If no configuration file is provided, the CLI will default to using `sample_config.yml`.

> [!WARNING]
> The name of your project _must_ be a valid Python package name - that means
> underscores (`_`) not hyphens (`-`) for name separators please.


## Contributing

If you have ideas for improvements, open a PR with your idea or propose it in the guild
channel

Feature branches are encouraged, and merging should on consensus from guild

<!-- Links -->
[pipx]: https://pypa.github.io/pipx/
