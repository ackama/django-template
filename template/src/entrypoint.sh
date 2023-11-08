#! /bin/bash
set -e

if [ -z "$1" ] # nothing specified so we bootstrap the service itself
then
    manage migrate --noinput
    exec uvicorn --loop=uvloop --host=0.0.0.0 django_template.main.asgi:application
elif [ "$1" = "run" ]  # run the service only
then
    exec uvicorn --loop=uvloop --host=0.0.0.0 django_template.main.asgi:application
elif [ "$1" = "migrate" ]  # run database migrations
then
    exec manage migrate --noinput "${@:2}"
elif [ "$1" = "bash" ]  # run a regular bash shell
then
    exec bash "${@:2}"
else # pass any other params directly to manage.py to handle
    exec manage "$@"
fi
