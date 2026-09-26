# How to run

From the repository root.

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export PYTHONPATH=$(pwd)
python3 scripts/smoke_test.py
python3 projects/05-subnet-calculator/subnet.py 192.168.1.10/24 --binary
python3 projects/14-log-analyzer/analyze.py projects/14-log-analyzer/sample_auth.log
python3 projects/27-siem-lite/siem.py ingest && python3 projects/27-siem-lite/siem.py alerts
python3 projects/23-zerotrust-api/app.py
python3 projects/31-secure-webapp/app.py
python3 projects/34-soc-dashboard/build_sample_alerts.py && python3 projects/34-soc-dashboard/app.py
python3 projects/49-api-security-lab/vulnerable_api.py
python3 projects/49-api-security-lab/test_idor.py
```

`PYTHONPATH` must be the repo root. Projects 07, 09, 10, 11, 24, and 26 import `shared.crypto_utils`. Each of those scripts also inserts the repo root onto `sys.path`, so they still run if you forget the variable. Set it anyway. That is how a second script in the same terminal finds the package.

On Windows, `python` is usually the right command, and the virtualenv activate script is `.venv\Scripts\Activate.ps1`. Set the path with `$env:PYTHONPATH = (Get-Location).Path`.

The four Flask apps bind to loopback only:

| App | URL |
| --- | --- |
| Zero-trust API | http://127.0.0.1:5001 |
| Notes app | http://127.0.0.1:5002 |
| SOC dashboard | http://127.0.0.1:5003 |
| IDOR lab | http://127.0.0.1:5005 |

Start project 49’s API, then run `test_idor.py` in a second terminal. The test prints the broken route and the fixed route.

`python3 scripts/smoke_test.py` is finished when the last line says `failed: 0`.
