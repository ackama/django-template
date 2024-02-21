# 0002 Use Gunicorn as a Process Manager

- Date: 2024-02-09
- Author(s): [Jonathan Moss][jmoss]
- Status: `Active`

## Decision

We will continue to use [Uvicorn][uvicorn] in order to support running Django in an
asynchronous (ASGI) manner. However, we will use it as a [Gunicorn][gunicorn] worker
rather than in stand alone mode.

## Context

In order to work with asynchronous views and functions, Django must be run within an
ASGI host. For this we previously chose Uvicorn, in part becasue it makes use the Cython
based uvloop to efficiently manage the event loop.

Uvicorn, because it focuses on asynchronous operations, runs as effectively a single
process,  instead relying on asynchronous tasks to manage concurrency. This is fine when
there is a low level of contention and the majority of tasks are co-operative and
non-blocking. For greater resilience and for more easily achieving updates without
dropping requests, [it is recommended][recommended] that Uvicorn is used as a _worker_
inside a process manager. For this reason it provides a Gunicorn compatible worker.

So Gunicorn handles the socket setup, start-up of multiple server processes, monitoring
process aliveness, and listens for signals to provide for processes restarts, shutdowns,
or dialing up and down the number of running processes. Uvicorn then handles each
individual request/response cycle.

## Implications

This does introduce another moving part. It is however, a well known and commonly used
component of a Django stack. The interaction of the two (Gunicorn and Uvicorn) may
necessitate slightly different configuration that is usual in order to work together
smoothly - something we won't know with any certainty until with try it under a
production-like load.

It is worth noting that at the present time, neither Gunicorn or Uvicorn support
HTTP/2.0 or above. The majority of the benefits of HTTP/2.0 come from it's ability to
multiplex requests. A feature that is of greatest benefit between the client and the
server where latency is significant. It also requires the communication of occur over
a TLS connection. In most production deployments Gunicorn will be behind a reverse proxy
such as Nginx. Nginx does support HTTP/2.0 as well as typically being used for TLS
termination. Given that the reverse proxy should be within the same network as the
Gunicorn host, the latency will be minimal. As such, we do not see the lack of HTTP/2.0
support in Gunicorn and Uvicorn as an immediate concern.

<!-- Links -->
[jmoss]: mailto:jonathan.moss@ackama.com
[uvicorn]: https://www.uvicorn.org/
[gunicorn]: https://gunicorn.org/
[recommended]: https://www.uvicorn.org/deployment/#using-a-process-manager

<!-- Abbreviations -->
*[ASGI]: Asynchronous Server Gateway Interface
*[TLS]: Transport Layer Security
