"""Fetch one URL and report common security headers. Use a site you are allowed to request."""

from __future__ import annotations

import sys
import urllib.request

EXPECTED = (
    "content-security-policy",
    "strict-transport-security",
    "x-content-type-options",
    "x-frame-options",
    "referrer-policy",
    "permissions-policy",
)


def main() -> None:
    if len(sys.argv) != 2 or not sys.argv[1].startswith("https://"):
        print("usage: python check_headers.py https://example.com")
        sys.exit(1)
    request = urllib.request.Request(sys.argv[1], headers={"User-Agent": "header-check-lab/1.0"})
    with urllib.request.urlopen(request, timeout=15) as response:
        headers = {key.lower(): value for key, value in response.headers.items()}
    print(f"status {response.status}  {sys.argv[1]}")
    for name in EXPECTED:
        if name in headers:
            print(f"present  {name}: {headers[name][:80]}")
        else:
            print(f"missing  {name}")


if __name__ == "__main__":
    main()
