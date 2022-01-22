# Contributing to `imktk`

## Interactive Development Environment

It is highly recommended to use the provided [Makefile](/Makefile) for creating
a reproducible development environment.

1. First create the docker container using `make build`.
2. Start and enter the container using `make bash`.

This setup mounts the current [`imktk`](/imktk) folder into the docker environment.
Therefore all changes in the codebase are reflected in the container. This
allows for an interactive development environment.

## Check Code Style Offline

The module uses (`black`)[https://black.readthedocs.io/en/stable/] and
[`flake8`](https://flake8.pycqa.org/en/latest/) for code styling. Checks are
executed when opening a PR to `master`. The styling of code can be checked
offline using the following commands from the [Makefile](/Makefile).

- Check `black` formatting via `make black`
- Check `flake8` lints via `make flake8`
