build:
	@echo "===================================================================="
	@echo "Build Docker Container"
	@echo "===================================================================="
	@docker build --tag imktk/imktk .

bash:
	@echo "===================================================================="
	@echo "Start container and bash"
	@echo "===================================================================="
	@docker run -it -v $(shell pwd)/imktk:/home/python/imktk imktk/imktk bash

package:
	@echo "===================================================================="
	@echo "Generate Python packages"
	@echo "===================================================================="
	@python3 -m build

install: package
	@echo "===================================================================="
	@echo "Install generated Python packages"
	@echo "===================================================================="
	@python3 -m pip install $(shell ls dist/*.whl)

black:
	@echo "===================================================================="
	@echo "Check code format via black"
	@echo "===================================================================="
	@docker run -it -v $(shell pwd)/imktk:/home/python/imktk imktk/imktk poetry run black .

flake8:
	@echo "===================================================================="
	@echo "Check code linting via flake8"
	@echo "===================================================================="
	@docker run -it -v $(shell pwd)/imktk:/home/python/imktk imktk/imktk poetry run flake8

.PHONY: build bash black flake8 install package
