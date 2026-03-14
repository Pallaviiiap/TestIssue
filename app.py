from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

users = {
    "admin": "1234",
    "user": "abcd"
}

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        flash("Both username and password fields are required")
        return redirect(url_for('home'))

    if username not in users:
        return render_template("result.html", message="Username not found")
    elif users[username] != password:
        return render_template("result.html", message="Invalid password")
    else:
        return render_template("result.html", message="Login Successful")


if __name__ == "__main__":
    app.run(debug=True)
