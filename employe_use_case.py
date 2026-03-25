#Importation des dépendances
from employe import Employe
from employe_repository import (
    add_employe,
    get_all_employes,
    update_employe,
    delete_employe,
    get_employe_by_id
)

#Créer un employe
def creer_employe(nom, prenom, poste, salaire):
    # 🔐 Validation métier
    if not nom or not prenom:
        raise ValueError("Nom et prénom obligatoires")

    if salaire <= 0:
        raise ValueError("Salaire invalide")

    # 🧠 Création objet métier
    employe = Employe(nom, prenom, poste, salaire)

    # 💾 Sauvegarde en base
    add_employe(employe)

    return employe

#lister les employes
def lister_employes():
    rows = get_all_employes()

    employes = []

    for row in rows:
        emp = Employe(
            id=row[0],
            nom=row[1],
            prenom=row[2],
            poste=row[3],
            salaire=row[4]
        )
        employes.append(emp)

    return employes

#Modifier un employe
def modifier_employe(id, nom, prenom, poste, salaire):

    # 🔍 Vérifier existence
    row = get_employe_by_id(id)

    if not row:
        raise ValueError("Employé introuvable")

    # 🔐 Validation
    if salaire <= 0:
        raise ValueError("Salaire invalide")

    # 🧠 Mise à jour objet
    employe = Employe(
            id=id,
            nom=nom,
            prenom=prenom,
            poste=poste,
            salaire=salaire
    )

    # 💾 Update DB
    update_employe(employe)

    return employe

#Supprimer un employe
def supprimer_employe(id):

    emp = get_employe_by_id(id)

    if not emp:
        raise ValueError("Employé introuvable")

    delete_employe(id)

    return True

#Trouver un employe
def trouver_employe(id):
    row = get_employe_by_id(id)

    if not row:
        return None

    return Employe(
        id=row[0],
        nom=row[1],
        prenom=row[2],
        poste=row[3],
        salaire=row[4]
    )