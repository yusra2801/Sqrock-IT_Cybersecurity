# Day 16 — HTTP Security Header Analysis

## Objective
Audit an HTTP server's response headers to check whether it follows
security best practices around transport, script execution policy,
clickjacking, and MIME sniffing protection.

## How it works
`verify_headers.py` sends a `GET` request to a target URL and checks the
response for four security-relevant headers:

| Header | Purpose |
|---|---|
| `Strict-Transport-Security` | Forces the browser to only use HTTPS |
| `Content-Security-Policy` | Restricts where scripts/resources can load from (mitigates XSS) |
| `X-Frame-Options` | Blocks the page from being embedded in an iframe (mitigates clickjacking) |
| `X-Content-Type-Options` | Stops the browser from guessing file types (mitigates MIME-sniffing attacks) |

Any missing header is flagged as `VULNERABLE`.

## How to run
```bash
# 1. Start an isolated local target (never point this at real infrastructure)
python -m http.server 8000

# 2. In another terminal, run the audit
python verify_headers.py
```

## Result
Run against a local test server, all four headers were reported missing —
expected, since Python's bare `http.server` sets no security headers by
default. Full output in [`run_output.txt`](./run_output.txt).

## Deliverable
See [`Day16_CSP_Analysis.docx`](./Day16_CSP_Analysis.docx) for the
analytical breakdown of how CSP prevents cross-site script loading.