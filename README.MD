# Projet NSI — Blog Web avec Flask

## Présentation

Dans le cadre du projet de NSI, nous avons réalisé un petit site de blog en utilisant Python avec Flask.

Le principe est simple : un utilisateur peut écrire un article via un formulaire, puis le retrouver sur la page du blog avec les autres publications déjà enregistrées.

Le but était de manipuler plusieurs notions vues en cours :
- les routes Flask
- les formulaires HTML
- le stockage de données en JSON
- le CSS pour le style
- un peu de JavaScript pour l’interaction
- GitHub pour le suivi du projet

---

## Fonctionnalités

Le site contient actuellement :

### Page d’accueil
Une page avec un formulaire permettant de :
- entrer un titre
- indquer l’auteur
- écrire le contenu de l’article

### Page blog
Une page qui affiche :
- tous les articles enregistrés
- le nombre total d’articles
- un bouton pour ajouter un nouvel article
- la possibilité de supprimer un article

### JavaScript
Deux petites fonctionnalités ont été ajoutées :
- affichage automatique du nombre d’articles
- confirmation avant suppression d’un article

---

## Technologies utilisées

- Python
- Flask
- HTML
- CSS
- JavaScript
- JSON
- Git / GitHub

---

## Structure du projet

```bash
blogv3.3/
│
├── app.py
├── journaldebord.txt
│
├── static/
│   ├── articles.json
│   ├── script.js
│   ├── styleBlog.css
│   └── styleFormulaire.css
│
└── templates/
    ├── blog.html
    └── formulaire.html
