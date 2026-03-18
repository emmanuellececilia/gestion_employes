# Définition de la classe Employe
class Employe:

    # Le constructeur de la classe
    # Il est appelé automatiquement lorsqu'on crée un objet Employe
    def __init__(self, nom, prenom, poste, salaire, id=None):

        # id correspond à l'identifiant dans la base de données
        self.id = id

        # nom de famille
        self.nom = nom

        # prénom
        self.prenom = prenom

        # poste occupé dans l'entreprise
        self.poste = poste

        # salaire
        self.salaire = salaire


    # Cette méthode sert à afficher un employé proprement
    def afficher(self):

        # On affiche les informations de l'employé
        print(self.id, self.nom, self.prenom, self.poste, self.salaire)