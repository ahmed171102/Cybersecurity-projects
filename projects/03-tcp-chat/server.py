"""TCP chat server. Binds to 127.0.0.1:9000 only."""

from __future__ import annotations

import socket
import threading

HOST = "127.0.0.1"
PORT = 9000
clients: dict[socket.socket, str] = {}
lock = threading.Lock()


def send_line(conn: socket.socket, text: str) -> None:
    conn.sendall((text + "\n").encode("utf-8"))


def broadcast(sender: socket.socket, text: str) -> None:
    with lock:
        targets = list(clients)
    for conn in targets:
        if conn is sender:
            continue
        try:
            send_line(conn, text)
        except OSError:
            with lock:
                clients.pop(conn, None)


def handle(conn: socket.socket) -> None:
    with lock:
        clients[conn] = "anon"
    buffer = b""
    try:
        send_line(conn, "welcome. commands: /name YOURNAME  /quit")
        while True:
            chunk = conn.recv(1024)
            if not chunk:
                break
            buffer += chunk
            while b"\n" in buffer:
                raw, buffer = buffer.split(b"\n", 1)
                text = raw.decode("utf-8", errors="replace").strip()
                if text.startswith("/name "):
                    name = text.split(" ", 1)[1].strip() or "anon"
                    with lock:
                        clients[conn] = name
                    send_line(conn, f"name set to {name}")
                elif text == "/quit":
                    return
                elif text:
                    with lock:
                        name = clients[conn]
                    broadcast(conn, f"{name}: {text}")
    finally:
        with lock:
            name = clients.pop(conn, "anon")
        conn.close()
        broadcast(conn, f"{name} left")


def main() -> None:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print(f"listening on {HOST}:{PORT}")
    while True:
        conn, _addr = server.accept()
        threading.Thread(target=handle, args=(conn,), daemon=True).start()


if __name__ == "__main__":
    main()
