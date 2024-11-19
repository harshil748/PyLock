from flask import Flask, request, render_template, jsonify, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from cryptography.fernet import Fernet
import pyotp
from password_strength import PasswordPolicy

app = Flask(__name__)
app.secret_key = 'supersecretkey'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

policy = PasswordPolicy.from_names(
    length=8,
    uppercase=1,
    numbers=1,
    special=1
)

class User(UserMixin):
    def __init__(self, id):
        self.id = id

users = {'admin': {'password': 'admin'}}

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

def generate_key():
    return Fernet.generate_key()

def encrypt_password(key, password):
    f = Fernet(key)
    return f.encrypt(password.encode()).decode()

def decrypt_password(key, encrypted_password):
    f = Fernet(key)
    return f.decrypt(encrypted_password.encode()).decode()

passwords = {}
key = generate_key()

@app.route("/")
@login_required
def index():
    return render_template("index.html")

@app.route('/totp')
@login_required
def totp():
    return render_template('totp.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users and users[username]["password"] == password:
            user = User(username)
            login_user(user)
            return redirect(url_for("index"))
        else:
            return "Invalid credentials"
    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route("/add_password", methods=["POST"])
@login_required
def add_password():
    service = request.form["service"]
    username = request.form["username"]
    password = request.form["password"]
    if service and username and password:
        if policy.test(password):
            return jsonify({"message": "Password does not meet strength requirements."}), 400
        encrypted_password = encrypt_password(key, password)
        passwords[service] = {"username": username, "password": encrypted_password, "category": request.form.get("category", ""), "tags": request.form.get("tags", "").split(",")}
        return jsonify({"message": "Password added successfully!"})
    else:
        return jsonify({"message": "Please fill in all the fields."}), 400

@app.route("/get_password", methods=["POST"])
@login_required
def get_password():
    service = request.form["service"]
    if service in passwords:
        encrypted_password = passwords[service]["password"]
        decrypted_password = decrypt_password(key, encrypted_password)
        return jsonify(
            {"username": passwords[service]["username"], "password": decrypted_password, "category": passwords[service]["category"], "tags": passwords[service]["tags"]}
        )
    else:
        return jsonify({"message": "Password not found."}), 404

@app.route("/generate_totp", methods=["POST"])
@login_required
def generate_totp():
    service = request.form["service"]
    if service:
        secret = pyotp.random_base32()
        totp = pyotp.TOTP(secret)
        current_totp = totp.now()
        return jsonify({"totp": current_totp})
    else:
        return jsonify({"message": "Please provide a service name."}), 400

if __name__ == "__main__":
    app.run(debug=True)
