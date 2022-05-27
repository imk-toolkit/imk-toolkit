# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Template files for scripts e.g. [Dataarrays](/imktk/dataarray_methods/_template.py).
- Watch ability for [Makefile](/Makefile).
- Dataarray method for [vapour pressure over liquid water](/imktk/dataarray_methods/vapour_pres_liq.py).
- Dataarray method for [vapour pressure over ice](/imktk/dataarray_methods/vapour_pres_ice.py).
- Dataarray method for [climatology](/imktk/dataarray_methods/climatology.py).
- Tutorial submodule for [example data](/imktk/tutorial.py).

## [0.1.8] - 2022-03-14

### Added

- Documentation to internal structure.
- Makefile for better handling of docker container.
- Contributing.md documentation.
- [DataArray] script for calculation of number density `num_den`.
- `lint` method in Makefile.
- Support for changing logging setting via `IMKTK_LOGLEVEL` environment variable.
- Support dataarray script paths using `IMKTK_DATAARRAY` environment variable.
- Support dataset script paths using `IMKTK_DATASET` environment variable.
- Labels `latest` and `testing` to docker images on dockerhub.
- Support for aliases `format` and `fmt` for `black` execution in Makefile.
- CI/CD workflows for `windows` and `macOS`.

### Removed

- Docker-compose setup.

### Fixed

- Makefile execution if default `build` module was installed.

## [0.1.7] - 2022-01-14

### Changed

- Internal naming of elements.

## [0.1.6] - 2022-01-13

### Added

- Version output for `imktk`.
- Printing of available scripts.
- Build information for supporting `python -m build`.
- Proper logging information.

### Changed

- Docker image and file size.
- Source release file size.

### Fixed

- Loading of scripts without environment variable.

## [0.1.5] - 2022-01-11

### Added

- Changelog.md to repository.
