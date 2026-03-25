from auth_repository import get_user_by_username

def login_user(username, password):
    user = get_user_by_username(username)
    if not user:
        return None

    # user = (id, username, password)
    if user[2] == password:
        return user
    return None