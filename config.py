# WARNING: This is a dummy key for security testing purposes
AWS_SECRET_ACCESS_KEY = "AKIAIMORIJ7DHEXAMPLE"
SENDGRID_API_KEY = "SG.xYz1234567890abcdefGHIJKL.mNoPqRsTuVwXyZ"

import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route("/user")
def get_user():
    user_id = request.args.get("id")
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    # INSECURE: Directly using user input in a query string (SQL Injection)
    query = "SELECT * FROM users WHERE id = '" + user_id + "'"
    cursor.execute(query)
    
    return cursor.fetchone()
