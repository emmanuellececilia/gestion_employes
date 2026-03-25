from flask import Blueprint, render_template, request, redirect, url_for,session
from flask_login import login_user, login_required, logout_user
from auth_data import users

# Import des use cases
from employe_use_case import (
    creer_employe,
    lister_employes,
    modifier_employe,
    trouver_employe,
    supprimer_employe
)

# Création du blueprint
employe_bp = Blueprint('employe', __name__)

#Fonction pour sécuriser les routes
def login_required():
    if "user" not in session:
        return False
    return True

# 📌 Lister les employés
@employe_bp.route("/")
#@login_required
def liste():

    if not login_required():
        return redirect(url_for("auth.login"))

    employes = lister_employes()
    return render_template("employes.html", employes=employes)


# 📌 Ajouter un employé
@employe_bp.route("/ajouter", methods=["GET", "POST"])
#@login_required
def ajouter():

    if not login_required():
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        try:
            nom = request.form["nom"]
            prenom = request.form["prenom"]
            poste = request.form["poste"]
            salaire = float(request.form["salaire"])

            creer_employe(nom, prenom, poste, salaire)

            return redirect(url_for("employe.liste"))

        except Exception as e:
            return f"Erreur : {e}"

    return render_template("ajouter.html")


# 📌 Modifier un employé
@employe_bp.route("/modifier/<int:id>", methods=["GET", "POST"])
#@login_required
def modifier(id):

    if not login_required():
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        try:
            nom = request.form["nom"]
            prenom = request.form["prenom"]
            poste = request.form["poste"]
            salaire = float(request.form["salaire"])

            modifier_employe(id, nom, prenom, poste, salaire)

            return redirect(url_for("employe.liste"))

        except Exception as e:
            return f"Erreur : {e}"

    # 🔥 On récupère les données pour pré-remplir le formulaire
    #from employe_repository import get_employe_by_id

    #emp = get_employe_by_id(id)
    emp = trouver_employe(id)

    return render_template("modifier.html", emp=emp)


# 📌 Supprimer un employé
@employe_bp.route("/supprimer/<int:id>")
#@login_required
def supprimer(id):

    if not login_required():
        return redirect(url_for("auth.login"))

    try:
        supprimer_employe(id)
        return redirect(url_for("employe.liste"))
    except Exception as e:
        return f"Erreur : {e}"