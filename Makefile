# Variables
PYTHON = python
DJANGO_PROJECT_DIR = .
MANAGE = $(PYTHON) $(DJANGO_PROJECT_DIR)/manage.py

# Linter directory
LINTER_DIR = .

# Main commands
run:
	$(MANAGE) runserver

migrate:
	$(MANAGE) migrate

makemigrations:
	$(MANAGE) makemigrations

createsuperuser:
	$(MANAGE) createsuperuser

shell:
	$(MANAGE) shell

collectstatic:
	$(MANAGE) collectstatic --noinput

# Installation and environment setup
install:
	pip install -r requirements.txt

freeze:
	pip freeze > requirements.txt

# Tests and Linter
test:
	$(MANAGE) test

lint:
	flake8 --config=$(LINTER_DIR)/.flake8 $(DJANGO_PROJECT_DIR)

format:
	black $(DJANGO_PROJECT_DIR)

lint:
	flake8 .

format:
	black .

format-lint: 
	lint format

help:
	@echo "Available commands:"
	@echo "  run              - Start the development server."
	@echo "  migrate          - Apply database migrations."
	@echo "  makemigrations   - Create new migrations based on model changes."
	@echo "  createsuperuser  - Create a superuser for the system."
	@echo "  shell            - Open the Django interactive shell."
	@echo "  collectstatic    - Collect static files for production."
	@echo "  install          - Install project dependencies."
	@echo "  freeze           - Freeze the current dependencies to requirements.txt."
	@echo "  test             - Run Django tests."
	@echo "  make format          - Run Black to automatically format the code"
	@echo "  make lint            - Run Flake8 to check for style violations"
	@echo "  make format-lint - Run Black to format the code and Flake8 to check for violations"
	@echo "  help             - Show this help message."
