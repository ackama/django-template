import shutil
import subprocess
from pathlib import Path

import typer
import yaml

app = typer.Typer()

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"


def load_config(config_path: Path):
    """Load project settings from YAML configuration file."""
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    return config


def django_start_project(config):
    """Create a Django project using the specified configuration."""
    project_name = config["project_name"]
    template_path = config.get("template_path", "template/")
    output_dir = Path(config.get("output_dir")) or OUTPUT_DIR
    output_dir.mkdir(parents=True, exist_ok=True)
    project_path = output_dir / project_name
    if project_path.exists():
        typer.echo(f"Directory '{project_path}' already exists.")
        if typer.confirm(
            "Do you want to clear this directory and start fresh?", default=False
        ):
            # Delete the existing directory
            shutil.rmtree(project_path)
            typer.echo(f"Cleared the directory: {project_path}")
        else:
            typer.echo("Aborting project creation.")
            raise SystemExit(1)
    project_path.mkdir(parents=True, exist_ok=True)

    # Call django-admin startproject
    typer.echo(f"Starting Django project '{project_name}' in {project_path}...")

    try:
        subprocess.run(
            [
                "django-admin",
                "startproject",
                project_name,
                str(project_path),
                "--template",
                template_path,
                "--extension",
                "py,env,sh,toml,yml",
                "--exclude",
                "nothing",
            ],
            check=True,
        )
        typer.echo(f"Django project '{project_name}' created successfully!")
    except subprocess.CalledProcessError:
        typer.echo(f"Failed to create the project '{project_name}'.", err=True)
        raise SystemExit(1)


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
