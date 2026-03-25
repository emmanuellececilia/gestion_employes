from database import get_connection

def get_user_by_username(username):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM users WHERE username = %s",
        (username,)
    )

    user = cur.fetchone()

    cur.close()
    conn.close()

    return user