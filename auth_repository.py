from database import get_connection

def get_user_by_username(username):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT id, username, password FROM users WHERE username = %s",
        (username,)
    )

    row = cur.fetchone()

    cur.close()
    conn.close()

    if row:
        return {
            "id": row[0],
            "username": row[1],
            "password": row[2]
        }

    return None