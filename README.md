# Projet Bibliothèque

Un système de gestion de bibliothèque développé en Python avec une architecture claire et des tests automatisés.

## Installation

### Méthode 1 : Avec environnement virtuel (recommandé)
```bash
# Créer et installer
make install

# Activer l'environnement virtuel
source venv/bin/activate

# Ou voir les instructions
make activate
```

### Méthode 2 : Installation manuelle
```bash
# Créer l'environnement virtuel
python3 -m venv venv

# Activer l'environnement virtuel
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt
```

### Méthode 3 : Avec pipx (alternative)
```bash
# Installer pipx si pas déjà fait
brew install pipx

# Installer pytest globalement avec pipx
pipx install pytest
pipx install pytest-cov
```

## Tests

### Lancer tous les tests
```bash
make test
# ou
pytest
```

### Lancer des tests spécifiques
```bash
# Tests d'un module
pytest tests/test_book.py

# Test spécifique
pytest tests/test_book.py::TestBookCreation::test_create_valid_book

# Tests avec plus de détails
pytest -v
```

## Couverture

### Générer le rapport de couverture
```bash
make coverage
# ou
pytest --cov=src/bibliotheque --cov-report=html
```

Le rapport HTML sera disponible dans `htmlcov/index.html`

## Structure

```
bibliotheque_projet/
├── src/bibliotheque/     # Code source
│   ├── book.py          # Classe Book
│   ├── user.py          # Classe User
│   └── library.py       # Classe Library
├── tests/               # Tests organisés
│   ├── test_book.py     # Tests pour Book
│   ├── test_user.py     # Tests pour User
│   └── test_library.py  # Tests pour Library
├── requirements.txt     # Dépendances
├── pytest.ini         # Configuration pytest
└── Makefile           # Automatisation
```

## Fonctionnalités

- **Gestion des livres** : création, emprunt, retour
- **Gestion des utilisateurs** : création, limite d'emprunts
- **Gestion de bibliothèque** : collection, recherche, transactions
- **Tests complets** : couverture > 90%
- **Intégration continue** : GitHub Actions