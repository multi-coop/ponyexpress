---
title: Premier lancement
description: Tutorial pour faire tourner l'outil localement
---

Dans ce tutoriel, nous allons lancer PonyExpress localement pour la première fois.

## Installer les outils nécessaires

Si vous utilisez nix, renommez simplement le fichier `_shell.nix` en `shell.nix` et lancez la commande `nix-shell --pure`

Sinon, installez : 
- python,
- [poetry](https://python-poetry.org/docs/#installation)
- [typst](https://github.com/typst/typst?tab=readme-ov-file#installation) 

Puis executez le code suivant :
```sh
git clone git@gitlab.com:multi-coop/pony_express.git
cd pony_express
poetry install

```

## Autoriser l'acces a l'API grist

Vous avez besoin d'un API Key pour utiliser l'API de Grist.

Cette clef est propre a votre compte utilisateur. 

Vous pouvez la recuperer en cliquant sur votre icone utilisateur => parametre du compte => section API => clef d'API 
Une fois copie ajoutez la comme variable d'environnement (ou dans votre shell.nix le cas echeant)

```sh
 export GRIST_API_KEY="API KEY disponible via votre compte GRIST"
```

## Lancer l'exemple

L'exemple propose recupere les donnees de ce [tableau public](https://docs.getgrist.com/uJrM5M5P5Z4Q/ponyexpressexemple) et genere un pdf selon le template `templates/exemple/birthday_template.typ`

```sh
 poetry run python src/pony_express/exemple.py
```

Le PDF genere sera cree dans le dossier generated

## Creer votre propre pdf 

See [Create your own PDF](/tutorial/2_create_your_pdf)