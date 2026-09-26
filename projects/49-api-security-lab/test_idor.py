"""Call the broken route and the fixed route. Start the API first, or import the app."""

from __future__ import annotations

import urllib.error
import urllib.request

from vulnerable_api import app


def live(path: str, user: str) -> tuple[int, str]:
    request = urllib.request.Request(
        f"http://127.0.0.1:5005{path}",
        headers={"X-User": user},
    )
    try:
        with urllib.request.urlopen(request, timeout=2) as response:
            return response.status, response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode("utf-8")


def main() -> None:
    try:
        broken_status, broken_body = live("/account/bob", "alice")
        secure_status, secure_body = live("/secure/account/bob", "alice")
        own_status, own_body = live("/secure/account/alice", "alice")
    except OSError:
        client = app.test_client()
        broken = client.get("/account/bob", headers={"X-User": "alice"})
        denied = client.get("/secure/account/bob", headers={"X-User": "alice"})
        own = client.get("/secure/account/alice", headers={"X-User": "alice"})
        broken_status, broken_body = broken.status_code, broken.get_data(as_text=True)
        secure_status, secure_body = denied.status_code, denied.get_data(as_text=True)
        own_status, own_body = own.status_code, own.get_data(as_text=True)
        print("API was not listening; used the in-process test client.")
    print(f"broken GET /account/bob as alice -> {broken_status} {broken_body.strip()}")
    print(f"secure GET /secure/account/bob as alice -> {secure_status} {secure_body.strip()}")
    print(f"secure GET /secure/account/alice as alice -> {own_status} {own_body.strip()}")


if __name__ == "__main__":
    main()
