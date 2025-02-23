Ce projet a été créé par Anthony et Ewen, il restitue les informations de la base de données Steam_Like.db dans une bibliothèque que l'on peut trier et au travers d'une recherche par nom.
Le site propose également un accueil (http://127.0.0.1:5000/) pour faciliter la navigation entre les pages.
Chaque jeu affiché est cliquable et fait découvrir les informations relatives à celui-ci. Il est possible d'ajouter ou de supprimer des jeux.

Liste des tâches effectuées par Anthony (frontend):
- La mise en forme du site internet (CSS)
- L'implémentation de l'affichage des images pour chaque jeu
- La fusion des deux projets en un seul plus massif
- Création de la base de donnée
- Travail sur la structure de la base de donnée
- Commentaires

Liste des tâches effectuées par Ewen (backend):
- Implémentation des fonctionnalités relatives à la base de donnée (Recherche, Bibliothèque, Info-Jeux, ajout et suppression de jeux)
- Développement de la structure des pages HTML et de la connexion au serveur avec python
- Travail sur la structure de la base de donnée
- Commentaires


Il est possible de trouver le fichier python qui fait tourner le serveur dans le dossier TP_bdd_jeux, il s'appelle main.py.
Le fichier bdd.py contient les fonctions python interagissant avec la base de donnée avec des commandes SQL. Toutes les images sont stockées dans le dossier images.
La feuille de style est dans le dossier static et le HTML dans templates.
Dans templates, le fichier ajouter.html propose le formulaire pour ajouter un jeu, info-jeu.html donne les informations précises par rapport au jeu, recherche.html permet de rechercher un jeu dans la base de données, supprimer.html
affiche la liste des jeux que l'on peut trier et une fonctionnalité pour supprimer chaque jeu ( il faut recharger la page pour voir la modification s'opérer ) et index.html est le menu.
