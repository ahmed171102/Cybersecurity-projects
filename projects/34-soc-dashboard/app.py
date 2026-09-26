"""Small alert board. Listens on 127.0.0.1:5003."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from flask import Flask, redirect, render_template_string, request

ROOT = Path(__file__).resolve().parent
STORE = ROOT / "alerts.json"
app = Flask(__name__)
STATUSES = ("open", "triaging", "closed")

PAGE = """
<!doctype html>
<title>SOC</title>
<h1>Alerts</h1>
<p>open {{ counts.get('open', 0) }} · triaging {{ counts.get('triaging', 0) }} · closed {{ counts.get('closed', 0) }}</p>
{% for alert in alerts %}
  <form method="post" action="/alert/{{ alert['id'] }}">
    <strong>{{ alert['severity'] }}</strong> {{ alert['title'] }}
    <select name="status">
      {% for status in statuses %}
        <option value="{{ status }}" {% if alert['status'] == status %}selected{% endif %}>{{ status }}</option>
      {% endfor %}
    </select>
    <button>Save</button>
  </form>
{% endfor %}
"""


def load() -> list[dict]:
    if not STORE.exists():
        return []
    return json.loads(STORE.read_text(encoding="utf-8"))


def save(alerts: list[dict]) -> None:
    STORE.write_text(json.dumps(alerts, indent=2) + "\n", encoding="utf-8")


@app.get("/")
def home():
    alerts = load()
    counts = Counter(item["status"] for item in alerts)
    return render_template_string(PAGE, alerts=alerts, counts=counts, statuses=STATUSES)


@app.post("/alert/<alert_id>")
def update(alert_id: str):
    status = request.form.get("status", "")
    if status not in STATUSES:
        return "bad status", 400
    alerts = load()
    for alert in alerts:
        if alert["id"] == alert_id:
            alert["status"] = status
    save(alerts)
    return redirect("/")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5003)
