FROM ubuntu:20.04

ENV LANG="C.UTF-8" LC_ALL="C.UTF-8" PATH="/home/python/.poetry/bin:/home/python/.local/bin:$PATH" PIP_NO_CACHE_DIR="false"

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    python3 python3-pip python3-venv python-is-python3 curl ca-certificates wait-for-it libpq-dev python3-dev build-essential gettext-base && \
    rm -rf /var/lib/apt/lists/*

RUN groupadd --gid 1000 python && \
    useradd  --uid 1000 --gid python --shell /bin/bash --create-home python

USER 1000
RUN mkdir /home/python/code
WORKDIR /home/python/code

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
RUN poetry config virtualenvs.create false

COPY --chown=python:python . /home/python/code/
RUN poetry install --no-interaction --no-ansi

CMD ["imktk"]
