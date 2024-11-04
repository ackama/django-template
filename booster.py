import subprocess
from pathlib import Path

import typer
import yaml

app = typer.Typer()


def load_config(config_path: Path):
    """Load project settings from YAML configuration file."""
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    return config


def django_start_project(config):
    """Create a Django project using the specified configuration."""
    project_name = config["project_name"]

    # Call django-admin startproject
    typer.echo(f"Starting Django project '{project_name}'...")
    subprocess.run(
        [
            "django-admin",
            "startproject",
            project_name,
            "--template",
            "template/",
            "--extension",
            "py,env,sh,toml,yml",
            "--exclude",
            "nothing",
        ]
    )

    typer.echo(f"Django project '{project_name}' created successfully!")


@app.command()
def fire(
    config_path: Path = typer.Option(
        "./sample_config.yml",
        "--config",
        help="Path to the project configuration YAML file",
    )
):
    """
    Start a new Django project using Ackama's django template
    based on a YAML configuration file.
    """
    config = load_config(config_path)
    django_start_project(config)


if __name__ == "__main__":
    app()
