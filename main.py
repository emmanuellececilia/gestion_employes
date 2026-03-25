# On importe la fonction qui crée la table
from database import creer_table

# On importe les fonctions de gestion
from employe_repository import add_employe, get_all_employes,update_employe,delete_employe

# On importe la classe Employe
from employe import Employe


# On appelle la fonction pour créer la table si nécessaire
creer_table()


# Fonction qui affiche le menu principal
def menu():

    # Boucle infinie pour garder le programme actif
    while True:

        # Affichage du menu
        print("\n===== Gestion des employés =====")

        print("1 Ajouter un employé")
        print("2 Lister les employés")
        print("3 Modifier un employé")
        print("4 Supprimer un employé")
        print("0 Quitter")


        # Lecture du choix utilisateur
        choix = input("Votre choix : ")


        # Si l'utilisateur veut ajouter un employé
        if choix == "1":

            # Demande du nom
            nom = input("Nom : ")

            # Demande du prénom
            prenom = input("Prenom : ")

            # Demande du poste
            poste = input("Poste : ")

            # Demande du salaire
            salaire = int(input("Salaire : "))

            # Création d'un objet Employe
            emp = Employe(nom, prenom, poste, salaire)

            # Appel de la fonction d'ajout
            add_employe(emp)


        # Si l'utilisateur veut afficher les employés
        elif choix == "2":

            # Appel de la fonction de récupération
            employes = get_all_employes()

            # Parcours de la liste
            for emp in employes:

                # Affichage de chaque ligne
                print(emp)

        elif choix == "2":

            # Appel de la fonction de récupération
            employes = get_all_employes()

            # Parcours de la liste
            for emp in employes:
                emp.afficher()

        elif choix == "3":

            id_emp = int(input("ID de l'employé à modifier : "))
            nom = input("Nouveau nom : ")
            prenom = input("Nouveau prénom : ")
            poste = input("Nouveau poste : ")
            salaire = float(input("Nouveau salaire : "))

            emp = Employe(nom, prenom, poste, salaire, id_emp)

            update_employe(emp)

        elif choix == "4":

            id_emp = int(input("ID de l'employé à supprimer : "))

            delete_employe(id_emp)

        # Si l'utilisateur veut quitter
        elif choix == "0":

            print("Au revoir")

            # Sortie de la boucle
            break


# Lancement du menu
menu()