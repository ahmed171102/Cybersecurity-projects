"""Print a mobile-app review list. Own apps and lab builds only."""

from __future__ import annotations

ITEMS = [
    "Hard-coded keys in the binary or a resource file. Search for api_key and Authorization.",
    "Plaintext storage: tokens in shared preferences or a world-readable file. Prefer the platform keystore.",
    "Missing TLS, or TLS that accepts any certificate. The app should refuse a broken chain.",
    "Extra permissions the feature does not need (contacts, location, microphone).",
    "Debug flags left on in a release build (debuggable, verbose logs).",
    "Logs that print tokens, passwords, or personal data. TLS on the wire does not help a log file.",
]


def main() -> None:
    print("Mobile app review. Use a build you own or a teaching app.\n")
    for index, item in enumerate(ITEMS, start=1):
        print(f"{index}. {item}")
    print("\nTLS is the one you fail first if the login traffic is clear text.")


if __name__ == "__main__":
    main()
