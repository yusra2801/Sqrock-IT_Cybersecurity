
from flask import Flask, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Fake correct credentials for this test lab
Correct_username = ("admin")
Correct_password = ("sqrock123")

app = Flask(__name__)
limiter = Limiter(get_remote_address, app=app, default_limits=["5 per minute"])

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if username == Correct_username and password == Correct_password:
        return "Login successful!", 200
    else:
        return "Invalid credentials.", 401

if __name__ == "__main__":
    app.run(port=5000)
