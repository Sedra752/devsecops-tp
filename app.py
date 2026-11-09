from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello DevSecOps!"

@app.route("/user")
def user():
    name = request.args.get("name", "")
    conn = sqlite3.connect("users.db")
    query = "SELECT * FROM users WHERE name = '" + name + "'"
    rows = conn.execute(query).fetchall()
    return str(rows)

@app.route("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")
    return os.popen("ping -c 1 " + host).read()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
