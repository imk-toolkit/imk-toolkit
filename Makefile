build: check-dependencies
	@echo "===================================================================="
	@echo "Build Python packages"
	@echo "===================================================================="
	@python3 -m build

install:
	@echo "===================================================================="
	@echo "Install built Python packages"
	@echo "===================================================================="
	@python3 -m pip install $(shell ls dist/*.whl)

container:
	@echo "===================================================================="
	@echo "Build Docker Container"
	@echo "===================================================================="
	@docker build --tag imktk/imktk .

bash:
	@echo "===================================================================="
	@echo "Start container and bash"
	@echo "===================================================================="
	@docker run --rm -it -v $(shell pwd)/imktk:/home/python/imktk imktk/imktk bash

check:
	@while inotifywait -q -e modify -e create -e delete -e move --recursive /home/python/ ; do \
		clear; \
		echo "===================================================================="; \
		echo "Check & correct format via black"; \
		echo "===================================================================="; \
		black --check /home/python/imktk; \
		echo ""; \
		echo ""; \
		echo "===================================================================="; \
		echo "Formatting and linting"; \
		echo "===================================================================="; \
		flake8 /home/python/imktk; \
	done

watch: container
	@echo "===================================================================="
	@echo "Starting watch environment in docker container"
	@echo "===================================================================="
	@docker run --pull never --workdir /home/python --rm -it -v $(shell pwd)/imktk:/home/python/imktk imktk/imktk make check

black:
	@echo "===================================================================="
	@echo "Check code format via black"
	@echo "===================================================================="
	@docker run --pull never --rm -it -v $(shell pwd)/imktk:/home/python/imktk imktk/imktk poetry run black .

flake8:
	@echo "===================================================================="
	@echo "Check code linting via flake8 (deprecated; please use `make watch`)"
	@echo "===================================================================="
	@docker run --pull never --rm -it -v $(shell pwd)/imktk:/home/python/imktk imktk/imktk poetry run flake8

.PHONY: build bash black check check-dependencies flake8 fmt format install lint watch

lint: flake8
format: black
fmt: black
check-dependencies:
	@echo "===================================================================="
	@echo "Check all dependencies for build"
	@echo "===================================================================="
	@python3 -c "import build" \
		|| (echo "DependencyError: Please install 'build' module using 'python3 -m pip install build'" && exit 1)
