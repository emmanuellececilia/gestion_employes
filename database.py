# On importe la bibliothèque psycopg qui permet à Python de se connecter à PostgreSQL
import psycopg2


# Cette fonction sert à créer une connexion avec la base de données
def get_connection():
    try:
        # On crée une connexion en utilisant psycopg.connect()
        # On indique les informations nécessaires pour accéder à la base
        conn = psycopg2.connect(

            # Adresse du serveur PostgreSQL (localhost signifie : la base est sur notre ordinateur)
            host="localhost",

            # Nom de la base de données à laquelle on veut se connecter
            dbname="entreprise_db",

            # Nom de l'utilisateur PostgreSQL
            user="postgres",

            # Mot de passe de l'utilisateur PostgreSQL
            password="emma",

            # Port utilisé par PostgreSQL (5432 est le port par défaut)
            port="5432"
        )

        # La fonction retourne la connexion pour qu'elle puisse être utilisée ailleurs dans le programme
        return conn

    except Exception as e:
        print("Erreur de connexion :", e)
        return None

# Cette fonction permet de créer la table des employés si elle n'existe pas déjà
def creer_table():

    # On ouvre une connexion à la base de données
    conn = get_connection()

    # On crée un curseur qui permettra d'exécuter des commandes SQL
    cur = conn.cursor()

    # On exécute une requête SQL pour créer la table "employes"
    cur.execute("""
        CREATE TABLE IF NOT EXISTS employes(

            -- id est la clé primaire
            id SERIAL PRIMARY KEY,

            -- nom de l'employé
            nom VARCHAR(50),

            -- prénom de l'employé
            prenom VARCHAR(50),

            -- poste occupé dans l'entreprise
            poste VARCHAR(50),

            -- salaire de l'employé
            salaire NUMERIC
        )
    """)

    # On valide les modifications dans la base de données
    conn.commit()

    # On ferme le curseur
    cur.close()

    # On ferme la connexion à la base
    conn.close()