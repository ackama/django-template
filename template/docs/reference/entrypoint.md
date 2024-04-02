---
tags:
  - Docker
  - Commands
---
# Docker Entry Point

The docker image produced by this service has a custom entrypoint (defined in
`src/entrypoint.sh`). This entry point support a small range of operations.

If no operation is supplied the docker image will attempt to perform  migrations then
starts the service.

If a operation is supply then it is treated as described below:

## migrate

`migrate` applies any outstanding migrations then terminates. It is run with the
`--no-input` flag and any additional parameters are passed through directly.

## run

The `run` operation will run the service (without first running migrations).

## bash

The `bash` operation runs a regular bash shell, best combined with the `-it` docker run
switches to ensure you are provided with a fully interactive terminal from which to
continue working.

Note that if additional parameters are passed supplied after the `bash` operations as
part of the docker run command, they will be forwarded on to bash itself.

## _<anything-else>_

Any other value supplied as an operation will be passed directly to Django's `manage`
command. So for example is you run with `shell`, the is the equivalent of
`./manage.py shell`. This is handy for management commands that are intended to be used
for _cron_ style job for example.
