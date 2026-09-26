# STRIDE for the notes app

The app is project 31. The diagram is `diagram.mmd`.

| Letter | Threat | Where | Control already in the lab |
| --- | --- | --- | --- |
| S | Spoofing | Login form | Password hash, session cookie |
| T | Tampering | Note form | Hidden CSRF field |
| R | Repudiation | Notes table | Owner column on each row |
| I | Information disclosure | SQL query | `WHERE owner = ?` |
| D | Denial of service | Note body | Add a length limit before this is a real service |
| E | Elevation of privilege | Any future admin route | Separate roles, see project 23 |
