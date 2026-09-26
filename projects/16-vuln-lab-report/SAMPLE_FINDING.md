# Sample finding — reflected XSS on a lab app

This describes a class of bug on OWASP Juice Shop or DVWA. It does not include a working exploit.

- Asset: the lab search box, in scope for the local VM only.
- What happened: text from the search box came back in the page as HTML instead of as plain text.
- Why that matters: a script in that text could run in the browser of the next person who opens the link.
- Fix: encode the output, and send a Content-Security-Policy that does not allow unexpected scripts.
- Evidence to attach in a real test: the request time, the parameter name, and a screenshot of the page treating the input as text after the fix.

Practice this only on Juice Shop, DVWA, or the PortSwigger Academy. Do not try it on a site you do not own.
