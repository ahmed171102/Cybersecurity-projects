# 03 — TCP chat

## What this is

A multi-client chat that listens only on `127.0.0.1:9000`. Messages are one line each. `/name` sets your name. `/quit` disconnects. Everyone else receives the line.

## Why it matters

TCP is a stream, not a pile of messages. The newline is the frame that turns the stream back into messages. The same idea shows up in logs and in HTTP.

## How to run

Use three terminals.

```bash
python3 projects/03-tcp-chat/server.py
python3 projects/03-tcp-chat/client.py
python3 projects/03-tcp-chat/client.py
```

In a client, type `/name ahmed` and then a sentence. The other client should print it.

## Portfolio deliverable

A short note that explains newline framing and why the server binds to loopback instead of every interface.

## Exercise

Start a third client and confirm a line from client 1 reaches both others. Then send a line without a newline habit: the other side should wait until you press Enter. That is framing.

