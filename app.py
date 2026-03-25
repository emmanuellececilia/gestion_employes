from flask import Flask, request, render_template, redirect, url_for
from flask_login import login_user, login_required, logout_user,LoginManager
from auth_controller import auth_bp
from employe_controller import employe_bp
from user import User  # 🔥 on va créer ce fichier
import os

app = Flask(__name__)

# 🔐 obligatoire pour session
app.secret_key = "supersecretkey"

# 🔥 Enregistrer le controller
app.register_blueprint(employe_bp)
app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )

# 🔐 Configuration login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "employe.login"  # IMPORTANT avec blueprint

# 🔥 Charger utilisateur
@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)

# 🔥 utilisateur temporaire
users = {
    "1": User("1", "admin", "1234")
}
