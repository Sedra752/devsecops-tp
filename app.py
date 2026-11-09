from flask import Flask, request
import re
import sqlite3
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello DevSecOps!"

@app.route("/user")
def user():
    name = request.args.get("name", "")
    conn = sqlite3.connect("users.db")
    rows = conn.execute("SELECT * FROM users WHERE name = ?", (name,)).fetchall()
    return str(rows)

@app.route("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9.-]*", host):
        return "Invalid host", 400
    result = subprocess.run(["ping", "-c", "1", host], capture_output=True, text=True)
    return result.stdout

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
