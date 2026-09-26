"""Notes app: hashed passwords, CSRF field, parameterized SQL. 127.0.0.1:5002."""

from __future__ import annotations

import secrets
import sqlite3
from pathlib import Path

from flask import Flask, redirect, render_template_string, request, session
from werkzeug.security import check_password_hash, generate_password_hash

ROOT = Path(__file__).resolve().parent
DB = ROOT / "notes.db"
app = Flask(__name__)
app.secret_key = "dev-only-change-me"

PAGE = """
<!doctype html>
<title>Notes</title>
<h1>Notes for {{ user }}</h1>
<ul>
{% for note in notes %}
  <li>{{ note }}</li>
{% endfor %}
</ul>
<form method="post" action="/notes">
  <input type="hidden" name="csrf" value="{{ csrf }}">
  <input name="body" required>
  <button>Save</button>
</form>
"""

LOGIN = """
<!doctype html>
<title>Login</title>
<p>{{ error }}</p>
<form method="post">
  <input name="username" placeholder="username">
  <input name="password" type="password" placeholder="password">
  <button>Sign in</button>
</form>
"""


def connect() -> sqlite3.Connection:
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with connect() as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password_hash TEXT)")
        conn.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, owner TEXT, body TEXT)")
        row = conn.execute("SELECT username FROM users WHERE username = ?", ("demo",)).fetchone()
        if row is None:
            conn.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                ("demo", generate_password_hash("demo-pass-123")),
            )


init_db()


@app.get("/login")
def login_form():
    return render_template_string(LOGIN, error="")


@app.post("/login")
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")
    with connect() as conn:
        row = conn.execute("SELECT password_hash FROM users WHERE username = ?", (username,)).fetchone()
    if row is None or not check_password_hash(row["password_hash"], password):
        return render_template_string(LOGIN, error="Unknown user or password."), 401
    session["user"] = username
    session["csrf"] = secrets.token_hex(16)
    return redirect("/notes")


@app.get("/notes")
def notes():
    user = session.get("user")
    if not user:
        return redirect("/login")
    session.setdefault("csrf", secrets.token_hex(16))
    with connect() as conn:
        rows = conn.execute("SELECT body FROM notes WHERE owner = ? ORDER BY id", (user,)).fetchall()
    return render_template_string(PAGE, user=user, notes=[row["body"] for row in rows], csrf=session["csrf"])


@app.post("/notes")
def add_note():
    user = session.get("user")
    if not user:
        return redirect("/login")
    if not secrets.compare_digest(request.form.get("csrf", ""), session.get("csrf", "")):
        return "CSRF check failed", 400
    body = request.form.get("body", "").strip()
    if len(body) > 500:
        return "Note too long (500 characters).", 400
    if body:
        with connect() as conn:
            conn.execute("INSERT INTO notes (owner, body) VALUES (?, ?)", (user, body))
    return redirect("/notes")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5002)
