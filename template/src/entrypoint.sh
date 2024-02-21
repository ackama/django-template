#! /bin/bash
set -e

if [ -z "$1" ] # nothing specified so we bootstrap the service itself
then
    manage migrate --noinput
    exec gunicorn -b 0.0.0.0:8000 -w 4 -k uvicorn.workers.UvicornWorker {{ project_name }}.main.asgi:application
elif [ "$1" = "run" ]  # run the service only
then
    exec gunicorn -b 0.0.0.0:8000 -w 4 -k uvicorn.workers.UvicornWorker {{ project_name }}.main.asgi:application
elif [ "$1" = "migrate" ]  # run database migrations
then
    exec manage migrate --noinput "${@:2}"
elif [ "$1" = "bash" ]  # run a regular bash shell
then
    exec bash "${@:2}"
else # pass any other params directly to manage.py to handle
    exec manage "$@"
fi
