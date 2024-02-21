# Django Template Project

Expected Python Version: 3.12.x

## Purpose

This project is intended as:

- a kick-off point for projects
- an evolving codebase which implements our best practices at the time
- a place where we can document decisions that have been made about practices
    - e.g.: why X was picked, why Y was avoided (+ pros & cons)

## Usage

To create a new project from this template, you must have the most recent stable version
of Django installed in order to run the `startproject` command. The simplest way to do
this is with [pipx][pipx]:

```shell
pipx install django
```

This will ensure that the `django-admin` command is available in your shell. From there
you can create a new project with the following command:

```shell
django-admin startproject --template path/to/django-template/template/ --extension py,env,sh,toml,yml <project_name>
```

!!! warn
    The name of your project _must_ be a valid Python package name - that means
    underscores (`_`) not hyphens (`-`) for name separators please.

Running the Django admin command will create a new project in the folder specified in
with `<project_name>`.

## Contributing

If you have ideas for improvements, open a PR with your idea or propose it in the guild
channel

Feature branches are encouraged, and merging should on consensus from guild

<!-- Links -->
[pipx]: https://pypa.github.io/pipx/
