---
tags:
    - Installation
    - Configuration
    - Setup
---
# Your First Day

So it is your first day on the project, where do you start? Here!

This tutorial will guide you through getting the project up and running as well as
making your first update to the code.

## Installing _pyenv_ & Python

!!! warning
    If you are not running a standard BASH shell then I'd recommend you read through the
    docs at <https://github.com/pyenv/pyenv> to be sure you get up and running safely.

### macOS

Installing pyenv on macOS is most easily achieved with [Homebrew][homebrew], you
probably already have homebrew installed, but if not you can follow the instructions on
<https://brew.sh/>

To install pyenv with homebrew you need to perform the following 2 commands in a
terminal:

```shell
brew update
brew install pyenv
```

Once you have done that you need to ensure that `pyenv init` is run when you open a
terminal window with the following command:

```shell
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
```

Now close and re-open your terminal for changes to take effect. Pyenv build Python from
scratch the first time you install a specific version. As such you will need a suitable
build environment and supporting libraries. Details for various platforms can be found
on the Pyenv wiki in the [common build problems][pyenv-build] section.

Then to install Python:

```shell
pyenv install 3.12.2
```

### Linux

The easiest way to install pyenv on Linux is to use the pyenv-installer:

```shell
curl https://pyenv.run | bash
```

This will download the latest version of pyenv and configure your shell to use it. You
will need to exit and restart your terminal for the changes to be picked up.

Pyenv build Python from scratch the first time you install a specific version. As such
you will need a suitable build environment and supporting libraries. Details for various
platforms can be found on the Pyenv wiki in the [common build problems][pyenv-build]
section.

Then to install Python:

```shell
pyenv install 3.12.2
```

## Preparing your Development Environment

You need to start your preparation by ensuring the correct version of Python is activated
in your shell.

```shell
pyenv shell 3.12.2
```

This project uses [Poetry][poetry] for Python virtual environment and dependency
management. The installation of poetry is automated by a bash script they provide. This
will ensure that the appropriate isolated environment is created for poetry:

```shell
curl -sSL https://install.python-poetry.org | python -
```

The installer creates a poetry wrapper in a well-known, platform-specific directory:

- `$HOME/.local/bin` on Linux/macOS/Unix
- `$POETRY_HOME/bin` if `$POETRY_HOME` is set.

If this directory is not present in your `$PATH`, you can add it in order to invoke
Poetry as `poetry`. You can check things are working correctly with the following:

```shell
poetry --version
```

If everything is working correctly it should print the current version of poetry.

As a final step you need configure poetry to work nicely with pyenv and to place the
virtual environment it creates in the same folder as the projects itself (in the folder
`.venv`):

```shell
poetry config virtualenvs.prefer-active-python true
poetry config virtualenvs.in-project true
```

This project also used [invoke][pyinvoke] for automating the various processes you might
need to do on a day to day basis. Whilst poetry is used for managing your virtual
environment, it is handy to have invoke installed globally within you pyenv environment
so you do not need to prefix every call with `poetry run invoke ...`. You can install it
within the current pyenv environment with:

```shell
pip install invoke
```

## Checking out the project

Now that everything is prepared, you can get to checking out a copy of the project from
Github and completing the setup.

```shell
git clone git@github.com:a-musing-moose/django_template.git
```

The change directory into your newly cloned copy of the source code and complete the
set up:

```shell
cd django_template
```

Then set the version of python you want to use for this project every time you open it:

```shell
pyenv local 3.12.2
```

Take the example configuration file and make a copy for your local development:

```shell
cp example.env .env
```

And then finally create the virtual environment and install all the dependencies with:

```shell
poetry install
```

You are now all set to make your first change!

## Making your first change

Your first change will be to add yourself to the list of humans who have worked on the
project.

This project uses a simple [trunk based][trunkbased] approach to developing features
with short lived feature branches. So your first step making a change should always be
to create a new feature branch.

Within a terminal opened at the root of this project type:

```shell
git checkout -b add_name_to_humans_txt
```

This will create a new branch for your change.

Your change will be in `src/templates/pages/humans.txt`. Open this file and add
yourself! There is at least one example in there already you can copy. If you don't feel
comfortable sharing your Github name or general location that is fine, you do not need
to provide them.

Once you have made you change we need to commit it:

```shell
git add src/templates/pages/humans.txt
git commit -m "Adds me to the list of humans involved in this project"
```

This will first stage the change with the `git add` then commit to the change with the
`git commit`. For day to day commits we would expect a little more detail in the commit
message, but for this first day the above message is fine.

Next we need to create a pull request so others can review and approve you change.

```shell
git push origin add_name_to_humans_txt
```

This will push your branch up to Github. You can then use the Github website itself to
create the pull request - note that output from the `git push` actually includes a link
to Github that will take you straight to the correct place to do this.

Please provide a description of the change you are making, why you are making it and
ideally some pointers for the reviewer that would allow them to double check the change
is acting as intended.

Now you wait. A team member will review your changes and assuming they are happy with it
approve the change. Once they do you can click the `merge` button and add your change to
the `main` branch.

You can view your change once deployed at `https://<hostname>/humans.txt`

!!! note
    As a second change, consider the tutorial you just completed. Were any of the steps
    unclear? Did anything just _not_ work? Create new branch from the `main` branch and
    update this tutorial with anything you think needs fixing up. You can find the
    source for this tutorial at `docs/tutorials/your-first-day.md`

<!-- Links -->
[homebrew]: https://brew.sh/
[pyenv-build]: https://github.com/pyenv/pyenv/wiki/common-build-problems
[poetry]: https://python-poetry.org/
[pyinvoke]: https://www.pyinvoke.org/
[trunkbased]: https://trunkbaseddevelopment.com/
