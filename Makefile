test:
	python -m unittest

lint:
	@echo
	isort --diff -c .
	@echo
	blue --check --diff --color . 
	@echo
	flake8 .
	@echo
	mypy .
	@echo
	bandit -r Underfoot/
	@echo
	pip-audit --ignore-vuln GHSA-w596-4wvx-j9j6

format:
	isort .
	blue .
	pyupgrade --py310-plus **/*.py

install_hooks:
	scripts/install_hooks.sh
