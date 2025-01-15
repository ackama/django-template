# 0002 Remove Gunicorn as a Process Manager

- Date: 2025-01-015
- Author(s): [Jonathan Moss][jmoss]
- Status: `Active`

## Decision

[Uvicorn][uvicorn] now has built in support for process management, so we no longer need
[Gunicorn][gunicorn] as well.

## Context

An ASGI runtime is needed to support asyncio operations in Django. We currently use
Uvicorn for this. Previously Uvicorn ran as a single process and it was recommended that
Gunicorn was used as a process manager, configured to use Uvicorn purely for the
workers. This is no longer the case, as of release [0.30.0][release] Uvicorn now has
built in process management support.

## Implications

This removes one of the moving part of our stack, reducing the over all number of
packages we need to understand and keep up to date.

Whilst some benchmarking has been performed - it is not exhaustive. The general results
however show a comparable level of throughput to what we had with the previous gunicorn
setup.

<!-- Links -->
[jmoss]: mailto:jonathan.moss@ackama.com
[uvicorn]: https://www.uvicorn.org/
[gunicorn]: https://gunicorn.org/
[release]: https://www.uvicorn.org/release-notes/#0300-2024-05-28

<!-- Abbreviations -->
*[ASGI]: Asynchronous Server Gateway Interface
