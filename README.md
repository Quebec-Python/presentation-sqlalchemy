# Présentation de SQLAlchemy

## Installation des dépendances de la présentation

    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt


### Générer les slides

    $ fab gen

### Démarrer la démo de la présentation

    $ fab demo

## Présentation de SQLAlchemy avec une base de données SQlite

### Établir une connexion à une base de données

### Obtenir des données

### Ajouter/Modifier/Supprimer des données

## Cas d'utilisation

### Lire des fichiers CSV datés et insérer chaque ligne dans la base de données

    $ cd src
    $ python csv_to_db_example.py

