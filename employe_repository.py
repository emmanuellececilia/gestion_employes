# On importe la fonction de connexion à la base
from database import get_connection

# On importe la classe Employe
from employe import Employe


# Fonction qui ajoute un employé dans la base
def add_employe(emp: Employe):

    # Ouverture de la connexion à la base
    conn = get_connection()

    # Création du curseur pour exécuter du SQL
    cur = conn.cursor()

    # Requête SQL pour insérer un employé
    cur.execute(

        # La requête SQL
        """INSERT INTO employes(nom, prenom, poste, salaire)
            VALUES (%s,%s,%s,%s)
        """,

        # Les valeurs envoyées à la requête
        (emp.nom, emp.prenom, emp.poste, emp.salaire)
    )

    # Validation de la transaction
    conn.commit()

    # Fermeture du curseur
    cur.close()

    # Fermeture de la connexion
    conn.close()

    # Message pour l'utilisateur
    print("Employé ajouté avec succès")


# Fonction pour récupérer tous les employés
def get_all_employes():

    # Connexion à la base
    conn = get_connection()

    # Création du curseur
    cur = conn.cursor()

    # Requête SQL pour récupérer tous les employés
    cur.execute("SELECT * FROM employes")

    # On récupère toutes les lignes retournées par la requête
    rows = cur.fetchall()

    # Fermeture du curseur
    cur.close()

    # Fermeture de la connexion
    conn.close()

    # On retourne les résultats
    return rows

#Modification de la fonction liste_employe afin d'utiliser le fonction Afficher de la classe Employe dans le main
def liste_employes():

    # Connexion à la base
    conn = get_connection()

    # Création du curseur
    cur = conn.cursor()

    # Requête SQL pour récupérer tous les employés
    cur.execute("SELECT * FROM employes")

    # On récupère toutes les lignes retournées par la requête
    rows = cur.fetchall()

    #création de la liste employe
    employes = []

    #on parcourt les lignes retournées par la requete
    for row in rows:

        #On attribut chaque valeur de la ligne au parametre qui lui correspond
        emp = Employe(
            nom=row[1],
            prenom=row[2],
            poste=row[3],
            salaire=row[4],
            id=row[0]
        )

        #On ajoute l'employe à la liste
        employes.append(emp)

    # Fermeture du curseur
    cur.close()

    # Fermeture de la connexion
    conn.close()

    return employes


#Fonction qui modifie un employe
def update_employe(emp: Employe):

    #connexion à la base de données
    conn=get_connection()

    #Creation du curseur
    cur=conn.cursor()

    #Requete SQL
    cur.execute("""
                    UPDATE employes set nom=%s,prenom=%s, poste=%s,
                    salaire=%s where id=%s
                """,
                # Les valeurs envoyées à la requête
                (emp.nom,emp.prenom, emp.poste,emp.salaire,emp.id))

    # Validation de la transaction
    conn.commit()

    #fermeture du curseur
    cur.close()

    #fermeture de la connexion
    conn.close()

    #message
    print("l'employé modifié avec succès")

    # Fonction qui supprime un employe
def delete_employe(id):
    # connexion à la base de données
    conn = get_connection()

    # Creation du curseur
    cur = conn.cursor()

    # Requete SQL
    cur.execute(
                 "delete from employes where id=%s",

        # Les valeurs envoyées à la requête
                (id,))

    # Validation de la transaction
    conn.commit()

    # fermeture du curseur
    cur.close()

    # fermeture de la connexion
    conn.close()

    # Message utilisateur
    print("Employé supprimé avec succès")

def seach_employe_by_world(mot: str):
    # Ouverture de la connexion
    conn = get_connection()

    # Création du cursor
    cur = conn.cursor()

    # Execution de la requête
    cur.execute(
        # La requete
        """SELECT * FROM employes as emp
            WHERE emp.nom like %s
            or emp.prenom like %s
        """,

        # Valeurs renvoyées à la requête
        ('%' + mot + '%', '%' + mot + '%')
    )

    # Récuperation des valeurs retournées
    rows = cur.fetchall()

    # fermeture du cursor
    cur.close()

    # fermeture de la connexion
    conn.close()

    # listre retourné
    return rows

def get_employe_by_id(id):
    # Ouverture de la connexion
    conn = get_connection()

    # Création du cursor
    cur = conn.cursor()

    # Execution de la requête
    cur.execute(
        # La requete
        """SELECT * FROM employes as emp
            WHERE emp.id  = %s
        """,

        # Valeurs renvoyées à la requête
        (id,)
    )

    # Récuperation des valeurs retournées
    rows = cur.fetchone()

    # fermeture du cursor
    cur.close()

    # fermeture de la connexion
    conn.close()

    # listre retourné
    return rows