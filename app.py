from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

FICHIER = "static/articles.json"

def lire_articles():
    if os.path.exists(FICHIER):
        with open(FICHIER, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def sauvegarder(articles):
    with open(FICHIER, "w", encoding="utf-8") as f:
        json.dump(articles, f, indent=4, ensure_ascii=False)

# Page d'accueil : le formulaire
@app.route("/")
def accueil():
    return render_template("formulaire.html")

# Traitement du formulaire
@app.route("/ajouter", methods=["POST"])
def ajouter():
    titre = request.form["titre"]
    auteur = request.form["auteur"]
    contenu = request.form["contenu"]

    articles = lire_articles()
    articles.append({"titre": titre, "auteur": auteur, "contenu": contenu})
    sauvegarder(articles)

    return redirect("/blog")

# Page du blog : la liste des articles
@app.route("/blog")
def blog():
    articles = lire_articles()
    return render_template("blog.html", articles=articles)

# Supprimer un article
@app.route("/supprimer/<int:numero>")
def supprimer(numero):
    articles = lire_articles()
    articles.pop(numero)
    sauvegarder(articles)
    return redirect("/blog")

if __name__ == "__main__":
    app.run(debug=True)
