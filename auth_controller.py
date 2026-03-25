from flask import Blueprint, render_template, request, redirect, url_for, session
from auth_use_case import login_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = login_user(username, password)

        if user:
            session["user"] = user[1]  # username
            return redirect(url_for("employe.liste"))
        else:
            return "Identifiants incorrects"

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("auth.login"))