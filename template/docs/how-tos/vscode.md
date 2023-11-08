---
tags:
    - vscode
---
# Recommended Configuration for VSCode

This document is a work in progress

## Plugins

- Python
- markkdownlint
- DotEnv
- Docker
- TOML Language Support

## Settings

TODO: This is just _my_ overrides from the default user settings. Need something more
comprehensive.

In `.vscode/setting.json`

```json
{
    "python.terminal.activateEnvironment": false,
    "python.testing.pytestArgs": [
        "src/tests"
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true,
    "markdownlint.config": {
        "MD007": {
            "indent": 4
        },
        "MD013": {
            "line_length": 88
        }
    }
}
```

## Launch

In `.vscode/launch.json`

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Django",
            "type": "python",
            "request": "launch",
            "cwd": "${workspaceFolder}/src",
            "program": "django_template/manage.py",
            "args": [
                "runserver",
            ],
            "django": true,
            "justMyCode": true
        },
    ]
}

```
