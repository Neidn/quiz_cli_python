tests: ## Run the unit tests
	$(info Running tests...)
	nosetests -vv --with-spec --spec-color --with-coverage --cover-package=service

run: ## Run the service
	$(info Starting service...)
	python3 main.py

.PHONY: tests run
