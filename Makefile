test:
	pytest --cov-report term-missing --cov-report html --cov-branch \
	--cov Underfoot/

lint:
	@echo
	isort --diff -c .
	@echo
	blue --check --diff --color /
	@echo
	flake8 .
	@echo
	mypy .
	@echo
	bandit -r Underfoot/
	@echo
	pip-audit

format:
	isort .
	blue .
	pyupgrade --py310-plus **/*.py

install_hooks:
	scripts/install_hooks.sh
