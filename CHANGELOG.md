# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- Documentation to internal structure.
- Makefile for better handling of docker container.
- Contributing.md documentation.
- [DataArray] script for calculation of number density `num_den`.
- `lint` method in Makefile.
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
