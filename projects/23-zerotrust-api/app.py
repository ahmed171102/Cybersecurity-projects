"""Lab API: 5-minute JWT, two roles. Listens on 127.0.0.1:5001."""

from __future__ import annotations

import os
from datetime import datetime, timedelta, timezone

import jwt
from flask import Flask, jsonify, request

app = Flask(__name__)
SECRET = os.environ.get("JWT_SECRET", "dev-only-change-me-use-32-bytes!!")
USERS = {
    "alice": {"password": "alicepass", "role": "admin"},
    "bob": {"password": "bobpass", "role": "user"},
}
# Wrong passwords per source. Five failures lock the username for this process.
FAILED_LOGINS: dict[str, int] = {}
LOCK_AFTER = 5


def current_user():
    header = request.headers.get("Authorization", "")
    if not header.startswith("Bearer "):
        return None, (jsonify({"error": "missing token"}), 401)
    token = header.split(" ", 1)[1]
    try:
        claims = jwt.decode(token, SECRET, algorithms=["HS256"])
    except jwt.PyJWTError:
        return None, (jsonify({"error": "invalid token"}), 401)
    return claims, None


def require(roles: set[str] | None = None):
    claims, error = current_user()
    if error:
        return None, error
    if roles and claims["role"] not in roles:
        return None, (jsonify({"error": "forbidden"}), 403)
    return claims, None


@app.get("/health")
def health():
    return jsonify({"ok": True, "bind": "127.0.0.1:5001"})


@app.post("/login")
def login():
    body = request.get_json(silent=True) or {}
    username = body.get("username", "")
    if FAILED_LOGINS.get(username, 0) >= LOCK_AFTER:
        return jsonify({"error": "account locked in this process after repeated failures"}), 429
    user = USERS.get(username)
    if not user or user["password"] != body.get("password"):
        FAILED_LOGINS[username] = FAILED_LOGINS.get(username, 0) + 1
        return jsonify({"error": "invalid credentials"}), 401
    FAILED_LOGINS[username] = 0
    now = datetime.now(timezone.utc)
    token = jwt.encode(
        {"sub": body["username"], "role": user["role"], "exp": now + timedelta(minutes=5)},
        SECRET,
        algorithm="HS256",
    )
    if isinstance(token, bytes):
        token = token.decode("ascii")
    return jsonify({"token": token})


@app.get("/me")
def me():
    claims, error = require()
    if error:
        return error
    return jsonify({"user": claims["sub"], "role": claims["role"]})


@app.get("/reports")
def reports():
    _claims, error = require({"admin", "user"})
    if error:
        return error
    return jsonify({"reports": ["quarterly-summary"]})


@app.get("/admin/stats")
def stats():
    _claims, error = require({"admin"})
    if error:
        return error
    return jsonify({"users": len(USERS)})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001)
