# 0004 Replacing startproject with a CLI Wrapper

- Date: 2024-11-22
- Author(s): [Zahra Alizadeh][zahra]
- Status: `Draft`

## Decision

We have decided to build a custom CLI Django's built-in `startproject` command. This wrapper will run `startproject` to scaffold the initial project and then apply additional configuration and customizations based on a user-defined configuration file. This approach allows us to dynamically customize project structures based on configuration files and support reusable variants.

## Context

### Background

Django's `startproject` command provides a basic project scaffolding mechanism. While this is sufficient for standard projects, it falls short when projects require:

- Dynamic configurations, such as database engines, general settings e.g. timezone, and optional components and apps.
- Customizable directory and file structures tailored to team or project-specific needs.
- Reusability across multiple projects with different configurations or variants (e.g., Docker, Celery, or CI/CD pipelines).

### Existing Approach


The current approach uses `django-admin startproject` with the `--template` option to specify a custom project template. While this allows some customization, it introduces several issues:

1. __Complex Command Syntax__:
   The command requires specifying a full template path along with multiple options like `--extension` and `--exclude`. Example:

```shell
django-admin startproject --template path/to/django-template/template/ --extension py,env,sh,toml,yml --exclude nothing <project_name>
```
   This is verbose, error-prone, and hard to remember.

2. __Limited Customization__:
   - The `--template` option does not support dynamic rendering of file names or content, or conditional inclusion of components.
   - Custom features (e.g., Celery support or different configurations) requires separate templates or post-processing.


This approach is overly complicated, lacks flexibility, and is not scalable for dynamic, reusable templates. A simpler, more customizable solution is needed to improve developer productivity and enforce consistency.

## New Approach


The custom CLI wrapper enhances this process by:

1.	Running the `startproject` command to scaffold the project.
2.	Applying additional setup steps, such as:
   - Modifying settings.py to add optional configurations (e.g., databases, installed apps).
   - Adding optional files (e.g., .env, Dockerfiles) based on user preferences.
3.	Allowing users to configure the setup via a YAML or TOML configuration file.


## Implications

### Positive Implications

1. __Flexibility__:
   - Supports dynamic configurations (e.g., different database backends, optional apps).
   - Simplifies the addition of reusable variants like Docker or CI/CD pipelines.

2. __Consistency__:
   - Enforces consistent project structures across teams and projects.
   - Reduces human error in project setup.

3. __Future Scalability__:
   - New variants or configurations can be added without disrupting existing workflows.

4. __Customization__:
   - Allows user-defined settings through configuration files (e.g., YAML or TOML).

### Negative Implications

1. __Initial Overhead__: Developing and testing the CLI wrapper requires upfront investment
2. __Maintenance__: The templates and wrapper tool will need to be maintained as requirements evolve.
3. __Learning Curve__: Developers familiar with startproject will need to learn the new CLI tool.

<!-- Links -->
[zahra]: mailto:zahra.alizadeh@ackama.com
