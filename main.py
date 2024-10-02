from flask import Flask, request, render_template, jsonify
from cryptography.fernet import Fernet

app = Flask(__name__)

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_password', methods=['POST'])
def add_password():
    service = request.form['service']
    username = request.form['username']
    password = request.form['password']
    if service and username and password:
        encrypted_password = encrypt_password(key, password)
        passwords[service] = {'username': username, 'password': encrypted_password}
        return jsonify({'message': 'Password added successfully!'})
    else:
        return jsonify({'message': 'Please fill in all the fields.'}), 400

@app.route('/get_password', methods=['POST'])
def get_password():
    service = request.form['service']
    if service in passwords:
        encrypted_password = passwords[service]['password']
        decrypted_password = decrypt_password(key, encrypted_password)
        return jsonify({'username': passwords[service]['username'], 'password': decrypted_password})
    else:
        return jsonify({'message': 'Password not found.'}), 404

if __name__ == '__main__':
    app.run(debug=True)
