from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = {
    "admin": "1234",
    "user": "abcd"
}

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username").lower()
    password = request.form.get("password")

    if username not in users:
        return render_template("result.html", message="Username not found")
    elif users[username] != password:
        return render_template("result.html", message="Invalid password")
    else:
        return render_template("result.html", message="Login Successful")


if __name__ == "__main__":
    app.run(debug=True)
