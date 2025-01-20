# Packaging Stage
# ===============

FROM python:3.12.8-slim-bookworm as packager
ENV PYTHONUNBUFFERED=1
RUN pip install -U pip && pip install poetry poetry-plugin-export
COPY README.md pyproject.toml poetry.lock /source/
COPY src /source/src/
WORKDIR /source/

# Uses export to get a pinned list of requirements
RUN rm -rf dist && poetry export -o requirements.txt && poetry build


# Building Stage
# ==============

FROM python:3.12.8-slim-bookworm as builder
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    build-essential \
    libffi-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN python -m venv /venv/

# _activate_ the virtual environment
ENV VIRTUAL_ENV=/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install -U pip

# Install pinned dependencies
COPY --from=packager /source/requirements.txt /
RUN pip install -r requirements.txt

# Install the application itself
COPY --from=packager /source/dist/*.whl /
RUN pip install --no-deps *.whl

# Final Runtime
# =============

FROM python:3.12.8-slim-bookworm as runtime
ENV PYTHONUNBUFFERED=1

ARG GIT_COMMIT_HASH
ARG GIT_COMMIT_TIME
ARG GIT_COMMIT_COUNT
ENV GIT_COMMIT_HASH=${GIT_COMMIT_HASH}
ENV GIT_COMMIT_TIME=${GIT_COMMIT_TIME}
ENV GIT_COMMIT_COUNT=${GIT_COMMIT_COUNT}

# Runtime deps
RUN apt-get update && apt-get install -y \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /venv /venv

# _activate_ the virtual environment
ENV VIRTUAL_ENV=/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Set user and add entrypoint script
RUN useradd -u 1000 runtime
COPY --chown=runtime:runtime src/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

USER runtime
EXPOSE 8000
ENTRYPOINT [ "/entrypoint.sh" ]
