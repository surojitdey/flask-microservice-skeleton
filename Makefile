.PHONY: install test run lint generate-spec validate-spec

install:
	@pip install -r requirements.txt
	@pip install -r requirements_dev.txt

test:
	@tox

run:
	@PYTHONPATH=. python app/main.py

lint:
	@tox -e lint

generate-spec:
	@PYTHONPATH=. python app/openapi.py

validate-spec: generate-spec
	@tox -e validate-spec
