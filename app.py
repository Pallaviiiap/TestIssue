from flask import Flask, render_template, request

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

    username = request.form.get("username").strip()
    password = request.form.get("password")

    # FIX: check if username exists
    if username in users and users[username] == password:
        message = "Login Successful"
    else:
        message = "Invalid username or password"

    return render_template("result.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)
