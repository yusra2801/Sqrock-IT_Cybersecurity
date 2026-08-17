
# Day 10 — Baiting & Watering Hole Attack Simulation

## Objective
Understand drive-by download logic and build a honeypot link tracker.

## Theory
- Baiting: physical (USB, CD) or digital (fake download link) traps that rely on curiosity or greed.
- Watering hole: instead of attacking a target directly, the attacker compromises a website the target regularly visits.
- Defense: web filtering, script blocking (e.g. NoScript), and consistent patch management.

## What the script does
`honeypot_server.py` runs a local web server that acts as a "bait" link. Every visit is logged with timestamp, client IP, requested path, and full request headers (including User-Agent, browser details, and OS).

## Tools used
- `http.server` (stdlib)
- `json`, `datetime` (stdlib)

## Demo & Log Analysis
Visiting `http://localhost:8000` in a browser triggered two logged requests: the page itself (`/`) and the browser's automatic favicon request (`/favicon.ico`).

Captured data included:
- **Client IP:** 127.0.0.1 (local test)
- **Timestamp:** exact visit time
- **User-Agent:** revealed browser (Chrome 151), rendering engine, and OS (Windows 10, 64-bit)
- **Accept-Language, Referer, and other headers:** additional fingerprinting detail

This shows how a single click on a bait link can silently reveal a visitor's IP, browser, OS, and language settings — information an attacker could use to pick a targeted exploit or track a specific user.

## Mitigation Report
1. **Web filtering** — block known malicious/untrusted domains at the network level before users can reach them.
2. **Script/ad blocking** — extensions like NoScript or uBlock Origin prevent unknown scripts from silently executing.
3. **Patch management** — keep browsers and OS updated, closing vulnerabilities that drive-by downloads rely on.
4. **User awareness** — train users to be suspicious of "too good to be true" download offers and unexpected links, even on familiar sites.
5. **Least privilege browsing** — avoid browsing as an admin/root user, limiting the damage a successful drive-by attack could cause.

## Deliverable
Server demo + log analysis of captured "victims" + mitigation report.