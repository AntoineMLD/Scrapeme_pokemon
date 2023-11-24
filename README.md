Projet Scrapy - Extraction de Données Pokémon

Description

Ce projet Scrapy a pour objectif d'extraire des données liées aux Pokémon à partir du site web spécifié. Il collecte des informations telles que le nom du Pokémon, son prix, sa description, les informations de stock, les tags associés, etc.

Dépendances

    Python 3.x
    Scrapy
    SQLite (pour la sauvegarde des données)

Utilisation

    Exécuter le Spider : scrapy crawl pokemon
    Vérifier les Données : Les données extraites seront stockées dans une base de données SQLite.
    Visualisation des Données : Utilisez un outil comme DBeaver pour visualiser et interagir avec la base de données SQLite.

Structure du Projet

    spiders/: Contient les spiders utilisés pour l'extraction des données.
    pipelines.py: Fichier définissant le nettoyage des données et leur stockage dans la base de données.
    settings.py: Fichier de configuration pour le projet Scrapy.

Configuration

    Base de Données: Le fichier de configuration settings.py contient le chemin vers la base de données SQLite utilisée pour stocker les données extraites.

Contribuer

Si vous souhaitez contribuer à ce projet, veuillez suivre ces étapes :

    Ouvrir une Issue pour discuter des modifications proposées.
    Forker le projet.
    Créer une branche pour votre contribution (git checkout -b feature/Contribution)
    Committer les modifications (git commit -m 'Ajout de fonctionnalité')
    Pousser la branche (git push origin feature/Contribution)
    Créer une Pull Request.

Auteur

   Antoine MLD
