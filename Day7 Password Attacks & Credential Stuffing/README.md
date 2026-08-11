# Day 7 — Password Attacks & Credential Stuffing

## Objective
Understand brute-force login logic and build a rate-limit detector as a defense mechanism.

## Theory
- Credential stuffing: using leaked username:password combos from one breach on other sites.
- Brute force = systematic guessing. Dictionary attack = using a wordlist of common passwords.
- Defense: account lockout, CAPTCHA, MFA, and breach monitoring.

## What was built
1. `test_server.py` — a local Flask lab server with a `/login` endpoint, used only for controlled testing (never a real website).
2. `brute_force_attacker.py` — simulates a brute-force attack by trying a wordlist of common passwords against the local server.
3. Rate limiting was added to `test_server.py` using `flask-limiter`, restricting each IP to 5 login attempts per minute.

## Tools used
- `requests`
- `Flask`
- `flask-limiter`

## Demo Results

**Without rate limiting:**
The attacker script found the correct password (`admin:sqrock123`) after 6 attempts — no restriction stopped it.

**With rate limiting (5 requests/minute):**
The server returned `401 Unauthorized` for the first 5 attempts, then `429 Too Many Requests` for the 6th — even the correct password (`sqrock123`) failed because the limit was already hit. This demonstrates how rate limiting can make brute-force attacks impractical.

## Defense Implementation
```python
limiter = Limiter(get_remote_address, app=app, default_limits=["5 per minute"])
```
This restricts each IP address to 5 requests per minute on the login endpoint, blocking further attempts with a 429 status once the limit is exceeded.

## Deliverable
Script demo on local lab + defensive implementation (rate limiter in Flask).