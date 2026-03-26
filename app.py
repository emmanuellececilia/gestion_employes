from flask import Flask
from flask_login import LoginManager
from auth_controller import auth_bp
from employe_controller import employe_bp
from user import User
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"

# 🔐 Login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"

# 🔥 utilisateur temporaire
users = {
    "1": User("1", "admin", "1234")
}

# 🔥 charger utilisateur
@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)

# 🔥 routes
app.register_blueprint(employe_bp)
app.register_blueprint(auth_bp)

# 🚀 lancement
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )