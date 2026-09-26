"""Lab API: a broken object check beside a fixed one. 127.0.0.1:5005."""

from __future__ import annotations

from flask import Flask, jsonify, request

app = Flask(__name__)
ACCOUNTS = {
    "alice": {"id": "alice", "email": "alice@example.com", "balance": 40},
    "bob": {"id": "bob", "email": "bob@example.com", "balance": 12},
    "carol": {"id": "carol", "email": "carol@example.com", "balance": 7},
}


def caller() -> str:
    return request.headers.get("X-User", "alice")


@app.get("/account/<account_id>")
def broken(account_id: str):
    """Returns any account. This is the insecure direct object reference."""
    record = ACCOUNTS.get(account_id)
    if record is None:
        return jsonify({"error": "missing"}), 404
    return jsonify(record)


@app.get("/secure/account/<account_id>")
def secure(account_id: str):
    user = caller()
    if user != account_id:
        return jsonify({"error": "forbidden", "caller": user, "asked": account_id}), 403
    record = ACCOUNTS.get(account_id)
    if record is None:
        return jsonify({"error": "missing"}), 404
    return jsonify(record)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5005)
