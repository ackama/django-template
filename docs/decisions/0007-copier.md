# 0000 Architectural Decision Record Template

- Date: 2026-01-30
- Author(s): [Jonathan Moss][jmoss]
- Status: `Active`

## Decision

We will adopt [copier][copier] as a tool for creating projects from this template. This
allows us to start building variants more easily.

## Context

Up until now the `django-template` project has used the built-in `startproject` command
to create new projects from this template. This approach was initially chosen as it
represented the simplistic route to getting the template project up and running.
However, it is also extremely limited. The `startproject` command does not currently
provide any mechanisms for extending the range of questions asked - something we need to
be able to start adding _variants_, additional optional project features and
configuration. We would need an external tool to support adding variants to the project
after it was created. Building a maintaining such a tool is entirely possible - and
likely quite fun. But there are also several tools in the Python ecosystem already that
are targeted at this kind functionality. Namely [Cookiecutter][cookie] and more
recently [Copier][copier]

Cookiecutter has been the _defacto_ approach for a while and it works quite well. It
does have some limitations. For example it cannot create files in a loop if that is
needed. Otherwise it is quite capable of doing the job. I have noticed that templates
with _lots_ of options things can get quite complicated in the files with so many
if/else blocks.

Copier is at the surface quite similar to Cookiecutter. It uses a YAML file for config
rather than JSON. Both use jinja2 for templating. Copier however does have 1 key
advantage. It is designed to support smart updates. Creating a project from a template
is not just a one time deal. You can, at a later date run copier _again_ in update mode.
Doing so will ask all the current questions in the template, pre-filling with the
answers from the last time it was run. You can then _change_ your response to questions
or provide answers to new questions and Copier will attempt to apply the necessary
changes to the existing project in a non-destructive way. To the author this is the
killer feature and make one of the problems with template projects less of a concern -
that of keeping existing projects in sync. With the more traditional one and done
approach of Cookie Cutter, once the creation is done and changes in the base template
have to be manually applied to existing project. Or worse, they are applied in a single
existing project and never make it back into the template, which then slowly becomes
outdated and obsolete. One minor annoyance - which might also be a feature depending on
your point of view is that any file that should be processed as a template (i.e. it
contains jinja2 markup) must have a `.jinja` suffix added to it. This looks a little
weird in the template code base but it also makes it quite explicit.

There is a 3rd option, write out our tool designed to work with our own project
structures that either replaces or compliments `startproject`. This approach would be
fun but would likely require significant time investment to create and more to maintain.
It would also likely result in a tool with less features than the existing tools
available.

As such we are going with Copier for the time being.

## Implications

The outcome of choosing Copier is a template that initially works very similar to how
it does with `startproject` but with the option to expand functionality later on. It
also means that many of the template's files now need `.jinja` suffixes which means that
IDEs tend to treat them as text templates rather than python code. So a little more
care is needed over accepting changes to the template project to ensure it continues
to produce valid Django projects.

<!-- Links -->
[jmoss]: mailto:jonathan.moss@ackama.com
[copier]: https://copier.readthedocs.io/en/stable/
[cookie]: https://cookiecutter.readthedocs.io/en/stable/
