from flask import Flask, render_template, request, url_for
from bdd import *
app = Flask(__name__)

@app.route("/")
def index():
    """Renvoie la page index.html"""
    return render_template("index.html")

@app.route("/recherche", methods=['GET', 'POST'])
def recherche():
    """Renvoie la page recherche.html après avoir récupéré les informations des jeux avec la fonction recuperer_jeux_par_nom(nom)"""
    if request.method == "POST":
        donnees = request.form
        nom = donnees.get('nom')
        liste_jeux = recuperer_jeux_par_nom(nom)
        print(liste_jeux)
    else:
        liste_jeux = None
    return render_template("recherche.html", jeux=liste_jeux)

@app.route("/info-jeu", methods=['GET'])
def info_jeux():
    """Renvoie les informations du jeu choisi par l'utilisateur sur la page info-jeu.html"""
    donnees = request.args.get("id")
    info = info_jeu(donnees)
    return render_template("info-jeu.html", id=donnees, jeux=info)

@app.route("/ajouter", methods=['GET', 'POST'])
def ajoute():
    """Affiche la page ajouter.html et récupère les valeurs du formulaire, permettant d'ajouter un jeu, quand il est envoyé"""
    if request.method == "POST":
        donnees = request.form
        titre = donnees.get('titre')
        prix = donnees.get('prix')
        statut = donnees.get('statut')
        date = donnees.get('date')
        type = donnees.get('type')
        developpeur = donnees.get('developpeur')
        ajouter(titre, prix, date, statut, type, developpeur)
    return render_template("ajouter.html")

@app.route("/supprimer", methods=['GET', 'POST'])
def supprime():
    """affiche la page supprimer.html qui est une liste de tous les jeux"""
    if request.method == "POST":
        donnees = request.form
        tri = donnees.get('tri')
        liste_jeux = chaque_jeu(tri)
        return render_template("supprimer.html", jeux=liste_jeux)
    else:
        return render_template("supprimer.html", jeux=None)

@app.route('/supprimer/jeu', methods=['POST'])
def supprimer_jeu():
    """Effectue la fonction supprimer(jeu_id) quand l'utilisateur clique sur le bouton Supprimer"""
    donnees = request.form
    tri = donnees.get('tri')
    liste_jeux = chaque_jeu(tri)
    jeu_id = request.form.get('jeu_id')
    supprimer(jeu_id)
    return render_template("supprimer.html", jeux=liste_jeux)

if __name__ == '__main__':
    app.run(debug=True)
