"""TCP chat client for 127.0.0.1:9000. One line in, one line out."""

from __future__ import annotations

import socket
import threading

HOST = "127.0.0.1"
PORT = 9000


def listen(conn: socket.socket) -> None:
    buffer = b""
    try:
        while True:
            chunk = conn.recv(1024)
            if not chunk:
                print("\nserver closed")
                break
            buffer += chunk
            while b"\n" in buffer:
                raw, buffer = buffer.split(b"\n", 1)
                print(raw.decode("utf-8", errors="replace"))
    except OSError:
        return


def main() -> None:
    conn = socket.create_connection((HOST, PORT))
    threading.Thread(target=listen, args=(conn,), daemon=True).start()
    try:
        while True:
            line = input()
            conn.sendall((line + "\n").encode("utf-8"))
            if line.strip() == "/quit":
                break
    except (EOFError, KeyboardInterrupt):
        pass
    finally:
        conn.close()


if __name__ == "__main__":
    main()
