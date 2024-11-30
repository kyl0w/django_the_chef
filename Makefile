# Variables
PYTHON = python
DJANGO_PROJECT_DIR = django_project
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

# Help
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
	@echo "  lint             - Run linter (flake8) to check code style."
	@echo "  format           - Format code with black."
	@echo "  help             - Show this help message."
