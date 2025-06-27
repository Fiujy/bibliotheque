# Variables
VENV_DIR = venv
PYTHON = $(VENV_DIR)/bin/python
PIP = $(VENV_DIR)/bin/pip
PYTEST = $(VENV_DIR)/bin/pytest

# Cible pour créer l'environnement virtuel
venv:
	python3 -m venv $(VENV_DIR)
	$(PIP) install --upgrade pip

# Cible pour installer les dépendances
install: venv
	$(PIP) install -r requirements.txt

# Cible pour lancer les tests
test:
	PYTHONPATH=src $(PYTEST)

# Cible pour la couverture
coverage:
	PYTHONPATH=src $(PYTEST) --cov=src/bibliotheque --cov-report=html --cov-report=term-missing

# Cible pour nettoyer
clean:
	rm -rf htmlcov/ .coverage .pytest_cache/ __pycache__/ */__pycache__/ */*/__pycache__/

# Cible pour nettoyer complètement (avec venv)
clean-all: clean
	rm -rf $(VENV_DIR)

# Cible pour tout installer et tester
all: install test coverage

# Cible pour activer l'environnement virtuel (info)
activate:
	@echo "Pour activer l'environnement virtuel, utilisez :"
	@echo "source $(VENV_DIR)/bin/activate"

.PHONY: venv install test coverage clean clean-all all activate