# Django Template Project

Expected Python Version: 3.12.x

## Purpose

This project is intended as:

- a kick-off point for projects
- an evolving codebase which implements our best practices at the time
- a place where we can document decisions that have been made about practices
    - e.g.: why X was picked, why Y was avoided (+ pros & cons)

## Usage

To create a new project from this template, you can use [Copier][copier]. The simplest
way to run copier is with [pipx][pipx] or [uvx][uvx]:

```shell
pipx run copier copy path/to/django-template <project_folder>
```

or

```shell
uvx copier copy path/to/django-template <project_folder>
```

You can pull the template directly from Github:

```shell
uvx copier copy gh:ackama/django-template <project_folder>
```

This will ask you a series of questions to help you configure your project. The answer
you provide to these questions will also be recorded in your new project in a file
called `.copier-answers.yml`.y

Running the copier command will create a new project in the folder specified in
with `<project_folder>`.

> [!NOTE]
> Copier has an `update` mode which allows you to change your answers to the setup
> questions at a later date. Your current project _must_ be under git control for this
> to work. It works pretty well but has not been tested here after lots of changes to
> the project have be made since the copy. So use caution.

## Contributing

If you have ideas for improvements, open a PR with your idea or propose it in the guild
channel

Feature branches are encouraged, and merging should on consensus from guild

<!-- Links -->
[copier]: https://copier.readthedocs.io/en/stable/
[pipx]: https://pypa.github.io/pipx/
[uvx]: https://docs.astral.sh/uv/guides/tools/