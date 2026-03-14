from flask import Flask, render_template, request, redirect, url_for, session
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

users = {
    "admin": "1234",
    "user": "abcd"
}

@app.route("/", methods=["GET"])
def home():
    session['csrf_token'] = secrets.token_hex(16)
    return render_template("index.html", csrf_token=session['csrf_token'])

@app.route("/login", methods=["POST"])
def login():
    if request.form.get('csrf_token') != session.get('csrf_token'):
        return render_template("result.html", message="Invalid CSRF token")
        
    username = request.form.get("username")
    password = request.form.get("password")

    if username not in users:
        return render_template("result.html", message="Username not found")
    elif users[username] != password:
        return render_template("result.html", message="Invalid password")
    else:
        return render_template("result.html", message="Login Successful")


if __name__ == "__main__":
    app.run(debug=True)