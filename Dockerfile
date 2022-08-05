FROM ubuntu:22.04

ENV LANG="C.UTF-8" \
    LC_ALL="C.UTF-8" \
    PATH="/home/python/.poetry/bin:/home/python/.local/bin:$PATH" \
    PIP_NO_CACHE_DIR="false" \
    POETRY_VERSION="1.1.12"

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    inotify-tools \
    make \
    python-is-python3 \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd --gid 1000 python && \
    useradd  --uid 1000 --gid python --shell /bin/bash --create-home python

USER 1000
RUN mkdir /home/python/imktk
WORKDIR /home/python/imktk

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/ecb030e1f0b7c13cc11971f00ee5012e82a892bc/get-poetry.py | python
RUN poetry config virtualenvs.create false

COPY --chown=python:python . /home/python/
RUN poetry install --no-interaction --no-ansi

CMD ["imktk"]
