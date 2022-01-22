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

.PHONY: build bash black flake8
