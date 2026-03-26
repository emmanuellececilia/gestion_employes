from auth_repository import get_user_by_username
import bcrypt

def login_user(username, password):

    user = get_user_by_username(username)

    if not user:
        return None

    # user = (id, username, password_hash)

    if bcrypt.checkpw(password.encode(), user[2].encode()):
        return user

    return None

def login_user(username, password):

    user = get_user_by_username(username)

    if not user:
        return None

    if bcrypt.checkpw(password.encode(), user["password"].encode()):
        return user

    return None

def create_user(username, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    # stocker hashed.decode()

