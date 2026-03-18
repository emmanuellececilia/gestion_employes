from flask import Flask, render_template, request, redirect
from gestion_employe import *
from employe import Employe

app = Flask(__name__)

# LISTE
@app.route("/")
@app.route("/employes")
def afficher():
    employes = lister_employes()
    return render_template("employes.html", employes=employes)

# AJOUT
@app.route("/ajouter", methods=["GET", "POST"])
def ajouter():
    if request.method == "POST":
        emp = Employe(
            nom=request.form["nom"],
            prenom=request.form["prenom"],
            poste=request.form["poste"],
            salaire=float(request.form["salaire"])
        )
        ajouter_employe(emp)
        return redirect("/employes")

    return render_template("ajouter.html")

# SUPPRIMER
@app.route("/supprimer/<int:id>")
def supprimer(id):
    supprimer_employe(id)
    return redirect("/employes")

# MODIFIER
@app.route("/modifier/<int:id>", methods=["GET", "POST"])
def modifier(id):

    # récupérer employé
    employes = lister_employes()
    emp = next((e for e in employes if e.id == id), None)

    if request.method == "POST":
        emp.nom = request.form["nom"]
        emp.prenom = request.form["prenom"]
        emp.poste = request.form["poste"]
        emp.salaire = float(request.form["salaire"])

        modifier_employe(emp)
        return redirect("/employes")

    return render_template("modifier.html", emp=emp)

app.run(debug=True)