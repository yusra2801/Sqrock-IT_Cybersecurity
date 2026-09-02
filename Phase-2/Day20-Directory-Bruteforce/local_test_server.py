from flask import Flask, abort

app = Flask(__name__)


@app.route("/")
def home():
    return "Day 20 local test server running."


@app.route("/admin")
def admin():
    return "Admin panel (should not be public!)"


@app.route("/dashboard")
def dashboard():
    abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)