.PHONY: install test lint typecheck demo verify

install:
	python -m pip install -e ".[dev]"

test:
	python -m unittest discover -s tests -v

lint:
	ruff check .

typecheck:
	mypy src/ai_api_playbook

demo:
	python -m ai_api_playbook.cli demo

verify: test lint typecheck
